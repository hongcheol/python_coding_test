import sys
numbers = list()
counter = [0]*8001
sorted_numbers = list()
n = int(input())
hap = 0
for _ in range(n):
    number = int(sys.stdin.readline())
    numbers.append(number)
    counter[number+4000] += 1
    hap += number
print(round(hap/n))

for i in range(8001):
    if counter[i] != 0:
        for _ in range(counter[i]):
            sorted_numbers.append(i-4000)

most = max(counter)
find = 0
ans = 0
i = 0
if n == 1:
    ans = sorted_numbers[0]
else:    
    while i < n:
        if most == counter[sorted_numbers[i]+4000]:
            ans = sorted_numbers[i]
            if find == 1:
                break
            else:
                find += 1
        i += counter[sorted_numbers[i]+4000]

print(sorted_numbers[n//2])
print(ans)
print(sorted_numbers[-1]-sorted_numbers[0])
        


