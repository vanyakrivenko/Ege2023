ax, ay = map(int,input().split())
bx, by = map(int,input().split())
cx, cy = map(int,input().split())
if ax == bx :
    dx = cx
elif ax == cx :
    dx = bx
else :
    dx = ax
if ay == by :
    dy = cy
elif ay == cy :
    dy = by
else :
    dy = ay
print(dx, dy)