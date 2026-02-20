"""
Docstring for TWL.jsc.docs.algorithm-study.Week-04.boj-17472
3줄요약
1. BFS를 이용한 섬 구분
2. 다리 후보들 생성
3. 최솟값 구분

문제설명
각 섬들을 지정을 먼저 하고 그 다음에 섬들을 연결을 해서 최소비용으로 섬을 구하는 문제

문제 유형
BFS, 시뮬레이션, MST

문제 풀이
1. 각 섬을 구분을 해서 숫자 매긴다.
2. 가능한 다리들을 모두 리스트에 넣어둔다.
3. 크루수칼 알고리즘으로 최소신장 트리를 찾느다.
이러면 될듯?

상세 풀이
#  1. BFS를 통해서 섬을 발견을 하면 그 지점부터 델타 이동을 사용을 함.
다시 찾은 셀은 큐에 넣어둔 이후 큐에서 하나씩 꺼내면서 다시 상하좌우를 탐색
찾으면 큐에 넣는것을 큐가 없어질때까지 반복
찾으면 해야하는 일은 visited에 True로 바꾸기, board에 섬 넘버로 바꾸기, 큐에 현재 위치 nr,nc넣어주기
#  2. 가능한 다리들을 while문과 델타이동을 이용을 해서 사용
parent-union을 사용을 해서 내가 만난 섬이 나랑 같은지 아닌지를 판단
맞으면 다리 카운트를 1증가
이후 다리의 수가 섬의 수 - 1가 맞는지 확인

알게 된 내용
1. 섬의 내부에서 출발을 하면 의미가 없으니 이것을 예외 처리를 할려고 했다.
하지만 이것을 예외처리를 하는것보다 그냥 자기섬이 다음에 나오면 빼라 이런식으로
코드를 짜는게 더 효율적으로 짤 수 있다는 것을 배움.
2. While True:
While뒤에 정지 조건을 쓰는게 당연하다고 생각을 했는데 뒤에 True를 쓰고
그 아래에 if문들을 여러개를 쓰고 break를 쓴다면 각각의 상황에서 내가 원하는 곳에서
멈출 수 있다는 사실을 알게 되었다. while뒤에 조건을 여러개를 쓸려면 쓸 수는 있지만
그러면 멈춘 이후에 왜 멈췄는지 또 파악을 해야한다.
3. parent, union을 이용을 해서 연결된지 아닌지를 판단
4. 객체참조(reference)때문에 list는 함수내에서 조작을 해도 return에 반환하지 않아도 됨.
하지만 불변인 숫자 데이터같은것들은 return을 해야 사용가능
5. 하지만 아무리 리스트라고 하더라도 함수 내에서 선언이 된거는 return을 해야한다.
6. def안에 if문과 return을 두개를 써서 if-else문처럼 쓸 수가 있다.

"""
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 1. island labeling
def label_islands():
    visited = [[False] * M for _ in range(N)]
    island_num = 0

    for r in range(N):
        for c in range(M):

            if board[r][c] == 1 and not visited[r][c]:
                island_num += 1
                queue = deque([(r,c)])
                visited[r][c] = True
                board[r][c] = island_num

                while queue:
                    curr_r, curr_c = queue.popleft()
                    for i in range(4):
                        nr, nc = curr_r + dr[i], curr_c + dc[i]
                        if 0 <= nr < N and 0 <= nc < M:
                            if board[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                board[nr][nc] = island_num
                                queue.append((nr, nc))
    return island_num

# 2. 다리 찾기
def get_bridges():
    bridges = []
    for r in range(N):
        for c in range(M):
            if board[r][c] > 0:
                curr_island = board[r][c]
                for i in range(4):
                    dist = 0
                    nr, nc = r + dr[i], c + dc[i]

                    while True:
                        if not (0 <= nr < N and 0 <= nc < M):
                            break
                        if board[nr][nc] == curr_island:
                            break
                        if board[nr][nc] == 0:
                            nr += dr[i]
                            nc += dc[i]
                            dist += 1
                        else:
                            if dist >= 2:
                                bridges.append((dist, curr_island, board[nr][nc]))
                            break
    return bridges

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
        return True
    return False

# 4. main logic 실행
def solve():
    num_islands = label_islands()
    all_bridges = get_bridges

    all_bridges.sort()

    parent = [i for i in range(num_islands + 1)]
    total_dist = 0
    bridge_count = 0

    for d, s, e in all_bridges:
        if union(parent, s, e):
            total_dist += d
            bridge_count += 1

        if bridge_count == num_islands - 1 and num_islands > 0:
            print(total_dist)
        else:
            print(-1)

    
solve()