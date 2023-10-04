# we make name and number variables

name = "Jack"
number = 4

# we make a variable to store the amount of time we printed the name

printed = 0

# we will make a while loop that will check if the printed time's is less than the number we want to print, if it's condition is True, the loop will print the name and increase the printed variable by 1

while printed < number:
    print("Your name is: ", name)
    printed = printed + 1

# we will print that the program finished outside the while loop, so this command will execute when the while loop is finished

print("Done")

# OUTPUT:
#>> Your name is Jack
#>> Your name is Jack
#>> Your name is Jack
#>> Your name is Jack
#>> Done
