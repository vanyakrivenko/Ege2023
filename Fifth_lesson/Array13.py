N = 2 * int(input())
A = [int(input("A["+str(i)+"]=")) for i in range(N)]

x = N - 1
while x >=0 :
    print((x, A[x]))
    x -= 2