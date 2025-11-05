# Count the no. of elements in the list
ListLength = len(MyList)
# Initialize a counter
count = 0

for i in MyList:
    # increment counter
    count += 1
    # Check if 'i' is the last element in the list
    # by using the counter
    if count == ListLength:
        # Do something different for the last
    else:
        # Do something for all other elements
