A = int(input())
B = int(input())
n = 1

os = A - B
while os >= B:
    os -= B
    n += 1

print(n)