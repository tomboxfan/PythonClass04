'''
Requirement:
1) Ask user to input a number from console
2) Then you need to tell whether the number is a square number or not
'''

# get user input ---------------------------------

# Solution 1)
str = input("Please input a number: ")
number_a = int(str)

# Solution 2)
# number_a = int(input("Please input a number: "))

# print(number_a)

number_a_square_root = number_a ** (1/2)
print(f"{number_a}'s square root is {number_a_square_root}")


# For now, the program tells us the square root of number_a