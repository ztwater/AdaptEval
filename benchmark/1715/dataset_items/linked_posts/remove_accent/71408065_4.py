LATIN = "ä  æ  ǽ  đ ð ƒ ħ ı ł ø ǿ ö  œ  ß  ŧ ü  Ä  Æ  Ǽ  Đ Ð Ƒ Ħ I Ł Ø Ǿ Ö  Œ  ẞ  Ŧ Ü "
ASCII = "ae ae ae d d f h i l o o oe oe ss t ue AE AE AE D D F H I L O O OE OE SS T UE"

def remove_diacritics(s, outliers=str.maketrans(dict(zip(LATIN.split(), ASCII.split())))):
    return "".join(c for c in normalize("NFD", s.translate(outliers)) if not combining(c))

