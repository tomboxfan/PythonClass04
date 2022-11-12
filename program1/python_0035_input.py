

'''
function input(): accept user input from console, as some variable's value
So we don't know your_name's value until program runs to below line.
'''

your_name = input("Your name: ")

print(f"Hello, {your_name}!")

'''
IMPORTANCE!!! ----------------------------------
As soon as the program runs to the line input(), program halts.
The control goes back to you - the user.

It waits until user types his name and "ENTER" in the console. 
Then the control goes back to the program immediately and program proceeds. 

input() also works! 
But 
input("Your name:") is much better! 
It supplies an extra prompt message to the user, telling him, what information he needs to supply.
'''

print(f"Variable your_name's type is: {type(your_name)}")


your_age = input("Your age: ")
print(f"Your age is: {your_age}")
print(f"Variable your_age's type is: {type(your_age)}")

'''
input() function ALWAYS gives you a str value.
'''
