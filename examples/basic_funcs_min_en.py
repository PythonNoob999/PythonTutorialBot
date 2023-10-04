# we take the user input
number = int(input("Type a number: "))

# we put the number in a list
numbers = [62, 12, 94, 7, number]

# now we check if the smallest number in the list (numbers) is equal to the user number

if min(numbers) == number:
    print("You Won! ")

# other wise we will print that he lost
else:
    print("You lost! ")
