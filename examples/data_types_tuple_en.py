# Creating a tuple with fruits
fruits = ("Apple", "Kiwi", "Banana")

# we can also print it's values with indexing

print(fruits[0])
#>> Apple

# and also use negative indexing
print(fruits[-1]) 
#>> Banana

# but unlike lists[], you can't change it's data

fruits[0] = "Orange"
#>> TypeError: "str" object does not support item assignment❗️
