# we make variables that contain multiple data types to calculate there length using the len() function

list = [3, 4, 8, "Ahmed", True]
tuple = (3, 4, 8, "Ahmed", True)
string = "Hello World!"

# now we calculate each variable length and print it

print("the list has ", len(list), " items")

print("the tuple has ", len(tuple), " items")

print("the string has ", len(string), " letters")
# OUTPUT
# the list and tuple contains 5 items, 3 int, 1 string, 1 boolean, so the total length is 5

#>> the list has 5 items
#>> the tuple has 5 items
# in the string case the len() function calculate the string, letter by letter
#>> the string has 12 letters
# now you might think why the string has 12 "letter", when it contains only of 11 letters. well, the len() function also count empty spaces in a string
