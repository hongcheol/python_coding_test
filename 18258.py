import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
cnt = 0
for _ in range(n):
    s = list(sys.stdin.readline().split())
    if s[0] == 'push':
        queue.append(s[1])
        cnt += 1
    if s[0] == 'front':
        if queue == []:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(queue[0])
            sys.stdout.write('\n')
    if s[0] == 'back':
        if queue == []:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(queue[cnt-1])
            sys.stdout.write('\n')
    if s[0] == 'pop':
        if cnt == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(queue.popleft())
            sys.stdout.write('\n')
            cnt -= 1
    if s[0] == 'size':
        sys.stdout.write(str(cnt))
        sys.stdout.write('\n')
    if s[0] == 'empty':
        if cnt == 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
