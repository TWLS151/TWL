# SWEA - 5650
# 핀볼 게임

# https://chelseashin.tistory.com/31

# 블럭 5종류 1~5
 # 1. 상우
 # 2. 하우
 # 3. 하좌
 # 4. 상좌
 # 5. 반대
# 웜홀 6~10
 # 같은 숫자로 이동
# 블랙홀 -1
 # 삭제

# DFS 는 아니고 그냥 시뮬레이션
# 분기가 없다.
# 벽이나 블록에 부딪힌 횟수가 점수

import sys
sys.stdin = open('input.txt')

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]
change_dir = ((),
              (1, 3, 0, 2),
              (3, 0, 1, 2),
              (2, 0, 3, 1),
              (1, 2, 3, 0),
              (1, 0, 3, 2))
# 잠깐 생각만 해보고 시도하지 않았던 방법
# rev 하나만 만들었었다. 제발 그냥 생각하면 좀 해보자

def pinball(r, c, d):
    global wormhole_info
    score = 0
    sr, sc, = r, c
    while True:
        dr, dc = dirs[d]
        r += dr
        c += dc

        if (r, c) == (sr, sc) or A[r][c] == -1:
            return score
        if 1 <= A[r][c] <= 5:
            d = change_dir[A[r][c]][d]
            score += 1
        elif 6 <= A[r][c] <= 10:
            r, c = wormhole_info[(r, c)]


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    ## 웜홀을 따로 만들었네
    wormhole_check = [0]*11
    wormhole_info = dict()
    A = [[5] * (N+2)]  # 벽을 만들었다! 5번 블럭이 반대로 가게 하는 블럭

    for i in range(1, N+1):
        A.append([5] + list(map(int, input().split())) +[5])
        for j in range(1, N+1):
            if 6 <= A[i][j] <= 10:
                num = A[i][j]
                if not wormhole_check[num]:  # 처음 보는 번호면
                    wormhole_check[num] = (i, j)  # 새로 등록
                else:  # 아니라면
                    wormhole_info[wormhole_check[num]] = (i, j)
                    wormhole_info[(i, j)] = wormhole_check[num]  # 쌍 연결
    A.append([5] * (N+2))  ## 행 맨 위와 맨 아래는 따로 벽을 치고
    ## 열 양 옆은 인풋 받을때 만들었네
    # 그리고 순회하면서 웜홀 찾으면 기록하고

    MAX = float('-inf')
    for sr in range(1, N+1):
        for sc in range(1, N+1):
            if A[sr][sc] == 0:
                for sd in range(4):
                    MAX = max(MAX, pinball(sr, sc, sd))

    print(f'#{test_case} {MAX}')