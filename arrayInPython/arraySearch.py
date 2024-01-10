#search for an element within an array (list in Python), you have various methods available:

#Using the in Operator:
array = [2, 4, 5, 6, 7]
elementToFind = 5

if elementToFind in array:
    print(f"{elementToFind} is present in the array.")
else:
    print(f"{elementToFind} is not present in the array")

#Using index() method:
    
array = [3, 7, 11, 5, 9]
element_to_find = 11

try:
    index = array.index(element_to_find)
    print(f"{element_to_find} found at index {index}.")
except ValueError:
    print(f"{element_to_find} is not found")

#Using for loop
    
array = [3,4,5,6,7,8,2,3]
element_to_find = 3
for index, element in enumerate(array):
    if element == element_to_find:
        print(f"{element_to_find} found at index {index}")

#using function
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]
element_to_find = 3
def search_element(array, element_to_find):
    found = False
    for index, element in enumerate(array):
        if element == element_to_find:
            found = True
            print(f"{element_to_find} found at index {index}")
    if not found:
        print(f"{element_to_find} is not present in the array")        
# Call the function to search for element 3 in the array
search_element(array, 3)