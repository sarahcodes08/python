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
lName = " Shahzad"
print(fName+lName) #operator overloading
print(fName*3) #string multiplication