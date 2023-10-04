# we make a function that takes the first angle and the second angle

def third_angle(Angle1, Angle2):
# we make a variable that has the sum of the 2 Angles

    Angles = Angle1+Angle2

# we calculate the third angle by substracting 180 from Angle1+Angle2

    Angle3 = 180-Angles

# we return the third_angle
    return Angle3

# we try using the function with angles 1 and 2
a = 70
b = 60
c = third_angle(a, b)

# we print the third angle
print(c, " Degrees")
#>> 50 Degrees
