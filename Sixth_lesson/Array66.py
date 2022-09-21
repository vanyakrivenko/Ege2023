N = int(input())
a = [int(input("A["+str(i)+"]=")) for i in range(N)]
x_e = None
for it in a :
    if it % 2 == 0:
        x_e = it
        break
for (i, it) in enumerate(a):
    if it % 2 == 0:
        a[i] += x_e
print(a)

