'''

bool is the 4th data type in Python. Sometimes, we call it boolean, it means bool.
it has only 2 values. True and False
it means something is true of false.

For example:
"Today is Sunday."     False
"Today is Saturday."   True
"Singapore is an European country."   False

I can define boolean variables which hold the above 3 bool results.

'''

# Step 1) define a variable
today_is_sun = False
today_is_sat = True
sg_is_in_europe = False


# Step 2) Use variable
print("Is today Sunday? ", today_is_sun)
print("Is Singapore in Europe? ", sg_is_in_europe)

print("variable today_is_sun, its type is: ", type(today_is_sun), ", its value is: ", today_is_sun)
print("variable sg_is_in_europe, its type is: ", type(sg_is_in_europe), ", its value is: ", sg_is_in_europe)


'''
bool value can be calculated using a boolean expression, just like 
int / float value can be calculated using an arithmetic expression.
'''

'''

What is a boolean expression?
boolean expression gives you a boolean value. Just like 1 + 2 gives you 3 (int value) 
1 > 2 is a boolean expression, and the expression's value is False
1 < 2 is a boolean expression, and the expression's value is True
'''


bool3 = (1 > 2) # 1 > 2 is False, variable bool3 now has value -> False
bool4 = (1 < 2) # 1 < 2 is True,  variable bool4 now has value -> True

print("Variable bool3 type is: ", type(bool3), ". bool3 = ", bool3)
print("Variable bool4 type is: ", type(bool4), ". bool4 = ", bool4)