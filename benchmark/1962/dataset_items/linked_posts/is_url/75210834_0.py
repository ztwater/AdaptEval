from requests import get, HTTPError, ConnectionError
from pydantic import BaseModel, AnyHttpUrl, ValidationError
    
class MyConfModel(BaseModel):
    URI: AnyHttpUrl

try:
    myAddress = MyConfModel(URI = "http://myurl.com/")
    req = get(myAddress.URI, verify=False)
    print(myAddress.URI)

except(ValidationError):
    print('Invalid destination')
