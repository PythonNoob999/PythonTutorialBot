# first we take the user age
age = int(input("Type your age: "))

# now we will make a lambda function that takes a number as a param, and return the number + 5
myfunc = lambda number: number+5

# Now we will print the new user age
print("You will be ", myfunc(age), " Years old in 5 years")

# OUTPUT:
#>> Type your age: 
# we will type 16 as our age
#>> You will be 21 Years old in 5 years
