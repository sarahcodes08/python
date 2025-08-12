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

a, b, c, d, e = car.items()
print(a)  # ('brand', 'Ford')
print(b)  # ('model', 'Mustang')
print(c)  # ('year', [1964, 1965, 1966])
print(d)  # ('color', ('red', 'blue', 'green'))
print(e)  # ('docs', {'original': 'yes', 'duplicate': 'no'})

f, g, h, i, j = car.keys()
print(f)  # 'brand' 
print(g)  # 'model'
print(h)  # 'year'
print(i)  # 'color'
print(j)  # 'docs'

f, g, h, i, j = car.values()
print(f)  # 'Ford'
print(g)  # 'Mustang'
print(h)  # [1964, 1965, 1966]
print(i)  # ('red', 'blue', 'green')
print(j)  # {'original': 'yes', 'duplicate': 'no'}
#built-in functions
print(car.items())  # All Items of the dictionary displayed
print(car.keys())   # All Keys of the dictionary displayed
print(car.values()) # All Values of the dictionary displayed

new_car = dict([('brand', 'Ford'), ('model', 'Mustang'), ('year', [1964, 1965, 1966]), ('color', ('red', 'blue', 'green')), ('docs', {'original': 'yes', 'duplicate': 'no'})])
print(new_car)
new_car.pop('color')  # Removes the 'color' key-value pair
print(new_car)
new_car.popitem()  # Removes the last inserted key-value pair
print(new_car)
del new_car['brand']  # Deletes the 'docs' key-value pair
print(new_car)