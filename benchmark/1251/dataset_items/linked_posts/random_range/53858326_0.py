from random import randint

data = []

def unique_rand(inicial, limit, total):

        data = []

        i = 0

        while i < total:
            number = randint(inicial, limit)
            if number not in data:
                data.append(number)
                i += 1

        return data


data = unique_rand(1, 60, 6)

print(data)


"""

prints something like 

[34, 45, 2, 36, 25, 32]

"""
