

# PREPARE DATA -----------------------------------

float_a = float(input("Number a: "))
float_b = float(input("Number b: "))
operator = input("Operator: ")
result = 0

# ALGO (算法) -------------------------------------

if operator == '+':
    result = float_a + float_b
elif operator == '-':
    result = float_a - float_b
elif operator == '*':
    result = float_a * float_b
elif operator == '/':
    if float_b == 0:
        print("Wrong input, please try again!")
        exit()
    else:
        result = float_a / float_b
    '''
    This is called nested if / else -> You have another if / elif / else inside the if body / elif body / else body
    '''

elif operator == '**':
    result = float_a ** float_b
else:
    print(f"Unrecognized operator: {operator}")
    exit()


# PRINT RESULT -----------------------------------
print(f"{float_a} {operator} {float_b} = {result}")