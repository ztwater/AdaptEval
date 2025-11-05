iterable = [1,2,3] # Your date
iterator = iter(iterable) # get the data iterator

try :   # wrap all in a try / except
    while 1 : 
        item = iterator.next() 
        print item # put the "for loop" code here
except StopIteration, e : # make the process on the last element here
    print item
