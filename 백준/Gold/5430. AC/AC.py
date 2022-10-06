from sys import stdin
from collections import deque

input = stdin.readline

for sequence in range(int(input())):
    answer = ''

    command_line = input().rstrip()
    size = int(input())
    list_instance = input().rstrip()[1:-1]

    deq = deque(map(int, list_instance.split(',') if list_instance != '' else []))

    D_amount = command_line.count('D')  # TODO
    R_amount = command_line.count('R')

    is_not_reversed = True

    if D_amount > size:
        print('error')
        continue

    for i in command_line:

        if i == 'D':
            size -= 1

            if is_not_reversed:
                deq.popleft()

            else:
                deq.pop()

        elif i == 'R':
            is_not_reversed = not is_not_reversed

    if R_amount % 2:
        deq.reverse()

    print('[',end='')
    
    for i in deq: answer += str(i) + ','

    print(answer[0:-1]+']')
