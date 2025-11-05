def question(question, answers):
    acceptable = False
    while not acceptable:
        print(question + "specify '%s' or '%s'") % answers
        answer = raw_input()
        if answer.lower() == answers[0].lower() or answers[0].lower():
            print('Answer == %s') % answer
            acceptable = True
    return answer

raining = question("Is it raining today?", ("Y", "N"))
