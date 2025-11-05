def ask(question, default = None):
    hasDefault = default is not None
    prompt = (question 
               + " [" + ["y", "Y"][hasDefault and default] + "/" 
               + ["n", "N"][hasDefault and not default] + "] ")

    while True:
        sys.stdout.write(prompt)
        choice = input().strip().lower()
        if choice == '':
            if default is not None:
                return default
        else:
            if "yes".startswith(choice):
                return True
            if "no".startswith(choice):
                return False

        sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
