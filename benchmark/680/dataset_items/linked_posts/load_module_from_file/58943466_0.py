from thesmuggler import smuggle

# À la `import weapons`
weapons = smuggle('weapons.py')

# À la `from contraband import drugs, alcohol`
drugs, alcohol = smuggle('drugs', 'alcohol', source='contraband.py')

# À la `from contraband import drugs as dope, alcohol as booze`
dope, booze = smuggle('drugs', 'alcohol', source='contraband.py')
