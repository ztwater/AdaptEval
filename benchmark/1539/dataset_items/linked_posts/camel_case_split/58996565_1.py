TESTS = [
    ("XYZCamelCase", ['XYZ', 'Camel', 'Case']),
    ("CamelCaseXYZ", ['Camel', 'Case', 'XYZ']),
    ("CamelCaseXYZa", ['Camel', 'Case', 'XY', 'Za']),
    ("XYZCamelCaseXYZ", ['XYZ', 'Camel', 'Case', 'XYZ']),
    ("aCamelCaseWordT", ['a', 'Camel', 'Case', 'Word', 'T']),
    ("CamelCaseWordT", ['Camel', 'Case', 'Word', 'T']),
    ("CamelCaseWordTa", ['Camel', 'Case', 'Word', 'Ta']),
    ("aCamelCaseWordTa", ['a', 'Camel', 'Case', 'Word', 'Ta']),
    ("Ta", ['Ta']),
    ("aT", ['a', 'T']),
    ("a", ['a']),
    ("T", ['T']),
    ("", []),
]

def test():
    for (q,a) in TESTS:
        assert camel_case_split(q) == a

if __name__ == "__main__":
    test()
