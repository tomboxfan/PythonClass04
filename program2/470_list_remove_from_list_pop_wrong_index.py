animals = ['tiger', 'elephant', 'snake', 'shark']

# popped_animal = animals.pop(20)
# IndexError: pop index out of range


# So you need to check index before calling pop method
index = -100

if index < len(animals):
    popped_animal = animals.pop(index)
    print(f"{popped_animal} is popped out at index: {index}")
    print(animals)
else:
    print(f"{index} is invalid, we only have {len(animals)} animals in the list.")

'''
HOMEWORK:
Can you fix this program so that only valid negative index works?


HINT:
The issue is at line 10
because the index has a restriction on both left side and right side. 
'''