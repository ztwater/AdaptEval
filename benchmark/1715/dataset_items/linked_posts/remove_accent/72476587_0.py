from sklearn.feature_extraction.text import strip_accents_ascii, strip_accents_unicode

accented_string = u'Málagueña®'

print(strip_accents_unicode(accented_string)) # output: Malaguena®
print(strip_accents_ascii(accented_string)) # output: Malaguena

