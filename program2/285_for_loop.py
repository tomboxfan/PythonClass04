

print("range(5, 10) generates number from 5 to 9, no 10! - [5, 10)")
for i in range(5, 10):
    print(i)

print('--------------------------')

print("range(5, 6) generates 1 number only - 5, it only loops once. [5, 6)")
for i in range(5, 6):
    print(i)

print('--------------------------')

print("range(5, 5) generates no number. So this prints nothing, no loop at all! [5, 5)")
for i in range(5, 5):
    print(i)

'''
IMPORTANCE!!! 
range(start, stop) generates number in range [start, stop), start is inclusive, stop is exclusive.
'''