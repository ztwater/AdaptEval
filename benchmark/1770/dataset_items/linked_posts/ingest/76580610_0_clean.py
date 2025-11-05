import requests

apiBase = 'https://query2.finance.yahoo.com'
headers = { 
  "User-Agent": 
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
}

def getCredentials(cookieUrl='https://fc.yahoo.com', crumbUrl=apiBase+'/v1/test/getcrumb'):
  cookie = requests.get(cookieUrl).cookies
  crumb = requests.get(url=crumbUrl, cookies=cookie, headers=headers).text
  return {'cookie': cookie, 'crumb': crumb}

def quote(symbols, credentials):
  url = apiBase + '/v7/finance/quote'
  params = {'symbols': ','.join(symbols), 'crumb': credentials['crumb']}
  response = requests.get(url, params=params, cookies=credentials['cookie'], headers=headers)
  quotes = response.json()['quoteResponse']['result']
  return quotes

credentials = getCredentials()
quotes = quote(['GOOG', 'TSLA'], credentials)
if quotes:
  for quote in quotes:
    print(f"{quote['symbol']} price is {quote['currency']} {quote['regularMarketPrice']}")
 