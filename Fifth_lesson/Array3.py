N = int(input())
A = int(input())
D = int(input())

a1 = []
for i in range(N):
    x = A + i*D
    a1.append(x)
a2 = [A + i*D for i in range(N)]


print(a2)