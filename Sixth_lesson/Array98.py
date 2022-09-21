N = int(input())
a = [int(input("A["+str(i)+"]=")) for i in range(N)]
i = 0
while i < len(a):
    x = a[i]
    k = 0
    for y in a:
        if x == y:
            k += 1
    if k < 3:
        f = True
    else:
        i += 1

print(a)
print(len(a))