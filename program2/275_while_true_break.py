
a = 0

print("While loop starts: ")

while True:
    a += 1
    print(a)

    # IMPORTANCE!!!
    if a == 10:
        break

print("While loop ends.")

'''
IMPORTANCE!!! -----------------------------------------
'break' will terminate the loop immediately! 
'break' is very useful in dead loop.
'break' will make your loop stop immediately and move on the the next line of code.

Now, we finally meet the famous guy: while True / break
'''

'''
Homework:
Please refactor(重构/修改) code 270, so that the program stops when we've counted 100 sheep.
'''