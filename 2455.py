saram = 0
maxi = 0
for _ in range(4):
    nae,ta = map(int,input().split())
    saram -= nae
    saram += ta
    if saram > maxi:
        maxi = saram

print(maxi)
