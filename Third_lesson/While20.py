N = int(input())

a = N
i = 0
f = False
while a >= 1:
    i += 1
    r = a % 10
    if r == 2:
        f = True
        break
    a = int(a/10)

print(f)
