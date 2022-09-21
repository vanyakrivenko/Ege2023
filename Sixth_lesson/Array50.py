N = int(input())
A = [int(input("A["+str(i)+"]=")) for i in range(N)]
n_i = 0
for i in range(0,N-1) :
    for j in range(i+1,N) :
        if A[i] > A[j] :
            n_i += 1
print(n_i)