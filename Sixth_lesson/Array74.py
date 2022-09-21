N = int(input())
a = [int(input("A["+str(i)+"]=")) for i in range(N)]
max_v = max(a)
max_i = a.index(max_v)
min_v = min(a)
min_idx = a.index(min_v)
if min_idx < max_i :
    start_idx = min_idx
    end_idx = max_i
else :
    start_idx = max_i
    end_idx = min_idx
i = start_idx + 1
while i < end_idx :
    a[i] = 0
    i += 1
print(a)