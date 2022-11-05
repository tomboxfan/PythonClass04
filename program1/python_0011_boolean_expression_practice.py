'''

Let's say, there are 34 students in your class.
18 boys, 16 girls.
'''

boys = 18
girls = 16
total = boys + girls

print(f"We have boys: ", boys)
print(f"We have girls: ", girls)
print(f"We have total students: ", total)

'''
Now, please express the following statement using boolean expression, and print its boolean value.
I will finish the 1st one for you.
'''

'''
Q1) We have more than 20 boys, right?
'''
we_have_more_than_20_boys = (boys > 20)
print("We have more than 20 boys, right? ", we_have_more_than_20_boys)



'''
Q2) We have more than 16 girls, right?
'''
q2 = (girls > 16)
print("We have more than 16 girls, right? ", q2)



'''
Q3) We have equal boys and girls, right?
'''
q3 = (boys == girls)
print("We have equal boys and girls, right? ", q3)



'''
Q4) We have more boys than girls, right?
'''
q4 = (boys > girls)
print("We have more boys than girls, right? ", q4)



'''
Q5) there are more than 5 boys than girls, right?  In Chinese: 男孩儿人数比女孩儿人数多超过5个
'''
q5 = (boys - girls > 5)
print("there are more than 5 boys than girls, right? ", q5)


'''
Q6) there are 5 more boys than girls, right?  In Chinese: 男孩儿比女孩儿人数多5个
'''
q6 = (boys - girls == 5)
print("there are 5 more boys than girls, right? ", q6)






