

'''
This program will run forever, never exit.

because after keyword 'while', it is not a boolean expression, it is a boolean value : True.
There isn't any variable here, inside the looping body, we are not able to update the looping variable or looping condition
So the loop runs forever.

we call it dead loop - as soon as Python falls into this loop, Python is dead, Looping forever, never come out!

'''

while True:
    print("I love Python!")



# another example -------------------------------------

sheep_count = 0

while True:
    print(f"{sheep_count} sheep, I feel sleepy...")
    sheep_count += 1


