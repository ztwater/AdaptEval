answer = input('Please indicate approval: [y/n]')
if not answer or answer[0].lower() != 'y':
    print('You did not indicate approval')
    exit(1)
