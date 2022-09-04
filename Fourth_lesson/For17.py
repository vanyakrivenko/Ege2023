A = int(input())
N = int(input())
re = 1
p = 1
for i in range (1, N + 1):
    p = p * A
    re = re + p
print(re)