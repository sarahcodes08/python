#Dictionary datatype
#unordered sets of key value pair
dict_a = {
  'key1':'value1',
  'key2':'value2',
  'key3':'value3'
}
print(dict_a)
print(dict_a['key1'])
print(dict_a.get('key5'))

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': [1964, 1965, 1966],
  'color': ('red', 'blue', 'green'),
  'docs': {'original':'yes', 'duplicate':'no'}
}
print(car['brand'])
print(car['model'])
print(car['year'])
print(car['year'][0])
print(car['color'])
print(car['color'][1])
print(car['docs'])
print(car['docs']['original'])