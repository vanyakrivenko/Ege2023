import math

cathetus_1 = int(input())
cathetus_2 = int(input())

hypotenuse = math.sqrt(cathetus_1 ** 2 + cathetus_2 ** 2)
perimeter = cathetus_1 + cathetus_2 + hypotenuse

print(hypotenuse, perimeter)
