import math

x_1, y_1 = map(float,input().split())
x_2, y_2 = map(float,input().split())
x_3, y_3 = map(float,input().split())

AB = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
AC = math.sqrt((x_3 - x_1)**2 + (y_3 - y_1)**2)
BC = math.sqrt((x_3 - x_2)**2 + (y_3 - y_2)**2)
perimeter = AB + AC + BC
half_per = perimeter / 2
square = math.sqrt(half_per * (half_per - AB) * (half_per - AC) * (half_per - BC))

print(square, perimeter)
