function ConvertFrom-RomanNumeral
{
  <#
    .SYNOPSIS
        Converts a Roman numeral to a number.
    .DESCRIPTION
        Converts a Roman numeral - in the range of I..MMMCMXCIX - to a number.
    .EXAMPLE
        ConvertFrom-RomanNumeral -Numeral MMXIV
    .EXAMPLE
        "MMXIV" | ConvertFrom-RomanNumeral
  #>
    [CmdletBinding()]
    [OutputType([int])]
    Param
    (
        [Parameter(Mandatory=$true,
                   HelpMessage="Enter a roman numeral in the range I..MMMCMXCIX",
                   ValueFromPipeline=$true,
                   Position=0)]
        [ValidatePattern("^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")]
        [string]
        $Numeral
    )

    Begin
    {
        $RomanToDecimal = [ordered]@{
            M  = 1000
            CM =  900
            D  =  500
            CD =  400
            C  =  100
            XC =   90
            L  =   50
            X  =   10
            IX =    9
            V  =    5
            IV =    4
            I  =    1
        }
    }
    Process
    {
        $roman = $Numeral + " "
        $value = 0

        do
        {
            foreach ($key in $RomanToDecimal.Keys)
            {
                if ($key.Length -eq 1)
                {
                    if ($key -match $roman.Substring(0,1))
                    {
                        $value += $RomanToDecimal.$key
                        $roman  = $roman.Substring(1)
                        break
                    }
                }
                else
                {
                    if ($key -match $roman.Substring(0,2))
                    {
                        $value += $RomanToDecimal.$key
                        $roman  = $roman.Substring(2)
                        break
                    }
                }
            }
        }
        until ($roman -eq " ")

        $value
    }
    End
    {
    }
}

function ConvertTo-RomanNumeral
{
  <#
    .SYNOPSIS
        Converts a number to a Roman numeral.
    .DESCRIPTION
        Converts a number - in the range of 1 to 3,999 - to a Roman numeral.
    .EXAMPLE
        ConvertTo-RomanNumeral -Number (Get-Date).Year
    .EXAMPLE
        (Get-Date).Year | ConvertTo-RomanNumeral
  #>
    [CmdletBinding()]
    [OutputType([string])]
    Param
    (
        [Parameter(Mandatory=$true,
                   HelpMessage="Enter an integer in the range 1 to 3,999",
                   ValueFromPipeline=$true,
                   Position=0)]
        [ValidateRange(1,3999)]
        [int]
        $Number
    )

    Begin
    {
        $DecimalToRoman = @{
            Ones      = "","I","II","III","IV","V","VI","VII","VIII","IX";
            Tens      = "","X","XX","XXX","XL","L","LX","LXX","LXXX","XC";
            Hundreds  = "","C","CC","CCC","CD","D","DC","DCC","DCCC","CM";
            Thousands = "","M","MM","MMM"
        }

        $column = @{Thousands = 0; Hundreds = 1; Tens = 2; Ones = 3}
    }
    Process
    {
        [int[]]$digits = $Number.ToString().PadLeft(4,"0").ToCharArray() |
                            ForEach-Object { [Char]::GetNumericValue($_) }

        $RomanNumeral  = ""
        $RomanNumeral += $DecimalToRoman.Thousands[$digits[$column.Thousands]]
        $RomanNumeral += $DecimalToRoman.Hundreds[$digits[$column.Hundreds]]
        $RomanNumeral += $DecimalToRoman.Tens[$digits[$column.Tens]]
        $RomanNumeral += $DecimalToRoman.Ones[$digits[$column.Ones]]

        $RomanNumeral
    }
    End
    {
    }
}
