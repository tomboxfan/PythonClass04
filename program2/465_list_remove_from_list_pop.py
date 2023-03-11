animals = ['tiger', 'elephant', 'snake', 'shark']
print(animals)


popped_animal = animals.pop()
print(popped_animal, 'is popped out.')
print(animals)

popped_animal = animals.pop(1)
print(popped_animal, 'at index 1 is popped out.')
print(animals)


'''
pop(i) - remove item by index i
pop()  - remove last item
It returns the popped item.
'''