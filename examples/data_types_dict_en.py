# We make a price dictionary
fruits = {
"Apple": 3,
"Kiwi": 9,
"Banana": 4
}

# We can print fruit price by using it's name aka "key" as index

print(fruits["Kiwi"], "$")
#>> 9$

# We can also change a fruit price
fruits["Banana"] = 2
print(fruits["Banana"], "$")
#>> 2$

# And of course that well change the dictionary totally
print(fruits)
#>> {
#    "Apple": 3,
#    "Kiwi": 9,
#    "Banana": 2
#}
