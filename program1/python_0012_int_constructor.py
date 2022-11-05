int_a = int('10')
print(int_a)

'''
IMPORTANCE!!! ---------------------------------------
1) int(...) is called int constructor.
2) '10' is a str value, you put str value '10' inside int constructor -> int('10')
3) int constructor helps convert str '10' to int 10
'''


int_b = int(1.2)
print(int_b)

'''
IMPORTANCE!!! ---------------------------------------
1) 1.2 is a float value, you put float value 1.2 inside int constructor -> int(1.2)
2) int constructor helps convert float 1.2 to int 1
'''

'''
we've learnt print() / type() / int()
1.2 and '10' have a name - argument(参数)
'''

int_c = int()
print(int_c)


'''
IMPORTANCE!!! ---------------------------------------
1) if you put nothing inside int constructor, then it creates int 0.
2) so int_c has value 0
'''

'''
Can you do this? 
int(int_d) = 10

You can never use int constructor on the left side of '=', this is WRONG!
Because int constructor gives you a int value, value can only appear on the right side of '='
You ALWAYS put variable on the left side of '='.
'''


'''
HOMEWORK -------------------------------------------------------------------------------------
'''

print("The following are for your own experiment ----------------------")

int_d = int(2.1)
int_e = int(3.9)
int_f = int(-4.1)
int_g = int(-5.9)

'''
1) guess the value of the 4 int variables.
2) print the 4 int variables to console.
3) summarize how int constructor works for float value.
'''