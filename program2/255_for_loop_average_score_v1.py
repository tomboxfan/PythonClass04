'''
Requirement:

1) Get student count from console. Ask user to tell you how many students in total.
2) For each student, let user to input the student score.
3) Calculate the average score of all students.

----------
Sample
----------
How many students: 5
Student 1 score: 50
Student 2 score: 60
Student 3 score: 90
Student 4 score: 40
Student 5 score: 90
Average score is: 66.00
'''

# Step 1) PREPARE DATA BEGIN =======================================

student_count = int(input("How many students: "))

total_score = 0

average_score = 0

# Step 2) ALGO BEGIN ===============================================

for student_no in range(student_count):

    score = int(input(f"Student {student_no + 1} score: "))
    total_score += score

average_score = total_score / student_count

# Step 3) PRINT ANSWER ============================================
print(f"Average score is: {average_score:.2f}")

