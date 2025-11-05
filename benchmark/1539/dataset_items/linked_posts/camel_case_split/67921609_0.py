import re

re.split('(?<=[a-z])(?=[A-Z])', 'camelCamelCAMEL')
# ['camel', 'Camel', 'CAMEL'] <-- result

# '(?<=[a-z])'         --> means preceding lowercase char (group A)
# '(?=[A-Z])'          --> means following UPPERCASE char (group B)
# '(group A)(group B)' --> 'aA' or 'aB' or 'bA' and so on
