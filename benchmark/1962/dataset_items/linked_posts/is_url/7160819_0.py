from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

val = URLValidator()
try:
    val('httpx://www.google.com')
except (ValidationError,) as e: 
    print(e)
