x = int(input())
n = int(input())
r = x
p = x
re = 1
rez = 1
for i in range (1, n):
    re = re * (2 * i - 1)
    rez = rez * (2 * i)
    p = p * x * x
    r = r + re * p / (rez * (2 * i + 1))
print(r)