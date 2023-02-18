'''
Requirement:

1) Get student count from console. Ask user to tell you how many students in total.
2) For each student, let user to input the student score.
3) Calculate the average score of all students.

Comparing with Version 1:
You need to check the validity of the student's score, it must be in range [30, 100]


New Requirement for Version 3)
Round a score to the next multiple of 5 if it is not a failing score.

If the difference between the score and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the score is less than 58, no rounding occurs, as it is a failing score.
For example: score = 84, round to 85 (because 85 - 84 less than 3)
             score = 57, no rounding (because 57 is less than 58)
             score = 67, no rounding ( because 70 - 67 is 3 or greater)
'''

# Step 1) PREPARE DATA BEGIN =======================================

student_count = int(input("How many students: "))

total_score = 0

average_score = 0

# Step 2) ALGO BEGIN ===============================================

for student_no in range(student_count):

    # Step 2.1) check score validity, repeat until user inputs a score fall in range [30, 100]
    score = 0 # put a init value to score variable

    while score < 30 or score > 100:
        score = int(input(f"Student {student_no + 1} score: ")) # update looping variable
        if score < 30 or score > 100:
            print('Wrong input, please try again ...')



    # Step 2.2) round the score to the next multiple of 5 if it is not a failing score
    if score % 5 >= 3 and score >= 58:      # the boolean expression is difficult!
        score = score + (5 - score % 5)     # this expression is difficult!
        print(f"After rounding, your score is: {score}")
    else:
        print(f"No rounding is required. Your score is: {score}")


    total_score += score

average_score = total_score / student_count

# Step 3) PRINT ANSWER ============================================
print(f"Average score is: {average_score:.2f}")

