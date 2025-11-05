def yes_no(question_to_be_answered):
    while True:
        choice = input(question_to_be_answered).lower()
        if choice[:1] == 'y': 
            return True
        elif choice[:1] == 'n':
            return False
        else:
            print("Please respond with 'Yes' or 'No'\n")

#See it in Practice below 

musical_taste = yes_no('Do you like Pine Coladas?')
if musical_taste == True:
    print('and getting caught in the rain')
elif musical_taste == False:
    print('You clearly have no taste in music')
