class Hey():
    pass

hey_type = globals().get("Hey")

hey_instance_1 = Hey()
hey_instance_2 = hey_type()

print(type(hey_instance_1))
print(type(hey_instance_2))
