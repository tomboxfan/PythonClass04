
'''
Requirement:
Ask user to input 3 numbers from console, sort the 3 numbers in ascending order.
'''

x = int(input("Please input x: "))
y = int(input("Please input y: "))
z = int(input("Please input z: "))



# x is the smallest
if x <= y and x <= z:

    if y <= z:
        print(x, y, z)
    else:
        print(x, z, y)


# y is the smallest
elif y <= x and y <= z:

    if z <= x:
        print(y, z, x)
    else:
        print(y, x, z)


# z is the smallest
elif z <= x and z <= y:

    if x <= y:
        print(z, x, y)
    else:
        print(z, y, x)
