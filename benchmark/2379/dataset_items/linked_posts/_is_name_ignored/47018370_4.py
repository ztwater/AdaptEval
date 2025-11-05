>>> def delta(*numbers):
...     try:
...         return max(numbers) - min(numbers)
...     except TypeError:
...         raise ValueError("delta should only be called with numerical arguments") from None
...     except ValueError:
...         return -1 # or None
... 
>>> 
>>> delta()
-1
