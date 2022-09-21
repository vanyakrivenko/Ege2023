
N = int(input())
K = int(input())
a = [int(input("A["+str(i)+"]=")) for i in range(N)]
for i in range(0,N-K) :
    a[i] = a[i+K]
for i in range(N-K,N) :
    a[i] = 0
print(a)

