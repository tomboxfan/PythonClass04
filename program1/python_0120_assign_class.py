'''
Requirement:
We have some students, based on their math / science / english score, we will assign them to the following classes.

Elite Class - all 3 subjects should have score higher than 85
Math Elite Class - Math score higher than 85 and 3 subjects average higher than 75 and no subject lower than 70
Science Elite Class - Science score higher than 85 and 3 subjects average higher than 75 and no subject lower than 70
English Elite Class - English score higher than 85 and 3 subjects average higher than 75 and no subject lower than 70
Express Class - average higher than 75 and no subject lower than 65
Normal Class - other students

You need to ask user to input math score / science score / english score from console, then assign them to the correct class.
'''


# PART 1) DEFINE VARIABLES ===========================================

# type 1) Define variables from the question ----------------------------------

math_score = float(input("Math score: "))
science_score = float(input("Science score: "))
english_score = float(input("English score: "))


# Type 2) DEFINE VARIABLE WHICH IS TO SAVE THE RESULT -----------------
class_name = ''


# Type 3) other extra variables  ------------------------------------
average_score = (math_score + science_score + english_score) / 3
print(f"Your score is: {math_score}, {science_score}, {english_score}. Average score: {average_score:.2f}")





# PART 2) YOUR ALGO ===========================================

'''
if <bool expression> :
    go to elite
    
elif <boolean expression> :        

    if <bool expression> :
        go to math elite
        
    elif <bool expression> :
        go to science elite
        
    else :
        go to english elite
        
    
elif <bool expression> :
    go to express
    
else:
    go to normal

'''

# Step 3) Check elite class
if math_score > 85 and science_score > 85 and english_score > 85:
    class_name = 'Elite Class'

# Step 4) Check Math Elite / Science Elite / English Elite class
elif (math_score > 85 or science_score > 85 or english_score > 85) and average_score > 75 and math_score >= 70 and science_score >= 70 and english_score >= 70:

    if math_score > 85:
        class_name = 'Math Elite Class'

    elif science_score > 85:
        class_name = 'Science Elite Class'

    else:
        class_name = 'English Elite Class'

# Step 5) Check Express
elif average_score > 75 and math_score >= 65 and science_score >= 65 and english_score >= 65:
    class_name = 'Express Class'

# Step 6) Assign to Normal
else:
    class_name = 'Normal Class'




# PART 3 PRINT THE RESULT ===================================================

# Step 7) Print the result
print(f"You are assigned to {class_name}")





