'''
Requirement:
Mimic online game user login.
'''

welcome_msg = '''
*********************************
    Welcome to King of Glory
*********************************
'''

'''
This is called multi-line str variable, surrounded by triple single quote
So that the str variable contains multiple lines. 
'''

print(welcome_msg)


real_password = "123456"

user_name = input("User name: ")
password = input("Password: ")

if password == real_password:
    print("Password is correct.")
else:
    print("Password is incorrect.")
    exit() # This function helps quite the whole program


print(f"Welcome! {user_name}, you've logged in successfully! ")

total_coins = 0
short_of_coins_msg = f"Unfortunately, you have only {total_coins} coins in your account. Please top you your account."
print(short_of_coins_msg)

coins_topup_str = input("Total coins to top up: ")
coins_topup = int(coins_topup_str)

total_coins += coins_topup

coins_requirement = 500

if total_coins < coins_requirement:
    print(f"You still do not have enough coins, you need to top up extra {coins_requirement - total_coins} coins.")
else:
    print(f"Now you have coins: {total_coins}. You can continue to play the game.")