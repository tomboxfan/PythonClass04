'''




巴比伦算法

it helps you calculate the square root of number x. (For example, we let x be 100)

step 1) define variable a = 1                       a = 1
step 2) define variable b = x / a                   b = 100  -> distance = 100 - 1 = 99

step 3) assign variable a = (a + b) /2              a = 50
step 4) assign variable b = x / 100                 b = 100 / 50 = 2   -> distance = 50 - 2 = 48

repeat step 3 & 4                                   a = (50 + 2) / 2 = 26
                                                    b = 100 / 26 = 3.84   -> distance = 26 - 3.84 = 22
... ...
... ...


while boolean_expression:  when abs(a - b) < 0.000000000001

    looping body

'''

# Step 1) prepare data -------------------------------------------------------------------


# x is the number which we need to calculate the square root
x = int(input("Number: "))

# a starts from 1
a = 1

# b starts from x / a, which is x / 1, which is x
b = x

# actual_diff is the distance between a & b
actual_diff = b - a

print(f"a: {a:.3f}, b: {b:.3f}, actual_diff: {actual_diff:.20f}")

'''
Our algo is a loop.
A loop of continuous calculation of a and b, so that a and b get nearer and nearer.
Finally, a and b become so near, both of them are square root of number x.
So the actual diff between a and b is less than the 0.000000000001
we define 0.000000000001 as target_diff
'''

target_diff = 0.000000000001



# Step 2) use our variables / our algo starts / our main program starts -----------------

while actual_diff > target_diff:

    a = (a + b) / 2
    b = x / a

    '''
    # solution 1) 
    if a > b:
        actual_diff = a - b
    else:
        actual_diff = b - a
    '''

    # solution 2)
    actual_diff = abs(a - b)

    print(f"a: {a:.3f}, b: {b:.3f}, actual_diff: {actual_diff:.20f}")


print(f"Square root of {x} is: {a}")
print(f"{a} * {a} = {a ** 2}")

