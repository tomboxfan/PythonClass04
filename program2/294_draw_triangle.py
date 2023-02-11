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


print("\n\n ----------------------------- \n\n")


'''
4) parallelogram

1st line: 9 ' ' + 10 '*'
2nd line: 8 ' ' + 10 '*'
...
10th line: 0 ' ' + 10 '*'

if I let my looping variable line_number loop from 0 - 9:
print 9, 8, 7 .... 0 ' '
print 10 '*'


I need to find 2 expressions that:
when line_number is 0   -> 9, 10
when line_number is 1   -> 8, 10
when line_number is 2   -> 7, 10

so the 2 expressions are: 
1) 9 - line_number   ( because when line_number goes up, the result goes down, so we have to put minus in front of line_number)
2) 10

'''

for line_number in range(10):
    print(' ' * (9 - line_number) + '*' * 10)


print("\n\n ----------------------------- \n\n")

'''
5) obtuse triangle
print 0,1,2 ...9 ' ' + 1,2,...10 '*'
'''

for line_number in range(10):
    print(' ' * line_number + '*' * (line_number + 1))

print("\n\n ----------------------------- \n\n")

'''
6) obtuse triangle2
print 18,16,14...0 ' ' + 1,2,...10 '*'

line_number = 0 -> 18
line_number = 1 -> 16
line_number = 2 -> 14

1) because as line_number goes up, the expression goes down  ->   - line_number
2) because line_number goes up 1, the expression goes down 2 ->   - line_number * 2
3) because when line_number is 0, the expression is 18       ->   18 - line_number * 2

18 - line_number * 2
'''


for line_number in range(10):
    print(' ' * (18 - line_number * 2) + '*' * (line_number + 1))


print("\n\n ----------------------------- \n\n")

'''
hourglass

19 lines in total
1st line: 0 ' ' + 19 '*' 
2nd line: 1 ' ' + 17 '*'
...
9th line: 8 ' ' + 3 '*' 
10th line: 9 ' ' + 1 '*'
11th line: 8 ' ' + 3 '*'
..
19th line: 0' ' + 19 '*' 


because it is symmetrical, it in total loops 19 times, 
so I loop in range (-9, 10)

Loop -9 to 9: 
1) print 0,1,2 ...8,9,8....1,0 ' '; 
2) print 19, 17, 15 ....3, 1, 3....17, 19 '*' 

a) abs(line_number)                             abs(line_number)                    reason: because it is symmetrical
b) - abs(line_number)                           abs(line_number)                    reason: the change direction vs the looping variable change direction
c) - abs(line_number)                           abs(line_number) * 2                reason: the change step vs the looping variable change step
d) 9 - abs(line_number)                         abs(line_number) * 2 + 1            reason: the extra constant number 

'''

for line_number in range(-9, 10):
    print(' ' * (9 - abs(line_number)) + '*' * (abs(line_number) * 2 + 1))


print("\n\n ----------------------------- \n\n")

'''
pine tree / triple isosceles

we know how to print a single isosceles triangle:


for line_number in range(10):
    print(' ' * (9 - line_number) + '*' * (line_number * 2 + 1))

but how to print triple isosceles triangle in 1 single for loop? 
single -> looping in range(10) -> 10 numbers: 0 - 9
triple -> looping in range(30) -> 10 numbers: 0 - 9, 10 numbers: 10 - 19, 10 numbers: 20 - 29

Question: how to make 10 - 19 and 20 - 29 similar to 0 - 9
Answer: Use % 10

'''

for line_number in range(30):
    print(' ' * (9 - line_number % 10) + '*' * (line_number % 10 * 2 + 1))

