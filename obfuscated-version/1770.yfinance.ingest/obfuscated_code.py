import requests

var_0 = 'https://query2.finance.yahoo.com'
var_1 = { 
  "User-Agent": 
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
}

def getCredentials(var_2='https://fc.yahoo.com', var_3=apiBase+'/v1/test/getcrumb'):
  var_4 = requests.get(cookieUrl).cookies
  var_5 = requests.get(url=crumbUrl, cookies=cookie, headers=headers).text
  return {'cookie': var_4, 'crumb': var_5}

def quote(var_6, var_7):
  var_8 = var_0 + '/v7/finance/quote'
  var_9 = {'symbols': ','.join(var_6), 'crumb': var_7['crumb']}
  var_10 = requests.get(var_8, var_9=var_9, cookies=var_7['cookie'], var_1=var_1)
  var_11 = var_10.json()['quoteResponse']['result']
  return var_11

var_7 = getCredentials()
var_11 = quote(['GOOG', 'TSLA'], var_7)
if var_11:
  for quote in var_11:
    print(f"{quote['symbol']} price is {quote['currency']} {quote['regularMarketPrice']}")
 