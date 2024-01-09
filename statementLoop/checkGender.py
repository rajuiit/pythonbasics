gender = input('Enter your gender: ')
gender = gender.lower()

if gender == "male":
    print("Your cat is male")
elif gender == "female":
    print("Your cat is female")
else:
    print("Not in categorised")    

number = int(input('Enter your number: '))

if number <= 5:
    print("Your cat is child")
elif number > 5 and number < 10:
    print("Your cat is young")
else:
    print("Your cat is adult")
