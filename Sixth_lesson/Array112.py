N = int(input())
a = [int(input("A["+str(i)+"]=")) for i in range(N)]
for i in range(1,N):
    for j in range(0,N-i):
        if a[j] > a[j+1] :
            a[j], a[j+1] = a[j+1], a[j]
print(a)