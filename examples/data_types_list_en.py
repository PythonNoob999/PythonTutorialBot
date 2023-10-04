fruits = ["Apple", "Kiwi", "Banana"]
# indexing starts at 0 in most programming languages

print(fruits[0])
#>> Apple

# you can also use negative indexes, wich will give you opposite result

print(fruits[-1]) # last item
#>> Banana

print(fruits[-2]) # the item before the last one

#>> Kiwi
fruits[0] = "Orange" # we can even change it's values
print(fruits)
#>> ["Orange", "Kiwi", "Banana"]
