import os
if os.environ.get('PYTEST_RUNNING', '') == 'true':
    print('pytest is running')
