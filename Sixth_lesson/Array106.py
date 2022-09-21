N = int(input())
a = [int(input("A["+str(i)+"]=")) for i in range(N)]
b = N//2
a.extend([0]*b)
j = 0
for i in range(N-1,0,-2) :
    a[(N+b-1)-j] = a[i]
    a[(N+b-2)-j] = a[i-(N%2)]
    a[(N+b-3)-j] = a[i-1]
    j += 3
print(a)