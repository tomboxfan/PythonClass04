fruits = ['Apple', 'Orange', 'Banana', 'Pear']

# Solution 1) Use append - add new value to the END of the list
fruits.append('Watermelon')

fruits.append(True)         # add boolean to the end of the list
fruits.append(1)            # add int
fruits.append(1.2)          # add float
fruits.append([1, 2, 3])    # add another list!!

print(fruits)        # ['Apple', 'Orange', 'Banana', 'Pear', 'Watermelon', True, 1, 1.2, [1, 2, 3]]

'''
This is called heterogeneous (Contains all kinds of objects)
'''


