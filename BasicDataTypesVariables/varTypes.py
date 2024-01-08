from ctypes import cast

x = 4 # a whole number 
f = 3.1416 # a floating point number
name = "Python" # a string
combination = name + " " + name

#f-string or interpolation
print(f"The combination is: {combination}")

sum = x+int(f)

#f-string or interpolation
print(f"The summation is: {sum}")

#Naming Convension: Camel Casing

daysInYear = 365
daysInMonth = 30
daysInHour = 24

print(f"Year: {daysInYear}\n Month: {daysInMonth} \n Hour: {daysInHour}")


#String Defining

x = "Hello World"
print(f"My first string output: {x}")

#String indexing

print(f"First letter: {x[0]} \n Second letter: {x[1]}")

#SubString

print(f"Substring: {x[0:4]}")
#If no start or end number is written, Python assumes you mean the first character or last character.
s = x[:4]
print(s)

#Replace
x = x.replace("World","Universe")
print(x)

#All World will be replaced
y = "Hello World World World"
# y = y.replace("World","Universe")
# print(y)

#First World will be replaced
y = y.replace("World","Universe",1)
print(y)

#To find a specific character in a string in Python, you can use the find() method.

text = "Hello World"
char = "l"
index = text.find(char)

if index != -1:
    print(f"The character {char} was found in index {index}.")
else:
    print(f"The character {char} was not found in the text")

#Print all index if character found
# text = "Hello, world!"
# char = "l"

# start = 0
# while True:
#     index = text.find(char, start)
#     if index == -1:
#         break
#     print(index)
#     start = index + 1

#using enumerate
text = "Hello World"
char = "l"
for i, letter in enumerate(text):
    if letter == char:
        print(i)

#simple range and len
    
# text = "Hello World"
# char = "l"
# for index in range(len(text)):
#     if text[index] == char:
#         print(index)    


#If we want to split a word into characters, use the list() method instead:
word = "Easy World"
x = list(word)

for i in range(len(x)):
    print(f"The characters are {i}: {x[i]} \n")

#Splits a string into words.
s = "Its to easy"
words = s.split()
print(words)
for i in range(len(words)):
    print(f"The words are: {words[i]}")
