
N = int(input())
A = [int(input()) for i in range(N)]
K = 0

for i in range(N):
    if A[i] % 2 == 1:
        K += 1

print(K)