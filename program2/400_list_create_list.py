'''

What is data structure?
Variable is like a pointer, points to a box which holds a single value - int / float / boolean / string
Data Structure is like a cabinet which contains many boxes!

Your variable now can point to a data structure, which is a cabinet,
You can use the variable to open the cabinet, and use any value inside it.

The first data structure we learn today is called - list
'''

'''
There are 2 important notion in list:
1) index: the number you are in the list
2) value: the value at the position
'''


# Solution 1) Use square bracket
fruits = ['Apple', 'Orange', 'Banana', 'Pear']
print(fruits)

animals = ['Tiger',      # I also can put 1 element per line
           'Elephant',
           'Snake',
           'Shark']
print(animals)

cars = []  # create an empty list
print(cars)


# Solution 2) Use list constructor
students = list()
print(students)


# I can put a range inside the list constructor
numbers = list(range(10))
print(numbers)

# I can put a string inside the list constructor
char_list = list("I love Python!")
print(char_list)