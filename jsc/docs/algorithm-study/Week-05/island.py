# ===BFS===
import sys
from collections import deque

sys.stdin = open('island.txt')

N, M = map(int, input().split())


# 인풋이 숫자들이 공백이 없는 상태로 들어와있다.
# 원래는 array = list(map(int, input().split()) for _ in range(N))
# 을 쓸텐데
# 지금은 for문을 돌리면서 받아야한다.
# 그런데 리스트 컴프리헨션으로 받고 싶다. 멋있으니깐
# map은 두번째 인자로 들어온것을 한글자씩 순회를 한다.
array = [list(map(int, input())) for _ in range(N)]
# 방문 이차원 배열 생성
visited = [[False] * M for _ in range(N)]

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

# 섬의 개수를 출력을 해야한다.
# BFS를 한다면 데크를 받아서 방문 정리를 해야한다.
# 이차원 리스트에서 각 셀의 방문하면서 체크를 해야한다. 그런데 이미 visited라는 곳은 빼고 돌아야
# 하는데 따라서 while문으로 하는게 더 좋아보인다. for문보다
# BFS가 DFS가 좋다라고 생각한 이유? -> 지금 생각해보니 좋은거는 잘 모르겠다.
# 다만 이전에 다리 만들기2 문제를 풀 때 BFS가 최선이라고 해서 이 문제에도 BFS가 좋을 거라고 생각했다.
# BFS설계는 좌표만 파라미터를 넣는다.
# 일단 이차원 리스트는 무조건 격자에 있는지 체크해야함
# 방문 한지도 체크르 해야함

def bfs():
    count = 0
    
    for r in range(N):
        for c in range(M):
            if array[r][c] == 1 and not visited[r][c]:
                count += 1
                
                queue = deque([(r, c)])
                visited[r][c] = True
                
                while queue:
                    curr_r, curr_c = queue.popleft()
                    
                    for i in range(8):
                        nr, nc = curr_r + dr[i], curr_c + dc[i]
                        
                        if 0 <= nr < N and 0 <= nc < M and array[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
    print(count)

bfs()