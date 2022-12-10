
is_bank_customer = input("如果您是本行客户，请按1; 如果您不是本行客户, 请按2: ")
service_type = input("信用卡服务, 请按1; 贷款服务, 请按2; 挂失请按3: ")

print(is_bank_customer, service_type)

print("-" * 100)

'''
1 - current account
2 - saving account

1 - show me the balance, 2 - withdraw money, 3 - deposit money

withdraw amount:
'''


initial_amount = 10000


account_type = input("1 - current account, 2 - saving account: ")
service_type = int(input("1 - show me the balance, 2 - withdraw money, 3 - deposit money: "))

if service_type == 1:
    print(f"You have {initial_amount} in your account.")
elif service_type == 2:
    pass
elif service_type == 3:
    pass

# HOMEWORK


print("-" * 50)


