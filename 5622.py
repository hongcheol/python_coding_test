string = input()
ans = 0
for data in string:
    temp = ord(data)-65
    if temp > 14 and temp < 19:
        ans += 8
    elif temp > 18 and temp < 22:
        ans += 9
    elif temp > 21 and temp <26:
        ans += 10
    else:
        ans += temp//3
        ans+=3
print(ans)
