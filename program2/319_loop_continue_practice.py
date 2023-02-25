'''
HOMEWORK

Print all numbers from 1 to 100
if the number is the multiple of 5, then you don't print it.
'''

for i in range(1, 101):

    if i % 5 == 0:
        continue

    print(i, end=' ')