functions = []

print(f"Before loop: local i = {locals().get('i')}, global i = {globals().get('i')}")

for i in range(3):
    print(f"Inside loop: local i = {locals().get('i')}, global i = {globals().get('i')}")
    def f():
        print(f"Inside f(): local i = {locals().get('i')}, global i = {globals().get('i')}")
        return i
    functions.append(f)

print(f"After loop: local i = {locals().get('i')}, global i = {globals().get('i')}")

print([f() for f in functions])
