import sys
input = sys.stdin.readline


que = []

for i in range(int(input())):
    required = input().split()

    if required[0] == 'push':
        que.append(int(required[1]))

    elif required[0] == 'pop':
        try:
            print(que.pop(0))
        except:
            print(-1)

    elif required[0] == 'size':
        print(len(que))

    elif required[0] == 'empty':
        print(1 if len(que) == 0 else 0)

    elif required[0] == 'front':
        try:
            print(que[0])
        except:
            print(-1)

    elif required[0] == 'back':
        try:
            print(que[-1])
        except:
            print(-1)
