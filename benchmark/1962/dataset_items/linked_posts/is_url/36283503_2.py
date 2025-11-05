my_list = [
    "http://www.cwi.nl:80/%7Eguido/Python.html",
    "/data/Python.html",
    532,
    type("FooObject", (), {"decode": None})(),
    "dkakasdkjdjakdjadjfalskdjfalk",
    "https://stackoverflow.com",
]

for item in my_list:
    try:
        print(f"{item} is valid: {is_valid(item)}")
    except (AttributeError, TypeError) as e:
        print(e)
