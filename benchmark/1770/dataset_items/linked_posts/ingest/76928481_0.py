Public crumb As String
Public cookie As String

Public Sub YahooGetCrumb()
    Dim http As MSXML2.XMLHTTP60
    Dim strHeader As String
    Dim strFields() As String
    
    Set http = New MSXML2.XMLHTTP60
    
    http.Open "GET", "https://fc.yahoo.com"
    http.setRequestHeader "User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    http.send
    
    strHeader = http.getAllResponseHeaders
    strFields = Split(strHeader, vbCrLf)
    cookie = Trim(Split(Split(strFields(5), ";")(0), ":")(1)) & "; " & Trim(Split(Split(strFields(6), ";")(0), ":")(1))

    http.Open "GET", "https://query2.finance.yahoo.com/v1/test/getcrumb"
    http.setRequestHeader "User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    http.setRequestHeader "Cookie", cookie
    http.send
    
    crumb = http.responseText
    
End Sub

Public Function GetYahooData(sSymbol As String) As String
    Dim http As MSXML2.XMLHTTP60
    
    If crumb = "" Then
        YahooGetCrumb
    End If
    
    Set http = New MSXML2.XMLHTTP60
    
    http.Open "GET", "https://query2.finance.yahoo.com/v7/finance/quote?symbols=" & sSymbol & "&crumb=" & crumb, False
    http.setRequestHeader "User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    http.send
    
    GetYahooData = http.responseText
    
End Function

Public Sub test()
    Dim JSON As Object

    responseText = GetYahooData("AAPL")
    
    Set JSON = ParseJson(responseText)
end Sub    
