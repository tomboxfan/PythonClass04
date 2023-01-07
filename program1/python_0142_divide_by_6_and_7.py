'''
Requirement:
Use while loop, print out all numbers below 1000, if it can be divided by both 6 and 7
'''

a = 1
count = 0

while a <= 1000:

    if a % 6 == 0 and a % 7 == 0:
        print(a)
        count += 1

    a += 1

print(f"There are in total {count} numbers.")