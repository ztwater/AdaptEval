from unicodedata import combining, normalize

LATIN = "ä  æ  ǽ  đ ð ƒ ħ ı ł ø ǿ ö  œ  ß  ŧ ü "
ASCII = "ae ae ae d d f h i l o o oe oe ss t ue"

def remove_diacritics(s, outliers=str.maketrans(dict(zip(LATIN.split(), ASCII.split())))):
    return "".join(c for c in normalize("NFD", s.lower().translate(outliers)) if not combining(c))
