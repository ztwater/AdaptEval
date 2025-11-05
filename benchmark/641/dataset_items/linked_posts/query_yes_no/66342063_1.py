def yes_or_no(question):
    """Simple Yes/No Function."""
    prompt = f'{question} ? (y/n): '
    answer = input(prompt).strip().lower()
    if answer not in ['y', 'n']:
        print(f'{answer} is invalid, please try again...')
        return yes_or_no(question)
    if answer == 'y':
        return True
    return False

def main():
    """Run main function."""
    answer = yes_or_no("Do you know who Novak Djokovic is?")
    print(f'you answer was: {answer}')


if __name__ == '__main__':
    main()
