# Requirement: A customer walks into a Pet's store, he said, 'I want a
# male cat, white or yellow
# Or a female cat, not white
# Or just a black cat

# You need to get input from console about cat gender and cat color
# You program needs to tell whether the customer wants it or not


# DEFINE VARIABLES -----------------------------------------------------

gender = input('Is the cat male or female? ')
color = input("What's the color of the cat? ")

# male cat, white or yellow
sit1 = (gender == 'male' and (color == 'white' or color == 'yellow'))

# Or a female cat, not white
# gender == 'female' and color != 'white'
sit2 = (gender == 'female' and not color == 'white')

# Or just a black cat
sit3 = (color == 'black')

# USE VARIABLES -----------------------------------------------------

if sit1 or sit2 or sit3:
    print("I will take it!")
else:
    print("I don't take it.")
