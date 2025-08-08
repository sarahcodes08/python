#Section: 5
#list data type
var_list= ['Sarah', 18]
#has ordered sequence(indexing)
l_one = [1,2,3,4]
l_two = [1,2,["three"],4]
l_three = list((1,2,3,4))
print(l_one[3])
print(l_one[0:3]) #(3rd element included) you can do slicing as well 
#functions on lists
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
d = ['a', 'b', 'c']
a.extend(b)
print(a)
a.append(7)
print(a)
a.pop()
print(a)
a.remove(2)
print(a) 
print(a.count(1))
a.sort(reverse=True)
d.sort(reverse=True)
a.reverse()
print(min(a))
print(max(a))
print(a)
print(d)

e = ['a', 'b', 'c', 1,2,3]
e[0] = 'z'
print(e)
# Mutable example: List
a = ['a', 'b', 'c', 0, 1, 2, 3, 3]
print(a)

a[0] = 'b'  # Modifying list element
print(a)

# Immutable example: Tuple
tuple_c = (2, 6, 9, 'A')
tuple_d = (4, 9, 2, 'B')
tuple_f = (8, 0, 1, 'C')

print(tuple_c)

# Creating a new tuple based on existing values
tuple_c = (tuple_c[0], tuple_c[2], 'S', tuple_f[2])
print(tuple_c)

# Unpacking tuple into variables
ele_a, ele_b, ele_c, ele_d = tuple_c

print(ele_a)
print(ele_b)
print(ele_c)
print(ele_d)

# Creating automatic lists using range

my_list = list(range(1, 10))
odd = list(range(1, 10, 2))
even = list(range(0, 11, 2))

print(my_list)
print(odd)
print(even)

print(list(range(1, 1000)))

even = list(range(0, 1000, 2))
odd = list(range(1, 1000, 2))

print(even)
print(odd)

print(even[334])
print(odd[420])

print(odd.index(841))

print(list(range(1, 10)))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)

list_seven = list(range(17, 100000, 17))
