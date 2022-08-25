A = int(input())
B = int(input())
C = int(input())
if A < B:
    y = A
    x = B
else:
    y = B
    x = A
if x < C:
    x = C
if y > C:
    y = C

print(y)
print(x)