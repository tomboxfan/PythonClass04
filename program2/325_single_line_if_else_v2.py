age = int(input("Show me your age: "))


'''
if age < 18:
    kids_or_adult = 'kids'
else:
    kids_or_adult = 'adult'
    
    
The above code can be simplified into 1 line:
'''

kids_or_adult = 'kids'                        if              age < 18                else            'adult'
#               <value when it is true>       if              <boolean expression>    else            <value when it is false>



kids_or_adult = 'kids' if age < 18 else 'adult'



print(kids_or_adult)
