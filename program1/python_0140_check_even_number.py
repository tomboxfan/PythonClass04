'''
Requirement: Print all numbers smaller than 7, odd or even.
'''

a = 1

while a < 7: # a appears inside the boolean expression after 'while', a is called 'looping variable'

    # step 1) check whether a is even or odd
    if a % 2 == 0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")

    # Step 2) update the looping variable
    a += 1


print("All Done! ")