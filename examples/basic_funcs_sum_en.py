# we make a empty list
numbers = []

# we make a while loop and take the user input
while True:
    number = input("Type a number ")
# now we make a if statment to check if the user input in the variable "number" does not equal to "exit", then it will add it to the number list

    if number != "exit":
        numbers.append(int(number))
# otherwise, we will break out of the loop

    else:
        break

# finally when the loop ends, we print the numbers list and its sum
print(numbers)
print(sum(numbers))

# OUTPUT
#>> Type a number
# we will type 5
#>> Type a number
# we will type 8
#>> Type a number
# we will type 12
#>> Type a number
# this time we will type exit to finish
# now it will print the list of numbers and sum
#>> [5, 8, 12]
#>> 25
