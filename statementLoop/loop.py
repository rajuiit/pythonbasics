#General for loop
city = ['Tokyo','New York','Dhaka','Brisbane']
for i in city:
    print(f"city: {i} \n")

numbers = [1,2,4,5,6,7,8,9]
for i, num in enumerate(numbers):
    print(f"Numbers {i}:  {num}\n")

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
