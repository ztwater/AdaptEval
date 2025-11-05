from your_tests import TestSequenceFunctions
print('\n'.join([f.__name__ for f in dir(TestSequenceFunctions) if f.__name__.startswith('test_')]))
