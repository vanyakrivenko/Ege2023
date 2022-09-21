N = int(input())
A = [int(input("A["+str(i)+"]=")) for i in range(N)]
B = []
B.append(A[0])
for i in range(1,N):
    B.append(A[i] + B[i-1])
print(B)