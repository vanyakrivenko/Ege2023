
N = int(input())
A = [int(input("A["+str(i)+"]=")) for i in range(N)]
print(min(A[::2]))