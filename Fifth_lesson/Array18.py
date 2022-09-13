
N = 10
A = [int(input("A["+str(i)+"]=")) for i in range(N)]

f = True
for i in range(0,N-1):
    if A[i] < A[N-1]:
        print(i,A[i])
        f = False
        break
if f:
    print(0)