'''
HOMEWORK VERSION 2 - SUPER CHALLENGING

Print all numbers from 1 to 100
if the number is the multiple of 5, then you don't print it.
if the number is the multiple of 7, then you don't print it.
if the number is the multiple of both 5 & 7, then you print it, but you need to print "WARNING!" after the number.
Stop your program immediately, when you've printed 2 'WARNING'.

...
34
35 1 WARNING!
36
37
...
68
69
70 2 WARNING!
'''

warning_count = 0


for i in range(1, 101):

    '''
    You put more strict conditions in the front, less strict conditions at the back
    '''
    if i % 5 == 0 and i % 7 == 0:

        warning_count += 1
        print(f"{i} WARNING {warning_count}!")

        if warning_count == 2:
            break


    if i % 5 == 0:
        continue

    if i % 7 == 0:
        continue



    print(i)