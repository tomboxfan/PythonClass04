animals = ['tiger', 'elephant', 'snake', 'shark']
animals = animals * 2
print(animals)


# animal = 'tiger'
animal = 'fish'

if animal in animals:
    animals.remove(animal)
    print(animals)
else:
    print(f"{animal} is not found in list {animals}")

'''
1) the 'in' operator tells you whether a value exist in a list or not
2) remove(value) helps remove value from the list, you need to check whether the value exists in the list or not.
'''
