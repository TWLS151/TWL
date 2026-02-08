# SWEA - 1220
# Magnetic
# TTP: 23'38"

import sys
sys.stdin = open('magnetic.txt')

for test_case in range(1, 11):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(100)]

    # 파랑색은 위쪽으로
    # 빨간색은 아래쪽으로
    # 필드 밖으로 나가면 삭제
    # 1은 빨강색
    # 2는 파랑색
    # 자력을 걸었을 때 다른 색끼리 위아래로 붙어있는 경우의 개수 구하기

    # 필드 밖으로 나가면 삭제를 어떻게 구현하지
    # 일단 교착상태를 구해야하니까 전부 다 같이 움직여야하고
    # 아마 홀수만큼 떨어져있는 경우는 없나본 있네
    # 그럼 시뮬레이션을 돌릴 필요는 없네
    # 위 아래로 탐색하다가 반대가 있으면 counting
    # 1만 확인하면 되는구나
    # 1을 아래로 내리다가 2가 있으면 count += 1
    # 1을 만나면 방문처리
    # 아무것도 안만나도 방문처리

    # 0. 완전탐색, 순회
    # 1. 빨간색 (1) 을 아래로 내린다
    # 2. 내려가다가 2를 만나면 count += 1
    # 3. 내려가다가 1을 만나면 continue
    # 4. 아무것도 못만나도 continue
    # 방문처리는 필요 없음

    count = 0
    for row in range(100):
        for col in range(100):
            if mag[row][col] == 1:
                drow = row + 1
                # 아래로 내린다. row + 1
                # while 문으로 처리하자
                while drow < 100:
                    
                    # 2 만나면 카운팅 후 브레이크
                    if mag[drow][col] == 2:
                        count += 1
                        break
                    # 1 만나면 브레이크
                    elif mag[drow][col] == 1:
                        break
                    # 아무것도 못만나면 계속 내려감
                    else:
                        drow += 1
                        continue
    print(f'#{test_case} {count}')