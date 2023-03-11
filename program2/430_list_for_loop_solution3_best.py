
'''
we know we can do this:
'''

print("for i in range(10) ---------------------------")


for i in range(10):
    print(i, end=" ")

'''
range(10) is a value, which represents number from 0 - 9
'''


# In the place of range, you can put a list value
print("\nfor f in fruits ---------------------------")

fruits = ['Apple', 'Orange', 'Banana', 'Pear']

for f in fruits:
    print(f, end=' ')


# In the place of range, you can put a str value
print("\nfor ch in str ---------------------------")

for ch in "Hello":
    print(ch, end=" ")