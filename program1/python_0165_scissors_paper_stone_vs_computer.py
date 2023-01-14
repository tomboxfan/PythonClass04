'''
Requirement:
Step 1) Ask player_a to input 'scissors', 'paper', 'stone', 'exit'.
Step 2) Use while loop, loop as long as player_a's input is NOT 'exit'.
Step 3) Inside the while loop body, you ask player_b to input 'scissors', 'paper', 'stone'.
Step 4) Use if / elif / else or nested if / elif / else to check who wins, print the result.
'''
import random

user_a_choice = input("User A's choice (scissors / paper / stone / exit): ")

while user_a_choice != 'exit':

    # step 3)

    # CODE DELETE
    # user_b_choice = input("User B's choice (scissors / paper / stone): ")


    # CODE ADD BEGIN --------------------------------------
    robot_choice = random.randint(1, 3)

    if robot_choice == 1:
        user_b_choice = 'scissors'
    elif robot_choice == 2:
        user_b_choice = 'paper'
    else:
        user_b_choice = 'stone'

    # CODE ADD END --------------------------------------
    '''
    ctrl + / : this helps you change a code to comment, or change a comment back to code
    '''






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
