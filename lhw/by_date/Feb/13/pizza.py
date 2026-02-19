import sys
from collections import deque

sys.stdin = open('input.txt')
TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    dow_lst = deque([(i + 1, cheese) for i, cheese in enumerate(map(int, input().split()))])
    fire = deque()

    # 집어 넣을때부터 치즈를 반으로 줄이고 넣으려고 시도해봤는데
    # 무의미한 공정만 늘어나는 것 같아 폐기했습니다..

    for _ in range(N):
        if dow_lst:
            fire.append(dow_lst.popleft())

    last_pizza = -1

    while fire:

        idx, cheese = fire.popleft()
        cheese //= 2

        last_pizza = idx

        if cheese > 0:
            fire.append((idx, cheese))

        elif dow_lst:
            fire.append(dow_lst.popleft())

    print(f'#{tc} {last_pizza}')