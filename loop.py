#iterator and iterable
a = [1,2,3,4,5,6,7,8,9]
#that data type is iterable
#and the function iter() will return an iterator

var_a = iter(a)
print(var_a)
print(next(var_a)) # Get the first element
print(next(var_a)) # Get the second element
print(next(var_a)) # Get the third element
print(next(var_a)) # Get the fourth element
t = next(var_a) + 2.5
print(t)
#instead of next() we can use a for loop
for var_a in a: #iter function var_a will be called for a
    print(var_a)

# Uses of for loop

# Uses of for loop in python

# 1. It is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
# 2. It is used to iterate over a range of numbers.
# 3. It is used to iterate over the elements of a file.
# 4. It is used to iterate over the keys and values of a dictionary.
# 5. It is used to iterate over the characters of a string.

# Benefits of using for loop:
# 1. It is more readable and easier to understand than a while loop.
# 2. It is less error-prone than a while loop.
# 3. It is more efficient than a while loop.
# 4. It is more flexible than a while loop.
# 5. It is more powerful than a while loop.



# Table of 0-10 

# an example of nested loop 

for i in range(0,10):
  print('------------------')
  for j in range(0,10):
    print(f'{j} * {i} = {j*i}')


# Sum of numbers using for loop
numbers = [1,3,5,7,9,11,13,15,17,19]
sum = 0
for i in numbers:
  sum = sum + i
print(f'Sum of numbers: {sum}')

# For loop examples
for i in range(0,10):
  if i % 2 == 0:
    print(f'{i} is even')
  else:
    print(f'{i} is odd')
  
  
# Nested for loop example 
colors = ['red', 'green', 'blue', 'yellow']
fruits = ['apple', 'banana', 'cherry', 'date']
for color in colors:
    for fruit in fruits:
        print(f'{color} {fruit}')

# Using zip to iterate over two lists simultaneously  
for x,y in zip(colors, fruits):
    print(f'{x} {y}')
    
# to pass a for loop without executing any code
for i in range(5):
    pass  # This will do nothing, just a placeholder
  
# Using else with for loop
for i in range(1, 11):
  print(i)
else:
  print("Loop completed successfully.")
    
# Using dictionary with for loop
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(f'{key}: {value}')
    
# Another way to iterate over a dictionary
student = {'name': 'Bob', 'age': 22, 'major': 'Computer Science'}
l = list(student.keys())

reversed_key = sorted(l, reverse=True)
print(reversed_key)

for key in reversed_key:
    value = student[key]
    print(value)
    
for value in student.values():
    print(value)
    
for key in student.keys():
    print(key)
    
for key in student:
    print(student[key])
    
    
# Using a tuple with for loop
my_tuple = (10, 20, 30, 40)
for item in my_tuple:
    print(item)
    
T = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in T:
    print(f'a: {a}, b: {b}, c: {c}')

x = tuple(list(range(1, 10)))
print(x)

for i in x:
    print(i)
    
smoothie = ('banana', 'strawberry', 'blueberry', 'yogurt')

for index, item in enumerate(smoothie):
    print(f'Index {index}: {item}')
    
    
# Quiz

fruits = ['apple', 'banana', 'cherry'] 
for fruit in fruits: 
    print(fruit)
    
    
for i in range(3):
  for j in range(2):
    print(i, j)
    
    
points = [(1, 2), (3, 4), (5, 6)] 
for x, y in points: 
      print(x, y)
      
numbers = [1, 2, 3, 4, 5] 
sum = 0 
for num in numbers: 
  sum += num 
  print(sum)
  
  
for i in range(2): 
  for j in range(2): 
    print(i + j)

# Table of 0-10 numbers


    

