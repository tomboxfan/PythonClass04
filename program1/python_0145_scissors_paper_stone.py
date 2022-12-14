'''
Requirement:
Step 1) Ask player_a to input 'scissors', 'paper', 'stone', 'exit'.
Step 2) Use while loop, loop as long as player_a's input is NOT 'exit'.
Step 3) Inside the while loop body, you ask player_b to input 'scissors', 'paper', 'stone'.
Step 4) Use if / elif / else or nested if / elif / else to check who wins, print the result.
'''


'''
-------------------
Thinking Logic
-------------------

------------------------------------------------------------
For all python programs, step 1) prepare 'data'
------------------------------------------------------------

For this question, what is 'data'?

player_a's choice, being 'scissors' / 'paper' / 'stone' / 'exit', is data.
player_b's choice, being 'scissors' / 'paper' / 'stone', is data.


------------------------------------------------------------
data is stored in variable, preparing 'data' means defining 'variable'
------------------------------------------------------------


step 1) using a input function, get player_a's choice, save to a variable -> user_a_choice
step 2) using a while loop, loop with condition: user_a_choice != 'exit'

inside loop body:
step 3) using a input function, get player_b's choice, save to a variable -> user_b_choice

step 4) comparing user_a_choice vs user_b_choice

    This is the most difficult part of this program.
    I never code line by line
    I code from top to bottom
    
    
    1) I set up skeleton
    if user_a_choice == 'scissors':
        pass # Place holder
    elif user_a_choice == 'paper':
        pass # Place holder
    elif user_a_choice == 'stone':
        pass # Place holder
    else:
        print(f"User A inputs a wrong choice: {user_a_choice} ")

    2) I fill up flesh




step 5) final step in loop body, read again from console (user) value of user_a_choice (update the looping variable)
'''

user_a_choice = input("User A's choice (scissors / paper / stone / exit): ")

while user_a_choice != 'exit':

    # step 3)
    user_b_choice = input("User B's choice (scissors / paper / stone): ")


    # step 4)
    if user_a_choice == 'scissors':
        if user_b_choice == 'scissors':
            print(f"User A: {user_a_choice}, User B: {user_b_choice}. Draw.")
        elif user_b_choice == 'paper':
            print(f"User A: {user_a_choice}, User B: {user_b_choice}. User A Wins.")
        elif user_b_choice == 'stone':
            print(f"User A: {user_a_choice}, User B: {user_b_choice}. User B Wins.")
        else:
            print(f"User B inputs a wrong choice: {user_b_choice}")

    elif user_a_choice == 'paper':
        if user_b_choice == 'scissors':
            print(f"User A: {user_a_choice}, User B: {user_b_choice}. User B Wins.")
        elif user_b_choice == 'paper':
            print(f"User A: {user_a_choice}, User B: {user_b_choice}. Draw.")
        elif user_b_choice == 'stone':
            print(f"User A: {user_a_choice}, User B: {user_b_choice}. User A Wins.")
        else:
            print(f"User B inputs a wrong choice: {user_b_choice}")

    elif user_a_choice == 'stone':
        if user_b_choice == 'scissors':
            print(f"User A: {user_a_choice}, User B: {user_b_choice}. User A Wins.")
        elif user_b_choice == 'paper':
            print(f"User A: {user_a_choice}, User B: {user_b_choice}. User B Wins.")
        elif user_b_choice == 'stone':
            print(f"User A: {user_a_choice}, User B: {user_b_choice}. Draw.")
        else:
            print(f"User B inputs a wrong choice: {user_b_choice}")

    else:
        print(f"User A inputs a wrong choice: {user_a_choice}")

    print("-" * 100)

    # step 5)
    user_a_choice = input("User A's choice (scissors / paper / stone / exit): ")
