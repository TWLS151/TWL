# SWEA - 1953
# 탈주범 검거

import sys
sys.stdin = open('input.txt')


from collections import deque

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]
things = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2]
}
oppe = {0:1, 1:0, 2:3, 3:2}

def CanIGoThere(r, c, nr, nc, d):
    if not (0<=nr<N and 0<=nc<M):
        return False
    
    if under[nr][nc] == 0:  
        return False
    
    if oppe[d] not in things[under[nr][nc]]:
        return False
    
    return True


    pass


def bfs(r, c, l):
    global N, M, L, under

    q = deque()
    q.append((r, c, l))

    dist = [[0] * M for _ in range(N)]
    dist[r][c] = 1

    while q:

        pr, pc, l = q.popleft()

        if l == L:
            continue

        for idx in range(4):
            dr, dc = dirs[idx]
            nr, nc = pr+dr, pc+dc

            if CanIGoThere(pr,pc,nr,nc,idx) and dist[nr][nc] == 0:
                q.append((nr,nc,l+1))
                dist[nr][nc] = 1+dist[pr][pc]
    count = 0
    for i in range(N):
        for j in range(N):
            if 1 <= dist[i][j] <= L:
                count += 1
    return count

    pass


T = int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    under = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{test_case} {bfs(R,C,1)}')