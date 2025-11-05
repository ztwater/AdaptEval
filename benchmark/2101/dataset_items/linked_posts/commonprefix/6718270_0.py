a = ["my_prefix_what_ever", "my_prefix_what_so_ever", "my_prefix_doesnt_matter"]
b = zip(*a)
c = [x[0] for x in b if x==(x[0],)*len(x)]
result = "".join(c)
