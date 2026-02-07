# SWEA - 1860
# 진기의 최고급 붕어빵

import sys
sys.stdin = open('taiyaki.txt')

TC = int(input())

for test_case in range(1, TC+1):
    people, sec, piece = map(int, input().split())
    reserve_time = list(map(int, input().split()))

    # 0초부터 sec이 지나면 piece만큼 붕어빵이 만들어지고
    # people 만큼 reserve_time 이 주어지고
    # reserve_time 이 되면 붕어빵이 한 개씩 줄어드는
    # 스택? 큐?

    # 반복 1회를 1초라고 상정
    # 범위 설정이 까다로우니 while 문으로

    reserve_time.sort()
    stop_watch = 0
    taiyaki = 0
    order = 0
    while True:
        pass
        if stop_watch > reserve_time[order]:
            print(f'#{test_case} Impossible')
            break

        stop_watch += 1
        if stop_watch % sec == 0:
            taiyaki += piece

        if stop_watch == reserve_time[order]:
            taiyaki -= reserve_time.count(reserve_time[order])
            order += reserve_time.count(reserve_time[order])

        if taiyaki < 0:
            print(f'#{test_case} Impossible')
            break

        if order > len(reserve_time) - 1:
            print(f'#{test_case} Possible')
            break