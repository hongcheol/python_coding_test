mini,maxi = map(int,input().split())

maxi_sqrt = int(maxi**0.5)

find = [False]*1000000
div_num = [0]
pow_array = []
count = 0
i = 2
while i*i <= maxi:
    pow_array.append(i**2)
    find[i**2] = True
    count += 1
    i += 1

for number in pow_array:
    j = 2
    while number*j < maxi:
        find[number*j] = True
        j+=1
pow_yes = 0
for i in range(mini,maxi+1):
    if find[i] == True:
        pow_yes += 1


pow_no = maxi-mini+1-pow_yes
print(pow_no)
        
