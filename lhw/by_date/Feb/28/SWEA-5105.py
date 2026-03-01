# SWEA - 5105
# 미로의 거리

from collections import deque

# import sys
# sys.stdin = open('input.txt')

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    maze = []  # 미로 입력 받을 빈 리스트
    for row in range(N):
        r = list(map(int, list(input())))  # 행 입력을 받고
        for col in range(N):  # 그 행을 순회하며
            if r[col] == 3:  # 종료점과
                er, ec = row, col
                continue  # continue 가 아닌 elif 를 채택하는게 더 좋았겠네요
            if r[col] == 2:  # 시작점을 탐색
                sr, sc = row, col
        maze.append(r)  # 탐색 종료 후 해당 행 리스트에 추가 ( 탐색 전이어도 상관 없음 )

    q = deque([(sr, sc)])
    # visited = [[False]*N for _ in range(N)]
    # visited[sr][sc] = True
    dist = [[0]*N for _ in range(N)]

		#  bfs 시작
    while q:
        r, c = q.popleft()

        if (r, c) == (er, ec):  # 도착하면
            print(f"#{test_case} {dist[r][c] - 1}")  # 도착점 한 칸 빼기
            break  # break

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if 0 <= nr < N and 0 <= nc < N \
            and dist[nr][nc] == 0 \
            and maze[nr][nc] != 1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    else:  # q가 빌때까지 break 가 잡히지 않았다면 실패. 0 출력
        print(f"#{test_case} 0")