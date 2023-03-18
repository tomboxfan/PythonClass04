animals = ['tiger', 'elephant', 'snake', 'shark']

insects = ['caterpillar', 'ant', 'butterfly']

# extend - join another list
animals.extend(insects)
print(animals)

'''
['tiger', 'elephant', 'snake', 'shark', 'caterpillar', 'ant', 'butterfly']
'''



# HOMEWORK
animals.append(insects)
print(animals)
'''
Please don't run this code:
You write out the content of list animals

ANSWER:
['tiger', 'elephant', 'snake', 'shark', ['caterpillar', 'ant', 'butterfly']]

'''