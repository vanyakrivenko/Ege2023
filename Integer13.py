x = int(input('Введите трёхзначное число:'))
Last_sign = x % 100
First_sign = x//100
Final_sign = First_sign + Last_sign * 10
print(Final_sign)
