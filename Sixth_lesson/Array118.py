N = int(input())
a = [int(input("A["+str(i)+"]=")) for i in range(N)]
k = 0
for x in a:
    if x < 0 or x >= 0:
        k += 1
a.extend([0]*k)
j = 0
for i in range(N-1, -1, -1):
    if a[i] < 0 or a[i] >= 0:
        a[(N+k-1)-j] = 0
        j += 1
    a[(N+k-1)-j] = a[i]
    j += 1

print(a)