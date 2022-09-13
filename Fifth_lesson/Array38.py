N = int(input())
A = [int(input("A["+str(i)+"]=")) for i in range(N)]


result = 0
count = 0
for j in range(len(A)-2):
    if A[j+2] > A[j+1] > A[j]:
        count += 1
    elif count >= 1 and A[j+1] > A[j+2]:
        result += 1
        count=0
if A[-1] > A[-2] > A[-3]:
    result += 1
print(result)
