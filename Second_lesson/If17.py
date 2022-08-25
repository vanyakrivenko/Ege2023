A = int(input())
B = int(input())
C = int(input())
x = 0

if (A < B and B < C) or (A > B and B > C):
    x = 2
else:
    x = -1
A *= x
B *= x
C *= x

print(A,B,C)