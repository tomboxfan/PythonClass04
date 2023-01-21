

'''
IMPORTANCE!!! ---------------------------------------------------------
In Python, there are 2 kinds of loop.
a) while loop   - repeat until some boolean expression is false. I don't know how many times it will repeat.
b) for loop     - repeat for a fixed number of times.            I know how many times it will repeat.

1) You are actually defining a new variable i inside the for loop.

2) function range() helps you generate a series of numbers.
   range(5) generates numbers: 0, 1, 2, 3, 4 (no 5!) - 0 based

3) so this for loop will repeat 5 times.
   Each time loop, inside the looping body, looping variable i equals to 0, 1, 2, 3, 4

'''

for i in range(5):
    print(i)

print("-" * 100)

for i in range(10):
    print('*' * i)

'''
HOMEWORK: 
How to change the above for loop, so that I can print stars from 1 to 10? (Right now, it is 0 - 9)
'''



