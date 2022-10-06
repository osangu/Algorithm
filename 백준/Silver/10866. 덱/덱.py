from sys import stdin
from collections import deque

input = stdin.readline
que = deque()
size = 0

for i in range(int(input())):

    req = input().rstrip()

    if req == 'pop_front':
        if size > 0:
            print(que.popleft())
            size -= 1
        else:
            print(-1)

    elif req == 'pop_back':
        if size > 0:
            print(que.pop())
            size -= 1
        else:
            print(-1)

    elif req == 'size':
        print(size if size > 0 else 0)

    elif req == 'empty':
        print(0 if size > 0 else 1)

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
        req, value = req.split()

        if req == 'push_front':
            que.insert(0, value)
            size += 1
        else:
            que.append(value)
            size += 1

