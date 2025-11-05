import distutils

if unsafe_case:
    print('Proceed with potentially unsafe thing? [y/n]')
    while True:
        try:
            verify = distutils.util.strtobool(raw_input())
            if not verify:
                raise SystemExit  # Abort on user reject
            break
        except ValueError as err:
            print('Please enter \'yes\' or \'no\'')
            # Try again
    print('Continuing ...')
do_unsafe_thing()
