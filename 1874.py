n = int(input())
count = 1
stack = []
answer = []
avail = 1
for i in range(1,n+1):
    num = int(input())
    while count <= num:
        stack.append(count)
        count += 1
        answer.append('+')
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        avail = 0
        

if avail == 1:
    print('\n'.join(answer))
else:
    print('NO')
