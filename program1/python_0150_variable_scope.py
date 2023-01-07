a = 10

if a < 20:
    my_name = 'Mr Fan'
    print(f"{my_name} teaches Python to young kids")


print(f"Who is {my_name}? ")

'''
The above code breaks when we change a's value to 30
because variable my_name will not be defined when a >= 20

so line 8 goes wrong!

How to solve it? Move my_name definition out of if blocks
'''