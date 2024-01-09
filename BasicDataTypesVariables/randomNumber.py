import random

#Create a random floating point number and print it.
x = random.random()
print(x)

# pick a random whole number between 0 and 10.
print(random.randrange(0,10))

# pick a random floating point number between 0 and 10.
print(random.uniform(0,10))

#To generate integer value

print(random.randint(1,10))

#For generating a random number from a list of numbers, you can use the choice() function.

numbers = [1,2,5,4,6,7,9,8]
randomValue = random.choice(numbers)
print(randomValue)

#We can use the seed() function to set the seed for the random number generator. 
#If we provide the same seed value each time we run your program, it will generate the same sequence of random numbers.
random.seed(1)
print(random.randint(1,10))
