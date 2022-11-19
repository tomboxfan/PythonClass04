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

number_a_square_root = number_a ** (1/2) # number_a_square_root is a float
print(f"{number_a}'s square root is {number_a_square_root:.2f}")





number_a_square_root_int = int(number_a_square_root)
print(f"{number_a}'s square root to int is {number_a_square_root_int}")


if number_a_square_root == number_a_square_root_int:
    print(f"Because {number_a_square_root:.2f} == {number_a_square_root_int}, so {number_a} is a square number.")
else:
    print(f"Because {number_a_square_root:.2f} != {number_a_square_root_int}, so {number_a} is NOT a square number.")


