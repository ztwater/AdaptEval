In [46]: names = (i for i in ('The CIO, Reed', 'The homeless guy, Arnot', 'The security guard Spencer'))

In [47]: po = (f'Strangely, {next(names)} has a nice {i}' for i in (" nice house", " fast car", " big boat"))

In [48]: while True:  
...:     try:  
...:         print(next(po))  
...:     except StopIteration:  
...:         break  
...:       
Strangely, The CIO, Reed has a nice  nice house  
Strangely, The homeless guy, Arnot has a nice  fast car  
Strangely, The security guard Spencer has a nice  big boat  
