n = int(input())

array1 = [0]*n
for _ in range(n):
    array2 = list(map(int,input().split()))
    for i in range(len(array2)):
        if i == 0:
            array2[i] += array1[i]
        elif i == len(array2)-1:
            array2[i] += array1[i-1]
        else:
            array2[i] += max(array1[i],array1[i-1])
    array1 = array2
    print(array1)
print(max(array2))
