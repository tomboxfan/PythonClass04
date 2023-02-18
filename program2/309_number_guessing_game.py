'''
Requirement:

Build a Number guessing game, in which the user selects a range, for example: 1, 100.
And your program will generate some random number in the range, for example: 42.
And the user needs to guess the number.
If his answer is 50, then you need to tell him. “Try Again! You guessed too high”
If his answer is 20, then you need to tell him. “Try Again! You guessed too low”
When he finally guesses it, you need to tell him, how many times he guesses.
'''

import random


# Step 1) PREPARE DATA BEGIN =======================================

lower = int(input("Enter positive lower bound: "))
upper = int(input("Enter positive upper bound: "))

answer = random.randint(lower, upper)

count = 0

# Step 2) ALGO BEGIN ===============================================

# Loop to ask user "What's the correct answer? ", and tell him / her higher or lower, if it is correct, exit.

while True:

    # Step 2.1) Get user guess
    guess_result = int(input("Guess a number: "))

    # Step 2.2) update the count
    count += 1

    # Step 2.3) check user guess
    if answer == guess_result:
        print(f"Congrats! You did it in {count} try.")
        break

    elif answer > guess_result:
        print("Try again! You guessed too low!")

    else:
        print("Try again! You guessed too high!")


# Step 3) PRINT ANSWER ============================================
# nothing


'''
optimized solution to play the game: 
You always guess the number exactly in the middle, so that you can quickly eliminate half the options.

This is a very famous computer algo: binary search (二分搜索)

The No.1 condition for binary search: all your numbers must be sorted properly.  *** 

'''