def median(data):
    new_list = sorted(data)
    if len(new_list)%2 > 0:
        return new_list[len(new_list)/2]
    elif len(new_list)%2 == 0:
        return (new_list[(len(new_list)/2)] + new_list[(len(new_list)/2)-1]) /2.0

print median([1,2,3,4,5,9])
