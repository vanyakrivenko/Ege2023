A = int(input())
B = int(input())
x = A
y = B
if A > B:
    y = x
else:
    x = y
if A != B:
    A = B = x
else:
    A = B = 0
print(A, B)
