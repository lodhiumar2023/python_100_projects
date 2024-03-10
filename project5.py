# SWAPING THE VALUE OF VARIABLES
# FIRST METHOD USING THIRD VARIABLE

x = 25
y = 50
temp_var = y

y = x
x = temp_var

print(x, y)


# SECOND METHOD
x = 25
y = 50

x, y = y, x

print(y)
