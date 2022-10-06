from sys import stdin
from collections import deque

input = stdin.readline

size = int(input())
que = deque(i for i in range(1, size + 1))

while size != 1:
    que.popleft()
    size -= 1
    que.append(que.popleft())

print(que.popleft())
