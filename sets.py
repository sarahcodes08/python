# Demonstrating sets in Python

# Creating a set
fruits = {"apple", "banana", "cherry"}
print("Fruits set:", fruits)

# Adding an element
fruits.add("orange")
print("After adding orange:", fruits)

# Removing an element
fruits.remove("banana")
print("After removing banana:", fruits)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a.intersection(b)
d = a.union(b)
print("Intersection of a and b:", c)
print("Union of a and b:", d)
# Set operations: union, intersection, difference, symmetric difference
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a - b):", a - b)
print("Symmetric Difference:", a ^ b)

a.add(5)  # Adding an element to set a
print("Set a after adding 5:", a)
a.update({6, 7})  # Adding multiple elements to set a
print("Set a after updating with {6, 7}:", a)
# Removing an element safely
a.remove(2)  # to remove any element from a set
del a  # to delete the entire set a

# Checking membership
print("Is 2 in set a?", 2 in a)

# Iterating over a set
for fruit in fruits:
  print("Fruit:", fruit)