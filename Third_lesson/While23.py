N = int(input())
K = int(input())
while (N!=0) and (K!=0):
    if N > K:
        N = (N % K)
    else:
        K = (K % N)
print((N+K))