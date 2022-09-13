
N = int(input())
A = [int(input("A["+str(i)+"]=")) for i in range(N)]

f = False
for i in range(N-2,0,-1):
    print(i)
    if A[i-1] < A[i] and A[i] > A[i+1]:
        f = True
        break
if f:
    print(i)