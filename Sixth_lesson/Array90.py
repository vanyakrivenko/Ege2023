N = int(input())
K = int(input())
a = [int(input("A["+str(i)+"]=")) for i in range(N)]
N = len(a)
a.pop(K - 1)
print(a)