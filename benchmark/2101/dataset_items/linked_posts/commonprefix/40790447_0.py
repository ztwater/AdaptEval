a = ["my_prefix_what_ever", "my_prefix_what_so_ever", "my_prefix_doesnt_matter"]

list = [all(x[i] == x[i+1] for i in range(len(x)-1)) for x in zip(*a)]

print a[0][:list.index(0) if list.count(0) > 0 else len(list)]
