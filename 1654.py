k,n = map(int,input().split())
array = []
total = 0
for _ in range(k):
    l = int(input())
    array.append(l)
    total += l
avg = int(total/n)+1
    
start = 0
end = avg
ans = 0
while 1:
    count = 0
    ans = (start+end)//2
    for data in array:
        count += data//ans
    if end-1 <= start:
        break
    elif count == n:
        start = ans
    elif count < n:
        end = ans
    elif count > n:
        start = ans

print(start)
#처음에 문제 풀 때 탈출조건을 잘못 잡아서 무한루프가 돌아버림. 그냥 두개가 같을 때로 잡아주면 되는거였음.
