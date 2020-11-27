n = int(input())
dots = []
for _ in range(n):
    dot = list(map(int,input().split()))
    dots.append(dot)


dots.sort()
dots = sorted(dots,key = lambda x : x[1])
for data in dots:
    print(data[0],data[1])
