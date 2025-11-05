for test in ['', ' ', 'lower', 'UPPER', 'Initial', 'dromedaryCase', 'CamelCase', 'ABCWordDEF', 'CamelCaseXYZand123.how23^ar23e you doing AndABC123XYZdf']:
    print test + ':' + str(splitWords(test))
