A=int(input())
if A == 0:
    s = "нулевое "
elif A > 0:
    s = "положительное "
else:
    s = "отрицательное"
if A != 0:
    if A%2 == 0:
        s += "четное число "
    else:
        s += "нечетное число "
print(s)