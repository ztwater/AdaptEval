answer = set()
sampleSize = 10
answerSize = 0

while answerSize < sampleSize:
    r = random.randint(0,100)
    if r not in answer:
        answerSize += 1
        answer.add(r)

# answer now contains 10 unique, random integers from 0.. 100
