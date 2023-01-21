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