
import statistics as stat
N = int(input())
L = int(input())
K = int(input())
A = [int(input("A["+str(i)+"]=")) for i in range(N)]
s = 0
c = 0
for i in range(0,N):
    if i not in range(K,L+1):
        c += 1
        s += A[i]

A1 = [x for i, x in enumerate(A) if i not in range(K,L+1)]

print(stat.mean(A1))