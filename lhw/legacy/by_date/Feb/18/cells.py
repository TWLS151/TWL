# SWEA - 5653
# 줄기세포배양

# 시뮬레이션

# 미생물 격리처럼하면 될 것 같은데

# *활성화된* 줄기 세포는 첫 한 시간 동안 네 방향으로 동시 번식
# == 활성화되면 네 방향 번식
# 번식되면 비활성 상태
# 둘 이상의 세포가 하나의 셀에 동시번식하려하면
# 생명력 수치가 가장 높은 세포가 먹는다.

# r, c, 생명력, 생명력 * 2
# 시간마다 3번 인덱스를 1씩 깎다가
# 2번과 3번 인덱스의 값이 같아지면 번식
# 3번 인덱스가 0이 되면 죽은 세포

# 번식은 좌표만 바뀌고 생명력은 그대로

# 0. 매 시간마다 3번 인덱스가 0이 아니라면 깎는다
# 1. 번식
# 2. 충돌 처리
# 3. 3번 인덱스 > 0 인 개수 출력

import sys
sys.stdin = open('input.txt')

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]


TC = int(input())
for test_case in range(1, TC+1):
    N, M ,K = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]

    cells = []
    visited = {}
    for i in range(N):
        for j in range(M):
            if field[i][j] != 0:
                cells.append([i, j, field[i][j], field[i][j]*2])
                visited[(i, j)] = True
                # cells[(i, j)] = [field[i][j], field[i][j]*2]
    
    for _ in range(K):  # K 시간 반복

        v = {}
        for idx in range(len(cells)):
            cells[idx][3] -= 1
            r, c, seki, life = cells[idx]
            
            if life == seki:
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if (nr, nc) not in visited:
                        if (nr, nc) not in v:
                            v[(nr, nc)] = [seki, seki*2]
                        else:
                            if v[(nr, nc)][0] <= seki:
                                v[(nr, nc)][0] = seki
                                v[(nr, nc)][1] = seki * 2
        
        for (r, c), (seki, life) in v.items():
            cells.append([r, c, seki, life])

    count = 0
    for _, _, _, life in cells:
        if life > 0:
            count += 1

    print(f'#{test_case} {count}')





        # for r, c in cells:
        #     for seki, life in cells[(r, c)]:
        #         life -= 1
        #         if life == seki:
        #             for dr, dc in dirs:
        #                 nr, nc = r+dr, c+dc
        #                 if (nr, nc) in cells:
        #                     continue
        #                 else:
        #                     v[(nr, nc)] = seki