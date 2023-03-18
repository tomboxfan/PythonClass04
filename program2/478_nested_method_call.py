animals = ['tiger', 'elephant', 'snake', 'shark']

'''
popped_animal = animals.pop(0)
print(popped_animal) # tiger
print(animals)       # ['elephant', 'snake', 'shark']

animals.append(popped_animal)
print(animals)       # ['elephant', 'snake', 'shark', 'tiger']
'''


# Line 4 & line 8 can be merged together to below:
animals.append(animals.pop(0))


'''
1) Python runs code from top line to bottom line
2) In the same line, python runs from left to right.
Here Python notices, it needs to append something to the end of the animals list
Then Python tries figuring out what it should append, it notices it is another function call.
So the append function call pauses first.
Python will first call animals.pop(0), 'tiger' is popped out, returned as the value to be appended.
Then the append function resumes.
'''
