# SWEA - 1953
# 탈주범 검거

import sys
from collections import deque

sys.stdin = open('z.txt')

# # 탈주범은 시간당 1의 거리 이동 가능
# # 지하는 총 7 종류의 구조물이 존재

# # 유형 : DFS
# # 상태 : 좌표, 시간
# # 반환 : count = 1 + 재귀
# # 기저조건 : 거리 : t

# directions = [
#     (-1, 0), (1, 0), (0, -1), (0, 1)
# ]

# things = {
#     1: [0, 1, 2, 3], # 상하좌우,
#     2: [0, 1], # 상하,
#     3: [2, 3], # 좌우,
#     4: [0, 3], # 상우,
#     5: [1, 3], # 하우,
#     6: [1, 2], # 하좌,
#     7: [0, 2] # 상좌
# }
# # 진행하다가 0이 아닌 값을 만나면 
# # 그 값을 딕셔너리에 넣고 그걸 델타 인덱스 값으로 쓰면 되지 않을까
# # if not 0:
# #     for idx in things[field[r][c]]:
# #         for dr, dc in directions[idx]:
# # 될듯?


# def Possiblity(r, c, time):
#     # print(f'나 여기야 {r, c, tizu[r][c], time}')
#     if time == L:
        
#         return 1  # 시간 다 됐으니까 해당 위치 카운트만 반환
    
#     # 할 일
#     # 시작점 주어졌고 이제 움직인다.
#     # 1. 값이 0인 지점은 갈 수 없다.
#     # 2. 위치의 값에 따라 움직일 수 있는 방향이 달라진다.
#     # 3. DFS 로 반환은 갈 수 있는 방의 총 개수
    
#     count = 1  # 이 위치 카운트 값

#     visited[r][c] = True  # 방문 처리 먼저

#     # t = time + 1  # 시간 계산

#     for idx in things[tizu[r][c]]:  # tizu[r][c] 는 구조물 번호
#         dr, dc = directions[idx]  # idx 는 구조물 번호에 따라 갈 수 있는 방향의 인덱스 번호
#         nr, nc = r + dr, c + dc
#         if 0 <= nr < N \
#         and 0 <= nc < M \
#         and tizu[nr][nc] != 0 \
#         and not visited[nr][nc]:  # 필드 안이고 값이 0이 아니고 방문한 적이 없다면
#             count += Possiblity(nr, nc, time+1)  # 이동하고 반환값을 카운팅
    
#     # visited[r][c] = False  # 백트래킹 // 필요없나? 

#     return count  # 이러면 카운트는 지금까지 들린 방의 수가 된다.


# TC = int(input())

# for test_case in range(1, TC+1):
#     N, M, R, C, L = map(int, input().split())
#     # 터널 지도의 행, 열, 진입 포지션의 행, 열, 총 시간

#     tizu = [list(map(int, input().split())) for _ in range(N)]
#     # 방문처리 필요하다.
#     visited = [[False]*M for _ in range(N)]

#     # 구조물 딕셔너리랑 델타 만들어와야곘네
#     # 만들었고
#     # 도둑 위치, 이 위치는 1초의 위치
#     pos = (R, C)

#     # # 준비는 다 한 것 같으니 시작
#     # for row in range(N):
#     #     for col in range(M):
#     #         if row == R and col == C:  # 위치에 도착하면.. # 그냥 바로 함수에 넣으면?
#     #             pass

#     print(f'#{test_case} {Possiblity(R, C, 1)}')  # 현재 위치와 시간


# # --------------- DFS 실패 --------------- #
# # --------------- BFS 전환 --------------- #

# # BFS 구현 실패해서 AI 도움 받음 #

# directions = [
#     (-1, 0), (1, 0), (0, -1), (0, 1)
# ]

# things = {
#     1: [0, 1, 2, 3], # 상하좌우,
#     2: [0, 1], # 상하,
#     3: [2, 3], # 좌우,
#     4: [0, 3], # 상우,
#     5: [1, 3], # 하우,
#     6: [1, 2], # 하좌,
#     7: [0, 2] # 상좌
# }  # 밸류 값을 list로 설정해도 이 문제에서는 아무 상관 없지만 순서가 필요 없이 그냥 있는지 없는지만 확인할 때는
#    # list가 아니라 set를 활용하는게 좋다는 의견

# # 반대 방향 인덱스 (상하, 좌우)
# oppo = {0: 1, 1: 0, 2: 3, 3: 2}

# def can_move(tizu, N, M, r, c, nr, nc, d):
#     '''(r, c) 에서 방향 d로 (nr, nc)로 이동이 가능한지. ( 둘이 연결되어 있는지 판별 )'''
#     # 왜 if 문 하나를 따로 함수로 만들어뒀지 싶었는데 밑의 핵심이라고 표시해둔 부분이 이유였음

#     if not (0 <= nr < N and 0 <= nc < M):
#         return False  # 맵 밖이면 불가
#     if tizu[nr][nc] == 0:
#         return False  # 벽이면 불가

#     cur_type = tizu[r][c]
#     nxt_type = tizu[nr][nc]

#     if d not in things[cur_type]:
#         return False
#     ##### 핵심 #####
#     if oppo[d] not in things[nxt_type]:
#         return False
#     ###############
#     # 길이 연결되어 있는지 판별해야함. 위의 DFS 코드도 그렇고 새로 작성한 BFS 도 그렇고 다음 길의 값이 0 만 아니면 들어갈 수 있게 해두어서
#     # 사실 연결되어 있지 않아도 그냥 뚫어버리는 문제가 있었음
#     # 반대 방향 인덱스를 사용할 수 있게 정의해서 판단할 수 있음
#     # 그리고 list 간의 in 연산자 사용도 가능하다는 걸 배웠음

#     return True

# def solve(tizu, N, M, R, C, L):
#     if tizu[R][C] == 0:
#         return 0
    
#     dist = [[0] * M for _ in range(N)]
#     dist[R][C] = 1

#     q = deque()
#     q.append((R, C))

#     while q:
#         r, c = q.popleft()

#         if dist[r][c] == L:
#             continue

#         cur_type = tizu[r][c]
#         for d in things[cur_type]:
#             dr, dc = directions[d]
#             nr, nc = r + dr, c + dc

#             if can_move(tizu, N, M, r, c, nr, nc, d) and dist[nr][nc] == 0:
#                 dist[nr][nc] = dist[r][c] + 1
#                 q.append((nr, nc))

#     ans = 0
#     for r in range(N):
#         for c in range(M):
#             if 1 <= dist[r][c] <= L:
#                 ans += 1

#     return ans


# TC = int(input())

# for test_case in range(1, TC+1):
#     N, M, R, C, L = map(int, input().split())

#     tizu = [list(map(int, input().split())) for _ in range(N)]
    
#     print(f'#{test_case} {solve(tizu, N, M, R, C, L)}')


'''
1. 반대 방향에서 들어오는 걸 체크하지 않았다. ( 길이 연결되어 있는지를 확인 안했다. )
 # 기본적으로 문제 유형을 잘못 판단하긴 했지만 그를 떠나서 그래프 간의 간선 방향이 존재하는지를 확인 했어야헀다. 
 # 이렇게 되면 만약 DFS 문제였다고 하더라도 문제 해결에 장애가 되었을 것.

2. BFS 문제인 점을 놓쳤다.
 # BFS 와 DFS 를 구분하는 연습이 필요하다.

3. BFS 코드 작성에 실패했다.
 # BFS 개념 공부 또한 필요하다. 처음 코드를 작성하며 힘들었던 점은
 # "'시간'을 어떻게 관리해야하지" 였는데 AI 코드를 보니 어느정도 감이 왔다.
 # 방문처리를 하듯이, 메모리제이션을 하듯이 기록하는 느낌인 것 같다. 이 부분은 연습이 필요하다.
'''

'''
DFS, BFS 판단 기준 (대부분 맞음)

1. DFS
 - 모든 경로 탐색
 - 조합 / 백트래킹
 - 경로 수 세기
 - 완전 탐색
 - 조건 만족하는 경우 찾기

2. BFS
 - 최소 이동 횟수
 - 최단 거리
 - 시간당 이동
 - 몇 초 안에 도달
 - 거리 <= K 인 정점 개수
'''

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

things = {
    1: {0, 1, 2, 3},
    2: {0, 1},
    3: {2, 3},
    4: {0, 3},
    5: {1, 3},
    6: {1, 2},
    7: {0, 2}
}

oppo = {0: 1, 1: 0, 2: 3, 3: 2}

def canGo(row, col, nr, nc, d):

    if not (0 <= nr < n and 0 <= nc < m):
        return False
    
    if tizu[nr][nc] == 0:
        return False
    # if d not in things[tizu[row][col]]:
    #     return False
    ##### 핵심 #####
    if oppo[d] not in things[tizu[nr][nc]]:
        return False
    ###############

    return True


def itachi(L, n, m, r, c):


    q = deque()
    q.append((r, c))

    dist = [[0]*m for _ in range(n)]
    dist[r][c] = 1

    while q:
        row, col = q.popleft()

        '''
        if dist[r][c] == L:
            continue
        '''

        for d in things[tizu[row][col]]:
            dr, dc = directions[d]
            nr, nc = row + dr, col + dc

            if canGo(row, col, nr, nc, d) and dist[nr][nc] == 0:  # dist[nr][nc] == 0 
                q.append((nr, nc))
                dist[nr][nc] = dist[row][col] + 1  # dist[nr][nc] = dist[r][c] + 1
    
    result = 0
    for i in range(n):
        for j in range(m):
            if 1 <= dist[i][j] <= L:
                result += 1

    return result


T = int(input())
for tc in range(1, T+1):
    n, m, r, c, l = map(int, input().split())
    tizu = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{tc} {itachi(l, n, m, r, c)}')