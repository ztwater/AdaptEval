> easy_install lepl
...
> python
...
>>> from lepl.apps.rfc3696 import HttpUrl
>>> validator = HttpUrl()
>>> validator('google')
False
>>> validator('http://google')
False
>>> validator('http://google.com')
True
