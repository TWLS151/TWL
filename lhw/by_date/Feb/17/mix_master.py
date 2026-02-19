# 기출
# 몬스터 마스터

# DFS
# 몬스터가 음수고 의뢰인이 양수
# 상태가 0이 되면 종료
# 들어가기 전에 몬스터 위치 찾고 리스트 추가하고
# 그 리스트 크기도 0이 되야겠네

import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt')

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def dfs(r, c, total):
    global field, N, trainer, monster

    # 기저조건
    # 지금 토탈값이 0이고 몬스터, 트레이너 리스트가 비어있으면 끝
    if total == 0 and not trainer and not monster:
        return 1

    count = float('inf')
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc

        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                dfs(nr, nc, total+field[nr][nc])
                visited[nr][nc] = False
                if field[nr][nc] > 0:
                    monster.remove((nr, nc))
                    field[nr][nc] = 0
            else:
                if field[nr][nc] < 0 and total + field[nr][nc] >= 0:
                    count = min(count, 1 + dfs(nr, nc, total+field[nr][nc]))
    

    return count
    pass


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    trainer = []
    monster = []
    for r in range(N):
        for c in range(N):
            if field[r][c] < 0:
                trainer.append((r, c))
            elif field[r][c] > 0:
                monster.append((r, c))
        
    print(dfs(0, 0, 0))