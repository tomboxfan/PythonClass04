'''
Requirement:
user inputs year / month / day information from the console
Your program needs to tell the user how many days in the year there are in front of the date which user input
For example: if user tells you 2019 Jan 1st, then your output should be 1
For example: if user tells you 2019 Feb 1st, then your output should be 32
HINT: Please consider leap year.

Q) How to tell whether a year is a leap year or not?

A) Case 1) The year number can be divided by 4, but not 100.
   Case 2) The year number can be divided by 400
   For either case, the year is a leap year.
'''


year = int(input("Please input the year: "))
month = int(input("Please input the month: "))
day = int(input("Please input the day: "))

print(f"{year}-{month}-{day}")

'''
----------------------------
The algo is most important.
----------------------------

Each date is composed of 2 parts:
1) month
2) day

We need to calculate 
a) the days in those full months
b) day not in the full month
Then we plus a & b, that's our answer.
'''

total_days = 0

if month > 1:
    total_days += 31
if month > 2:
    total_days += 28
if month > 3:
    total_days += 31
if month > 4:
    total_days += 30
if month > 5:
    total_days += 31
if month > 6:
    total_days += 30
if month > 7:
    total_days += 31
if month > 8:
    total_days += 31
if month > 9:
    total_days += 30
if month > 10:
    total_days += 31
if month > 11:
    total_days += 30

total_days += day


# check leap year ---------------------------------------------
is_leap_year = False

'''
A) Case 1) The year number can be divided by 4, but not 100.
   Case 2) The year number can be divided by 400
   For either case, the year is a leap year.
'''
# if <Please put your boolean expression here>:
#     is_leap_year = True

if is_leap_year and month > 2:
    total_days += 1

# -------------------------------------------------------------


print("Total days: ", total_days)
