cities = [
  'Jakarta',
  'Surabaya',
  'Semarang'
]

for city in cities[:-1]:
  print(city)
else:
  print(' '.join(cities[-1].upper()))
