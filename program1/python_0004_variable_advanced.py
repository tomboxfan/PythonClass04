
# define a variable with value = 5
h = 5
print("Now h value is:", h)

'''
Duplicate the current line:
Move your cursor to the line, then you press: Ctrl + D

Move a line:
Alt + Shift + Down
'''

'''
IMPORTANCE!!! -------------------------------------
FOREVER REMEMBER:
when variable appears on the right side of '='    :  use the variable's value
when variable appears on the left side of '='     :  we put a new value into the box which the variable points to, assign value from the right to the variable

explanation --------------------
on the right side of '='     :    h - 1
                                  use variable h's value - 5
                                  5 - 1 = 4
                                  
on the left side of '='      :    h
                                  assign value from right to left (h), to the variable h
                                  now h becomes 4

in summary -----------------------------------------------
assign a new value to h, using an expression which uses h's old value.
h's old value is 5, expression h - 1 = 4, assign 4 to variable h, now variable h equals to 4.
'''

h = h - 1
print("Now h value is:", h) # h is 4

h -= 1 # this equals to 'h = h - 1'
print("Now h value is:", h) # h is 3

h += 1 # this equals to: h = h + 1
print("Now h value is:", h) # h is 4

h *= 2 # this equals to: h = h * 2
print("Now h value is:", h) # h is 8

h /= 4 # this equals to: h = h / 4
print("Now h value is:", h) # h is 2

'''
5, 4, 3, 4, 8 are called integer
2.0           is called float (小数) 
'''



