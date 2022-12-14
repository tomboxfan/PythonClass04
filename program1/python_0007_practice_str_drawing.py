'''

Requirement: I want to print a square with length = 5

'''

# Example 1)
# Let's print a small square 2 * 2
star_line = '*' * 2
print(star_line)
print(star_line)

print("--------------------------------------------")

star_line = '*' * 5
print(star_line)
print(star_line)
print(star_line)
print(star_line)
print(star_line)

'''
There is a special key in PyCharm -> double click 'shift' key, then a window will pop up.
Then you type 'Console Font', then the console font setting window will appear.
Please follow the 2 images.
'''


print("--------------------------------------------")

'''
Now I want to move the square to the middle, in stead of the far left. 
How can I do this? -- HOMEWORK
'''

star_line = ' ' * 5 + '*' * 5

'''
these 2 lines are exactly the same:
star_line = ' ' * 5 
star_line = '     '
'''

print(star_line)
print(star_line)
print(star_line)
print(star_line)
print(star_line)


print("--------------------------------------------")

left_star_right_star =  ' ' * 5 + '*' + ' ' * 3 + '*'

print(star_line)
print(left_star_right_star)
print(left_star_right_star)
print(left_star_right_star)
print(star_line)