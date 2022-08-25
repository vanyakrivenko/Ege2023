A = float(input('A ='))
B = float(input('B ='))
C = float(input('C ='))
AB = abs(A-B)
AC = abs(A-C)
if AB < AC:
    print("В ближе ", AB)
elif AB > AC:
    print("C ближе ", AC)
else:
    print("B и C равноудалены ", AB)