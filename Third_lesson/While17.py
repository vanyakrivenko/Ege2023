N = int(input())

q = N
while q >= 1:
    r = q % 10
    print(r)
    q = int(q/10)