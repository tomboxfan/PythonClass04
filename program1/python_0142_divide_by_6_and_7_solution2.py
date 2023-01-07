'''
Requirement:
Use while loop, print out all numbers below 1000, if it can be divided by both 6 and 7
'''

a = 42
count = 0

while a <= 1000:

    print(a)
    count += 1

    a += 42

print(f"There are in total {count} numbers.")