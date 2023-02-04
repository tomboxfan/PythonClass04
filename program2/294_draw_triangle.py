'''
1) Right triangle 1

1st line: 1 '*'
2nd line: 2 '*'
...
10th line: 10 '*'

if I let my looping variable line_number loop from 0 - 9:
print 1, 2, 3 ....10 '*'

I need to find such an expression that:
when line_number is 0   -> 1
when line_number is 1   -> 2
when line_number is 2   -> 3

so the expression is:
line_number + 1
'''

# Solution 1)
for line_number in range(10):
    print('*' * (line_number + 1))


# Solution 2)
# for line_number in range(1, 11):
#     print('*' * line_number)

print("\n\n ----------------------------- \n\n")

'''
2) Right triangle 2

1st line: 9 ' ' + 1 '*'
2nd line: 8 ' ' + 2 '*'
...
10th line: 0 ' ' + 10 '*'

if I let my looping variable line_number loop from 0 - 9:
print 9, 8, 7 .... 0 ' '
print 1, 2, ......10 '*'



if I let my looping variable line_number loop from 0 - 9:
print 9, 8, 7 .... 0 ' '
print 1, 2, ......10 '*'

I need to find 2 expressions that:
when line_number is 0   -> 9, 1
when line_number is 1   -> 8, 2
when line_number is 2   -> 7, 3

so the 2 expressions are: 
1) 9 - line_number   ( because when line_number goes up, the result goes down, so we have to put minus in front of line_number)
2) line_number + 1

'''

for line_number in range(10):
    print(' ' * (9 - line_number) + '*' * (line_number + 1))

print("\n\n ----------------------------- \n\n")



'''
3) isosceles triangle 

1st line: 9 ' ' + 1 '*'
2nd line: 8 ' ' + 3 '*'
...
10th line: 0 ' ' + 19 '*'

if I let my looping variable line_number loop from 0 - 9:
print 9, 8, 7 .... 0 ' '

print 1, 3, 5 ....19 '*'
I need to find 2 expressions that:
when line_number is 0   -> 9, 1
when line_number is 1   -> 8, 3
when line_number is 2   -> 7, 5
...
when line_number is 9   -> 0, 19


so the 2 expressions are: 
1) 9 - line_number     (explained in 2nd example)
2) line_number * 2 + 1 (because when line_number goes 1 step, the result goes 2 steps, so we must put * 2 to variable line_number) 
'''

for line_number in range(10):
    print(' ' * (9 - line_number) + '*' * (line_number * 2 + 1))