'''
There are 4 kinds of data in Python, meaning 4 kinds of data type.

1) int - 整数
2) float - 小数
3) str - 字符串
4) bool - True / False
'''

# int
# define a new variable h
h = 2 + 3    # 2 + 3 = 5, so variable h contains value 5

# define a new variable j, I use variable h
j = h - 100  # 5 - 100 = -95, so variable j contains value -95

# define a new variable k, I use variable h * j
k = h * j    # 5 * -95 = -475, so variable k contains value -475

print("variable h type is: ", type(h), 'h =', h)
print("variable j type is: ", type(j), 'j =', j)
print("variable k type is: ", type(k), 'k =', k)

'''
type() is a function

Q) What is a function?
A) Function has a name - type
   Function has a pair of parentheses after the function name - type()
   Sometimes, we can put a value inside the parentheses - type(h), print("Hello")
   
   Function does something for you.
   print("Hello") is a function, it helps you print "Hello" to the console  -> call my function, 
   type(h) is a function, it tells you the type of variable h.

Q) What is python built-in function?
A) The function is supplied / defined by Python

We will learn user-defined function in the future. 
'''



# float - 小数
a = 1.2
b = 0.01
c = -12.0
d = a + b + c
print("variable a type is: ", type(a), 'a =', a)
print("variable b type is: ", type(b), 'b =', b)
print("variable c type is: ", type(c), 'c =', c)
print("variable d type is: ", type(d), 'd =', d)

e = j / h
print("variable e type is: ", type(e), 'e =', e)
