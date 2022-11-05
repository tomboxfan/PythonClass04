

# Here we have 2 str variables

first_name = "James"
last_name = "Bond"

'''
Requirement: 

Print out this sentence:
My name is Bond, James Bond.

You must use these 2 variables - first_name, last_name 
'''

'''
[Solution 1]
We pass 6 str values to print() function as arguments. 
[Problem]
There are extra spaces after 'Bond'
[Why]
Because print function will automatically insert space among those arguments.
'''
print("My name is", last_name, ",", first_name, last_name, ".")


'''
[Solution 2]
Use '+' sign to join these str values together, create a new str variable - sentence, then we send this sentence variable as the only argument to print function.
We can control the space ourselves.
[Problem]
We use too many '+' sign, this code looks very messy, not readable.
'''
sentence = "My name is " + last_name + ", " + first_name + " " + last_name + "."
print(sentence)


'''
[Solution 3] - Python f string
IMPORTANCE !!! ---------------------------------------
1) have an f at the beginning. 'f' means: 'formatted' (格式化) 
   f string also means: formatted string.
   
   What is formatted string (格式化字符串)? 
   it means: You can nest variables inside your string. 
   
2) variables wrapped inside curly braces, these variables will be replaced by their actual value.

Python formatted string can help easily combine actual string values with variables.
'''
sentence2 = f'My name is {last_name}, {first_name} {last_name}.'
print(sentence2)



s3 = f"No, Mr {last_name}, I expect you to die!"
print(s3)



age = 93
s4 = f"Sean Connery is now {age} years old. "
print(s4)


language = "Python"
rank = 1
who = "All kids"
kids_age = 12
teacher_surname = "FAN"

s5 = f"{language} is the world No.{rank} programming language, {who} should start learning it from age {kids_age}, and they all should learn {language} with Teacher {teacher_surname}."
print(s5)

s6 = f"{who} enjoy learning {language}, as {language} is quite fun, and teacher {teacher_surname} is quite fun! "
print(s6)

# variable can be reused multiple times!


'''
IMPORTANCE!!! -----------------------------------------
1) Besides variables, you can also use expressions
'''

s7 = f"2 + 3 = {2 + 3}"
print(s7)


