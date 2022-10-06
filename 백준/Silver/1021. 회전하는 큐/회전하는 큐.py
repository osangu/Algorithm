from sys import stdin
from collections import deque

input = stdin.readline

size, pop_amount = map(int, input().split())
targets = list(map(int, input().split()))

deq = deque(i for i in range(1, size + 1))
answer = 0

for target in targets:
    if target == deq[0]:
        deq.popleft()
        size -= 1

    else:
        before = deq.index(target)  # 36번 라인 주석 참고
        after = size - before

        if before <= after:  # 49번 라인 주석 참고
            for i in range(before):
                deq.append(deq.popleft())
                answer += 1

        elif after < before:
            for i in range(after):
                deq.insert(0, deq.pop())
                answer += 1

        deq.popleft()
        size -= 1

print(answer)

'''
    index를 통해서 얻는 before는 자기 자신을 제외한 값
    
    size - before를 통해서 구하는 after는 자기 자신을 포함한 값이다.
    
    여기서 자기 자신을 제외시키기 위해 size - before - 1을 하게 되면, 해당 수가 맨 마지막에 오게 된다
    
    ex) 
        6을 찾아야 하는데 아래와 같이 오게 되는 것이다
        10 9 8 7 1 2 3 4 5 6
'''

'''
10 1 3 4 5 6 7 8에 target = 5일 경우
5의 인덱스 = 4
before = 5의 인덱스 = 4
after = size - before = 8 - 4 = 4가 된다

하지만 4가 맨앞에 오기 까지 문제에 적힌
2번 연산은 3번 실행
3번 연산은 4번 실행 해야 된다.

따라서 2번 연산에 =를 넣는게 맞는 판단이다.
'''
