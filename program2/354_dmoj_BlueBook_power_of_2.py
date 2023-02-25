'''
here comes the questions list:
https://dmoj.ca/problems/?category=46
You can try problems inside the page one after another.


https://dmoj.ca/problem/p129ex3
'''


# Step 1) PREPARE DATA BEGIN =======================================

# Step 1.1) DEFINE VARIABLE READ FROM INPUT(mandatory)
i = int(input())

# Step 1.2) DEFINE VARIABLE TO SAVE RESULT(mandatory)
answer = 0

# Step 2) ALGO BEGIN ===============================================
while 2 ** answer < i:
    answer += 1


# Step 3) PRINT ANSWER ============================================
print(answer)