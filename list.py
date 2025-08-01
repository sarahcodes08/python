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
a.append(7)
a.pop()
a.remove(2) 
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
#yall i need to speed up this