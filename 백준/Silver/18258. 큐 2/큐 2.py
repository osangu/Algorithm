from sys import stdin
from collections import deque

input = stdin.readline
que = deque()
size = 0

for i in range(int(input())):
    req = input().rstrip()

    if req == 'pop':
        if size > 0:
            print(que.popleft())
            size -= 1
        else:
            print(-1)

    elif req == 'size':
        print(size)

    elif req == 'empty':
        print(1 if 0 == size else 0)

    elif req == 'front':
        if size > 0:
            print(que[0])
        else:
            print(-1)

    elif req == 'back':
        if size > 0:
            print(que[-1])
        else:
            print(-1)

    else:
        value = req.split()[1]
        que.append(value)
        size += 1
