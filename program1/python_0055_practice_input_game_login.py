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


user_name = input("User name: ")
password = input("Password: ")

print(f"Welcome! {user_name}, you've logged in successfully! ")