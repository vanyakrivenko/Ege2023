N = int(input())
A = 2
B = 1
C = 2
while abs(A - B) >= N:
    F = B
    B = A
    C += 1
    A = (F+2*B)/3
print(C,A,B)