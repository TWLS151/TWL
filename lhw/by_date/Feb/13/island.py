import sys
sys.setrecursionlimit(10**7)

# 다시 쓸 일이 없는 지도니까 방문처리 하지 않고 그냥 원본을 바꿔봤습니다.
# 배열이 작아서 크게 상관 없지만
# 배열이 커질 수록 체감이 되지 않을까 싶습니다.

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def findIsland(r, c, tizu):

    tizu[r][c] = 0

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(tizu) and 0 <= nc < len(tizu[0]) and tizu[nr][nc] == 1:
            findIsland(nr, nc, tizu)

    tizu[r][c] = 1
    pass




t = 2

for test_case in range(1, t+1):
    tc = int(input())
    tizu = [list(map(int, input())) for _ in range(4)]

    count = 0
    for r in range(4):
        for c in range(5):
            if tizu[r][c] == 1:
                findIsland(r, c, tizu)
                count += 1   
                pass
    print(count)
    print(tizu)