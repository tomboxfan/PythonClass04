'''

1) Please define several lists from your daily life

2) You need access the value using index from your defined lists

3) You need to insert & append values to your list

4) Can you print all values in your list using loop? (VERY DIFFICULT)

'''

l = list(range(5))
print(l)

print(l[2])     # 2
print(l[-2])    # 3

l.insert(3, 'X')
print(l)

l.insert(-1, 'B')
print(l)

l.append("Q")
print(l)
