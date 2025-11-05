    # ► Create $session Object
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$Stock = "MSFT" 

    # ► Call 1st Url ( Gain some headers and cookies stuff ) - using try & catch to prevent 404 error ( as mentioned above )
try { Invoke-WebRequest -UseBasicParsing -Uri "https://fc.yahoo.com/" -SessionVariable session } catch {
  $null}        
        

    # ► Call 2nd Url ( Generate Crumb ) 
$crumb = Invoke-WebRequest -UseBasicParsing -Uri "https://query2.finance.yahoo.com/v1/test/getcrumb" -WebSession $session


    # ► Call 3rd Url ( Get Yahoo's Data ) 
$URL = $("https://query2.finance.yahoo.com/v10/finance/quoteSummary/" + $Stock + "?modules=price&crumb=" + $crumb)
$ResponseText = Invoke-WebRequest -UseBasicParsing -Uri $URL -WebSession $session

    
    # ► Print Result
$ResponseText = $ResponseText.ToString()
$ResponseText 
