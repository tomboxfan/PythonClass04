
a = 1.2345678

print("number a is:", a)
print(f"number a is: {a}")


# so many digits after the decimal point.
# I want to print only 2 digits after the decimal point.

print(f"number a is: {a:.2f}")


'''

:.2f       has 3 parts:

:      means   I want to format the number              你告诉Python, 不要这样打印 1.2345678， 请换一种格式！ 
.2     means   keep 2 digits after the decimal point   
f      means   this is a float number 
'''
