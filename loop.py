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

# an example of nested loop 
for i in range(0,10):
  print('------------------')
  for j in range(0,10):
    print(f'{j} * {i} = {j*i}')

# Table of 0-10 numbers
    
