'''
Homework:

Requirement:

Input a student's score.
if it is equals to 90 or above, your program prints 'A'
if it is equals to 60 or above, your program prints 'B'
other score, print 'C'
'''

# DEFINE A VARIABLE -------------------------

score = int(input("Your score:"))

# USE A VARIABLE ----------------------------
if score >= 90:
    print("A")
elif score >= 80:
    print('B1')
elif score >= 70:
    print('B2')
elif score >= 60:
    print('B3')
else:
    print('C')



