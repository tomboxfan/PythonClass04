
'''
The most 2 important thing in Python programming is:
1) define a variable
2) use a variable
'''


'''
-------------------------------
Define variables
-------------------------------
'''


'''
This defines a variable
I can give the variable name whatever I like.
I want to give my variable a name -> a_number, and I want to put value 5 into variable a_number's box
'''
a_number = 5



# I want to give my variable a name -> another_number, and I want to put value 2 into variable another_number's box
another_number = 2


# I want to give my variable a name -> greeting_word, and I want to put value "hello!" into variable greeting_word's box
greeting_word = 'Hello!'

'''
Ctrl + D helps you quickly duplicate the current line
'''


'''
-------------------------------
Use variables
-------------------------------
'''

print(a_number)
print(another_number)
print(greeting_word)

print(a_number, another_number, greeting_word)



'''
This is using variable a_number & another_number
This is also defining a new variable plus_variable

a_number's value + another_number's value will be assigned to variable plus_variable, and I'd like to name it 'plus_variable'
'''
plus_variable = a_number + another_number
minus_variable = a_number - another_number
multiply_variable = a_number * another_number
divide_variable = a_number / another_number     # 5 / 2 = 2.5

# Floor division - find quotient
divide_variable2 = a_number // another_number     # 5 // 2 = 2 (quotient)

# Find remainder
remainder_variable = a_number % another_number     # 5 % 2 = 1 (remainder)

'''
ctrl + x -> cut 
ctrl + v -> paste
'''

'''
5 * 5 
'''
power_variable = a_number ** another_number       # 5 ** 2 = 25 / 5 ** 3 = 125 / 5 ** 4 = 625






# basic
print(a_number, "+", another_number, "=", plus_variable)
print(a_number, "-", another_number, "=", minus_variable)
print(a_number, "*", another_number, "=", multiply_variable)
print(a_number, "/", another_number, "=", divide_variable)


# advance
print(a_number, "//", another_number, "=", divide_variable2)
print(a_number, "%", another_number, "=", remainder_variable)


# super_advance
print(a_number, "**", another_number, "=", power_variable) # 5 * 5 = 25



# super advance



'''
"+" & "=" are called: 字符串 -> 字符 串在了一起
                      string
'''


# step 1) define variables a/b/c/d/e/f
a = 1
b = 2
c = 5
d = 6
e = 7
f = 9


# step 2) doing math using variables a/b/c/d/e/f , assign the result to a newly-defined variable 'answer'
answer = (a - (a / d) * (b / c)) / (e / f)

# step 3) use variable answer
print(answer)





