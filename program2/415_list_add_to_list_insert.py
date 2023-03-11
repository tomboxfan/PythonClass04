animals = ['Tiger', 'Elephant', 'Snake', 'Shark']


'''
Solution 2: User insert - add new value to the list at index specified.
You need to tell function insert 2 things:
1) where
2) what
'''
animals.insert(1, 'Leopard')
print(animals)  # ['Tiger', 'Leopard', 'Elephant', 'Snake', 'Shark']

animals.insert(100, "Giraffe") # When index > length of the list, it appends the value to the end of the list
print(animals)  # ['Tiger', 'Leopard', 'Elephant', 'Snake', 'Shark', 'Giraffe']

# HOMEWORK, Please help insert Hedgehog at the place 2nd from the last

animals.insert(-1, "hedgehog")
print(animals)