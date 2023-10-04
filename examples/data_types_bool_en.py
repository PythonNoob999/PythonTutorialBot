# we make the 2 passwords vars
password1 = 12345
password2 = 12344

# we make a var for the main password
password = 12345

# we make a Boolean var to store the access status

access = False

# We match the first password
if password1 == password:
    access = True

print(access) 
>> True

# We match the second password

if password2 == password:
    access = False

print(access)
