n, index = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

print(array[index-1])
