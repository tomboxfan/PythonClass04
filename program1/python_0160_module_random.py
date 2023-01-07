
# IMPORTANT!! ---------------------------
# This is to import random module
# ---------------------------------------
import random



'''
IMPORTANCE!!! ------------------------------
random.randint(1, 10) is composed of 4 parts

1) random   : module name
2) .        : separate module name and function name
3) randint  : function name
              it is under random module
              it will return a random number in range [1, 10], both 1 and 10 are included ('closed interval' / 闭区间)
              In math, we use [ and ] to express 'closed interval'
              
              [1, 10) : 1 to 9
              (1, 10) : 2 to 9
              [1, 10] : 1 to 10
              
4) (1, 10)  : both 1 and 10 are arguments. They are surrounded by 1 pair of parentheses            
              What is argument? Argument is some value you pass to a function.
--------------------------------------------
'''



i = 0
while i < 10:

    # do something
    random_int = random.randint(1, 3) # random.randint(1, 10) returns a random int in range [1, 10]
    print(random_int)

    i += 1
