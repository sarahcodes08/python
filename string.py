#Section: 4
#String data type
word = "Sarah"
sentence = 'She said, "Hello" '
print(word)
print(sentence)

#indexing
#left to right(0 to onwards)
#right to left(-1 to backwards)
print(word[0])
print(word[-5])
#to print series
print(word[0:5])
print(word[0::]) #double-colon means go till the end of string
print(word[0:5:2]) #[start:end:step-size]
#concatenation
fName = "Sarah"
lName = "Shahzad"
print(fName+lName) #operator overloading
print(fName+' '+lName) #with space
print(fName*3) #string multiplication
#string formatting
name = input('Enter your name: ')
age = int(input('Enter your age: '))

msg1= f'Merhaba\' {name}, you are {age+1} years young' #easier method using backslash for using apostrophe
msg2 = 'Merhaba {0}, you are {1} years young'.format(name, age) #older method, no need for indexing though
print(msg1)
#escape sequences:
#1. \t : for space
#2. \n : for new line and multiple others
#3. """ """ : for big paragraph and multi line as well
#
#built-in functions
print(msg1.lower())
print(msg1.upper())
print(msg1.strip())
print(msg1.split())
print(msg1.find('are'))
print(msg1.replace('are', 'r'))
print(msg1.startswith('M'))
print(msg1.endswith('a'))