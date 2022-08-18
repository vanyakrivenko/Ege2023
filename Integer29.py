A = int(input())
B = int(input())
C = int(input())
A_Side = A // C
B_Side = B // C
Squares = B_Side * A_Side
Square_all = A*B
White_square = Square_all - C*C*Squares
print(Squares, White_square)

