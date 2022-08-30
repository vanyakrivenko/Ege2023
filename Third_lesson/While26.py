N = int(input())

F_1 = 1
F_2 = 1
F = 0

while F < N:
    F = F_2 + F_1
    F_2 = F_1
    F_1 = F
print(F_2, F_1 + F_2)