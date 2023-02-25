# by default, print() inserts a space between the items it prints.
print(1, 2, 3)

# But, you can specify a 'separator' argument to tell Python, how to separate those items.
print(1, 2, 3, sep='-') # sep means 'separator'
print(1, 2, 3, sep=' * ')
print(1, 2, 3, sep='\n') # \n is a special character - next line character

print('-------------------------------------------')

'''
By default, print() adds an extra \n at the end of what it prints.
'''

for i in range(5):
    print(i)


print('-------------------------------------------')

'''
But, you can change this by using the end argument.
'''

for i in range(5):
    print(i, end = ' ')

