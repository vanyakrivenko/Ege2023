X = int(input())
N = int(input())
r = 1
p = 1
f = 1
for i in range (1, N + 1):
    f = f * i
    p = p * X
    r = r + p/f
print(r)