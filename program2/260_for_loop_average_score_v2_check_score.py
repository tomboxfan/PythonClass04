'''
Requirement:

1) Get student count from console. Ask user to tell you how many students in total.
2) For each student, let user to input the student score.
3) Calculate the average score of all students.

Comparing with Version 1:
You need to check the validity of the student's score, it must be in range [30, 100]

----------
Sample
----------
How many students: 5
Student 1 score: 20
Wrong input, please try again ...
Student 1 score: 60
Student 2 score: 70
Student 3 score: 101
Wrong input, please try again ...
Student 3 score: 100
Student 4 score: 90
Student 5 score: 75
Average score is: 79.00
'''

# Step 1) PREPARE DATA BEGIN =======================================

student_count = int(input("How many students: "))

total_score = 0

average_score = 0

# Step 2) ALGO BEGIN ===============================================

for student_no in range(student_count):


    # score = int(input(f"Student {student_no + 1} score: "))
    score = 0 # put a init value to score variable

    while score < 30 or score > 100:
        score = int(input(f"Student {student_no + 1} score: ")) # update looping variable
        if score < 30 or score > 100:
            print('Wrong input, please try again ...')

    total_score += score

average_score = total_score / student_count

# Step 3) PRINT ANSWER ============================================
print(f"Average score is: {average_score:.2f}")

