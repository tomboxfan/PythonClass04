


'''
If some line has 0 spaces in the front, we call it 'indentation level 1'
If some line has 4 spaces in the front, we call it 'indentation level 2'

'''


years_learnin_python = int(input("How many years have you been learning Python? "))


if years_learnin_python > 5:
    print(f"Not bad! {years_learnin_python} years is quite a long time, you've already been a Python Guru!")
    print("I am sure you can earn a lot of money in the market!")

else: # else clause (子句) if I type colon (:), I press 'enter' immediately
    print(f"{years_learnin_python} years is still quite short.")
    print("I know it is hard, just hang in there! Not everybody has the opportunity to learn python!")
    print("You are very lucky!")


print("Python is the future! You are on the right track!")


'''
IMPORTANCE!!! -------------------------------------------

if <boolean expression> :   # Press enter if you type :
    <statement 1>       <block 1>
    <statement 2>
    <statement 3>
else:
    <statement 4>       <block 2> 
    <statement 5>
    <statement 6>

1) block 1 will be executed if boolean expression is True
2) block 2 will be executed if boolean expression is False
'''