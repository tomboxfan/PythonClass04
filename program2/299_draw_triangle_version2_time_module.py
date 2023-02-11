import time


for line_number in range(100):
    print('*' * (line_number + 1))
    time.sleep(0.1) # you let your program to sleep for 0.1 second

print("\n\n ----------------------------- \n\n")

for line_number in range(100):
    print(' ' * (99 - line_number) + '*' * (line_number + 1))
    time.sleep(0.1)

print("\n\n ----------------------------- \n\n")

for line_number in range(100):
    print(' ' * (99 - line_number) + '*' * (line_number * 2 + 1))
    time.sleep(0.1)

print("\n\n ----------------------------- \n\n")

for line_number in range(100):
    print(' ' * (99 - line_number) + '*' * 10)
    time.sleep(0.1)


print("\n\n ----------------------------- \n\n")

for line_number in range(100):
    print(' ' * line_number + '*' * (line_number + 1))
    time.sleep(0.1)

print("\n\n ----------------------------- \n\n")

for line_number in range(100):
    print(' ' * (198 - line_number * 2) + '*' * (line_number + 1))
    time.sleep(0.1)


print("\n\n ----------------------------- \n\n")

for line_number in range(-99, 100):
    print(' ' * (99 - abs(line_number)) + '*' * (abs(line_number) * 2 + 1))
    time.sleep(0.1)

print("\n\n ----------------------------- \n\n")

for line_number in range(300):
    print(' ' * (99 - line_number % 100) + '*' * (line_number % 100 * 2 + 1))
    time.sleep(0.1)

