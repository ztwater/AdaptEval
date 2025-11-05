Public Function GetStockData() As String
    Dim qurl As String
    Dim cookie As String
    Dim crumb As String
    Dim req As Object
    Dim cookieurl As String

    cookieurl = "https://fc.yahoo.com" 'This page needs to return a cookie, query1.finance.yahoo does not return cookie.
    
    Set req = CreateObject("WinHttp.WinHttpRequest.5.1")
    
    'get cookie
    With req
        .Open "GET", cookieurl, False
        .setRequestHeader "REFERER", cookieurl
        .setRequestHeader "User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        .Send
        
        cookie = .getResponseHeader("Set-Cookie") 'gets cookie and saves it.
    End With
   
    'get crumb
    With req
        .Open "GET", "https://query2.finance.yahoo.com/v1/test/getcrumb", False 'gets crumb, which must be attached to all quote calls
        .setRequestHeader "REFERER", cookieurl
        .setRequestHeader "User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        .setRequestHeader "Cookie", cookie 'applies cookie to header, currently working without this, but probably good practice to use it
        .Send
        
        crumb = .responseText 'saves crumb
    End With
    
    qurl = "http://query1.finance.yahoo.com/v7/finance/quote?symbols=AAPL"
  
    qurl = qurl & "&crumb=" & crumb 'add crumb info from GetCookie sub
    

    'get data
    With req
        .Open "GET", qurl, False
        'header is needed but not specific, could probbaly remove a couple lines without creating a problem
        .setRequestHeader "REFERER", cookieurl
        .setRequestHeader "User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        .setRequestHeader "Cookie", cookie
        .Send
        GetStockData = .responseText 'get data and return
    End With
End Function