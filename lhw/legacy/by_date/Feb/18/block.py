# SWEA - 5656
# 벽돌 깨기
import sys
from collections import deque
import copy
sys.stdin = open('input.txt')

dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def shoot(col):
    global q

    # 1) 맞는 첫 벽돌 찾기 (위에서부터 찾기 → index H-1 ~ 0)
    target = -1
    for i in range(H-1, -1, -1):
        if q[col][i] != 0:
            target = i
            break
    if target == -1:
        return  # 아무것도 안 맞음

    # 2) BFS 폭발
    visited = [[False]*H for _ in range(W)]
    dq = deque()
    dq.append((col, target))
    visited[col][target] = True

    while dq:
        c, r = dq.popleft()
        power = q[c][r]
        q[c][r] = 0  # 바로 제거

        for dist in range(1, power):
            for dc, dr in dirs:
                nc, nr = c + dc*dist, r + dr*dist
                if 0 <= nc < W and 0 <= nr < H:
                    if q[nc][nr] != 0 and not visited[nc][nr]:
                        visited[nc][nr] = True
                        dq.append((nc, nr))

    # 3) 중력 처리 (열마다 아래로 당기기)
    for c in range(W):
        new_col = [v for v in q[c] if v != 0]
        while len(new_col) < H:
            new_col.append(0)
        q[c] = new_col


def dfs(shot):
    global minmain, q

    # 남은 벽돌 수 계산
    remain = 0
    for c in range(W):
        for r in range(H):
            if q[c][r] != 0:
                remain += 1

    if remain == 0:
        minmain = 0
        return

    if shot == N:
        minmain = min(minmain, remain)
        return

    if minmain == 0:
        return

    # 매 샷마다 열 선택
    for col in range(W):
        backup = copy.deepcopy(q)
        shoot(col)
        dfs(shot + 1)
        q = backup


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    pre = [list(map(int, input().split())) for _ in range(H)]

    # 열 기준으로 뒤집어서 저장 (아래가 index 0)
    field = list(map(list, zip(*pre)))
    q = []
    for col in field:
        q.append(list(reversed(col)))

    minmain = 10**9
    dfs(0)

    print(f"#{tc} {minmain}")


# ------------------------------------------- #
# ------------------------------------------- #
# ------------------------------------------- #
# ------------------------------------------- #
# ------------------------------------------- #
# ------------------------------------------- #

# SWEA - 5656
# 벽돌 깨기

# import sys
# from collections import deque
# import copy
# sys.stdin = open('input.txt')

# dirs = [
#     (-1, 0), (1, 0), (0, -1), (0, 1)
# ]

# def shoooot(pos):
#     # 지금 자리에서 쐈을 때 부서지는 벽돌의 좌표를 구하는 함수
#     # 중력처리까지 해버려야함
#     # 데크로 만들어뒀으니 중력처리는 신경안쓰고
#     # 개수가 H 될때까지 0 밀어넣기

#     brick_lst = deque()
    
#     # 지금 위치의 기둥의 마지막 인덱스
#     for i in range(len(q[pos])-1, -1, -1):  # 거꾸로 훑으면서
#         if i != 0:  # 블럭을 찾으면
#             brick_lst.append((pos, i))  # 처음 부서지는 블럭
#             break

#     # 연쇄작용
#     # 새 함수?
#     # bfs?
#     visited = [[False] * H for _ in range(W)]
#     result = []
#     while brick_lst:
#         pos, idx = brick_lst.popleft()
#         # visited[pos][idx] = True

#         step = q[pos][idx]

#         for i in range(step):
#             for dr, dc in dirs:
#                 pos, idx = pos+dr*i, idx+dc*i

#                 if 0<= pos < W and 0 <= idx < H:
#                     if q[pos][idx] != 0 and not visited[pos][idx]:
#                         brick_lst.append((pos, idx))
#                         visited[pos][idx] = True
#                         result.append((pos, idx))

#     return result


# def dfs(pos, t):
#     global q, minmain
#     # 기저조건
#     # 횟수 다쓰면 끝 # 끝까지 닿으면 끝
#     if t == 4 or pos == len(q):
#         a = 0
#         for r in q:
#             a += r.count(0)
#         remain = H * W - a
#         if minmain > remain:
#             minmain = remain
#         return

#     # 할 일
#     # 쏘고 부수고 밑으로 밀어 넣고

#     # 분기
#     # 지금 자리에서 안쏘고 넘어가기
#     # 지금 자리 쏘고 넘어가기
#     # 지금 자리 쏘고 안넘어가기

#     # 안쏜당
#     dfs(pos + 1, t)
    
#     # 쏜다 !!
    
#     backup = copy.deepcopy(q)
#     for r, c in shoooot(pos):
#         q[r].pop(c)

#     for r in q:
#         while len(r) == H:
#             r.append(0)


#     dfs(pos + 1, t + 1)

#     q = backup

#     # 쏜다 !!
    
    
#     backup = copy.deepcopy(q)
#     for r, c in shoooot(pos):
#         q[r].pop(c)

#     for r in q:
#         while len(r) == H:
#             r.append(0)


#     dfs(pos, t + 1)

#     q = backup

#     # 백트래킹 해야하네
#     # 함수 하나 짜서 부서지는 곳 리스트 받아오기



# TC = int(input())
# for test_case in range(1, TC+1):
#     N, W, H = map(int, input().split())
#     pre = [list(map(int, input().split())) for _ in range(H)]

#     field = list(map(list, zip(*pre)))
#     last = []
#     for i in range(len(field)):
#         last.append(list(reversed(field[i])))
#     q = deque(last)
#     # 전처리 끝

#     minmain = 10 ** 7

#     dfs(0, 0)

#     print(minmain)