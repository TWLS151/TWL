# 기출
# 산악 구조 로봇

# 상태 하나 추가된 BFS 같은 느낌인데

import sys
from collections import deque
import heapq
sys.stdin = open('input.txt')

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def diff(r, c, nr, nc):
    global mountain

    if mountain[nr][nc] - mountain[r][c] < 0:
        return 0

    result = (mountain[nr][nc] - mountain[r][c]) * 2

    return result


def bfs(sr, sc):

    # q = deque([(sr, sc)])
    # dist = [[[-1]*2 for _ in range(N)] for _ in range(N)]
    dist = [[float('inf')]*N for _ in range(N)]
    dist[sr][sc] = 0
    q = [(0, 0, 0)]

    while q:
        cur, r, c = heapq.heappop(q)
        
        if cur != dist[r][c]:
            continue

        if (r, c) == (N-1, N-1):
            return cur

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if 0 <= nr < N and 0 <= nc < N:
                if dist[nr][nc] > dist[r][c]:
                    if mountain[nr][nc] < mountain[r][c]:
                        heapq.heappush(q, (cur, nr, nc))
                        dist[nr][nc] = cur

                    elif mountain[nr][nc] == mountain[r][c]:
                        heapq.heappush(q, (cur + 1, nr, nc))
                        dist[nr][nc] = cur + 1
                    
                    else:  # 연료소모가 더 크면 안가야하는데 가고있다.
                        if dist[nr][nc] > diff(r, c, nr, nc):
                            heapq.heappush(q, (cur + diff(r, c, nr, nc), nr, nc))
                            dist[nr][nc] = cur + diff(r, c, nr, nc)
                
    return dist[N-1][N-1]

    # 프레임은 다 됐는데
    # 이제 연료 상태를 반영해야함.
    # 높이가 낮은 곳으로 가면 안들고
    # 높은 곳으로 가면 높이 차이의 두 배만큼 연료 소모
    # 이러면 dist 를 거리가 아니라 연료로 할까?
    # 어차피 시작점하고 도착점 정해져있으니까
    # 다음 좌표 dist가 지금보다 더 크면 가고 아니면 안가고
    # 마지막에 dist[N][N] 출력.


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    print(bfs(0, 0))