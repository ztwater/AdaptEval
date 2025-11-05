def get_percentile(data, percentile):
    # Get the number of observations
    cnt=len(data)
    # Sort the list
    data=sorted(data)
    # Determine the split point
    i=(cnt-1)*percentile
    # Find the `floor` of the split point
    diff=i-int(i)
    # Return the weighted average of the value above and below the split point
    return data[int(i)]*(1-diff)+data[int(i)+1]*(diff)

# Data
data=[1,2,3,4,5]
# For the median
print(get_percentile(data=data, percentile=.50))
# > 3
print(get_percentile(data=data, percentile=.75))
# > 4

# Note the weighted average difference when an int is not returned by the percentile
print(get_percentile(data=data, percentile=.51))
# > 3.04

