mini, maxi = map(int, input().split())
a = [False,False] + [True]*(maxi-1)
prime = []
count = 0
for i in range(mini,maxi+1):
    if a[i]:
        prime.append(i)
        for j in range(2*i,maxi+1,i):
            a[j] = False
print(prime)
high = 0
low = 0
total = 0
for data in prime:
    high = maxi//(data**2)
    low = mini//(data**2)
    total += high-low

print(maxi-mini+1-total)
