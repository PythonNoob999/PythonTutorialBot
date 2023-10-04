# we take a user input and turn it to int

age = int(input("Type your age: "))

# we wil check if the user age is bigger than 18, then we will print to the user that he can use the service

if age > 18:
    print("You can use our service!")

# now we make an elif statement, it will check if the condition above it is not correct, then it will check that the user age is 18 then it will print to the user that he can't use our service and to try again next year

elif age == 18:
    print("You cant use our service yet!, try again next year")

# finally we make an else statment, and it will check if the none of the above conditions are True, it will print to the user that he can't use our service

else:
    print("You cant use our service!")

# OUTPUT
#>> Type your age: 
# first time we will write 19
#>> You can use our service!

# the second time we will write 18
#>> You cant use our service yet!, try again next year

# the last time we will write 17
#>> You cant use our service!
