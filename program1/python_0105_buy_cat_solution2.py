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

# Or a female cat, not white
# gender == 'female' and color != 'white'

# Or just a black cat

# USE VARIABLES -----------------------------------------------------

if gender == 'male' and (color == 'white' or color == 'yellow') or gender == 'female' and not color == 'white' or color == 'black':
    print("I will take it!")
else:
    print("I don't take it.")


'''
ctrl + x -> cut
ctrl + c -> copy
ctrl + v -> paste
'''