'''
Requirement:

print 2 to the power of 1 to 10 in a while loop
meaning,
print 2, 4, 8, 16 ... 1024 in a while loop

further...

print 2 to the power of 1 to 10 mod 5 in a while loop
meaning,
print 2, 4, 3, 1 ... 4 in a while loop


'''


a = 1

while a < 11:

    print(2 ** a, 2 ** a % 5)

    a += 1