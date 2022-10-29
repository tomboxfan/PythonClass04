# Example 1

# Step 1) Define a variable
# Let's assume Tom is 20 years old now.
toms_age = 20


# Step 2) Use variable toms_age
'''
==     tells you whether the number on the left and right are equal or not, and gives you a boolean value.
=      assigns value on the right to the variable on the left 
       toms_age == 20 is a boolean expression, and its value equals to True 
'''

print("Is Tom 20 years' old? ", toms_age == 20)

print("Is Tom 13 years' old? ", toms_age == 13)

print("Tom is not 20 years old. Am I right? ", toms_age != 20)


print("-~" * 50)


'''
Another example
'''

a = (toms_age == 20)
b = (toms_age == 13)
c = (toms_age != 20)
d = (toms_age != 13)
e = (toms_age < 30)
f = (toms_age < 20)
g = (toms_age > 30)
h = (toms_age >= 20)
print(a, b, c, d, e, f, g, h)



'''
example 3)
'''

my_math_mark = 75
my_math_is_excellent = (my_math_mark > 90)
print("Is my math excellent? ", my_math_is_excellent) # TELL ME THE OUTPUT

failed_in_math = (my_math_mark < 60)
print("Have I failed in Math? ", failed_in_math)  # TELL ME THE OUTPUT

billy_math_mark = 75
biily_has_same_score_as_mine = False # Replace False with a correct boolean expression
print("Does Billy has same score as mine? ", biily_has_same_score_as_mine)

our_total_marks_greater_than_150 = False # Replace False with a correct boolean expression
print("Is our total score greater than 150? ", our_total_marks_greater_than_150)


'''
You must remember the meaning of:
> 
< 
>=
<=
==
!=
'''