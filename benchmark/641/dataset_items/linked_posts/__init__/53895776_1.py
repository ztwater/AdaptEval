import re
text = "RULES OF LIFE: I. STAY CURIOUS; II. NEVER STOP LEARNING"
text = re.sub(r'(?=\b[MCDXLVI]{1,6}\b)M{0,4}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})', 'ROMAN', text)
print(text)
