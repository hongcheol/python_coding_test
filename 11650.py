n = int(input())
array = []

for _ in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]),int(input_data[1])))

array = sorted(array,key = lambda x : (x[0],x[1]))

for i in array:
    print(i[0],i[1])
