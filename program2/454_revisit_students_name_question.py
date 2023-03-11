
'''
Requirement:
Read students name from console, stop when user type 'exit', and print their names in one line
'''

names = []

while True:
    
    tmp = input("Student name: ")

    if tmp == 'exit':
        break

    names.append(tmp)


for s in names:
    print(s, end=', ')