tests = [
    "XYZCamelCase",
    "CamelCaseXYZ",
    "Camel_CaseXYZ",
    "3DCamelCase",
    "Camel5Case",
    "Camel5Case5D",
    "Camel Case XYZ"
]

for test in tests:
    print(test, "=>", camel_terms(test))
