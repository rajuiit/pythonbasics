#General for loop
city = ['Tokyo','New York','Dhaka','Brisbane']
for i in city:
    print(f"city: {i} \n")


#General for loop
city = ['Tokyo','New York','Dhaka','Brisbane']
for i, city in enumerate(city):
    print(f"city: {i}: {city} \n")


city = ['Tokyo', 'New York', 'Dhaka', 'Brisbane']
for i, c in enumerate(city):
    if c == 'Dhaka':
        print(f"city: {i}: {c}")

city = ['Tokyo', 'New York', 'Dhaka', 'Brisbane']
search_city = 'Dhaka'

for i, c in enumerate(city):
    if c == search_city:
        print(f"The index of '{search_city}' is: {i}")
        break  # Stop the loop once the city is found



numbers = [1,2,4,5,6,7,8,9]
for i, num in enumerate(numbers):
    print(f"Numbers {i}:  {num}\n")

numbers = [1,2,4,5,6,7,8,9]
for i in numbers:
    print(f"Numbers {i}\n")

#Nested for loop

lists = [[1,2,3], [4,5,6], [5,7,8], [9,8,7]]

for outer_i in lists:
    for inner_j in outer_i:
        print(f"Show inner elements: {inner_j}")

#If you want to access the outer index in the nested loop, you can use the enumerate() function. 
#This function adds a counter to an iterable and returns it. The counter increments each time the function is called.

for outer_index, outer_list in enumerate(lists):
    print("Outer list index:", outer_index)
    for inner_element in outer_list:
        print(inner_element)


#While loop
        
x = 5
while x < 10:
    print(f"The while loop value:", x)
    x = x+1

# while True:
#     print("Forever")
    
number = 100
for i in range(number):
    print(i)

numberslist = [1,2,3,5,6,7,8,9]
for i in range(len(numberslist)):
    print(f"Index {i}: {numberslist[i]}")
