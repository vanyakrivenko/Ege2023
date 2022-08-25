A = int(input())
B = int(input())
C = int(input())
x = 0
y = 0
if A > 0:
    x += 1
if B > 0:
    x += 1
if C > 0:
    x += 1
print(x)
if A < 0:
    y += 1
if B < 0:
    y += 1
if C < 0:
    y += 1
print(y)