n = int(input())
list_num = list(input().split())
s = set(list_num)
'''
    array = set(map(int, input().split()))
    이런 식으로도 입력이 가능하다.
'''
m = int(input())
find_num = list(input().split())
s1 = set(find_num)
'''s1 = list(map(int,input().split()))'''

s2 = s1 & s
#we can use for i in x 
for j in range(0,m):
    if find_num[j] in s2:
        print(1)
    else:
        print(0)

#we can use set, when we need to use hash!!
