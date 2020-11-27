import sys
n=10000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

for num in range(2,10001,2):
    #num = int(input())
    gap = 1000000
    ans = [0,0]
    for data in primes:
        if a[num - data] == True:
            if num - data < data:
                break
            if data > n//2:
                break
            if num - data - data < gap:
                ans[0] = data
                ans[1] = num - data
                gap = num - data -data
    ans_num = num
    ans0, ans1 = ans[0], ans[1]
    ab = str(ans_num)+">>>"+str(ans0)+' '+str(ans1)
    sys.stdout.write(ab+'\n')
