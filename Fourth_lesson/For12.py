N = int(input())
re = 1

for i in range(1, N+1):
    re = re * (1 + 0.1 * i)

print(re)