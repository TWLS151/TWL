# BOJ - 2116
# 주사위 쌓기

# 로테이트 돌리면서

# 인덱스 [0][5] 더한거 가장 작은거 찾고

# 그리드로?

# (0, 5), (1, 3), (2, 4) 경우의 수 1번 주사위가 3개
# 위 세 인덱스 고정하고 위에 주사위는 돌려가면서

N = int(input())

dice = [list(map(int, input().split())) for _ in range(N)]

dice_dict = {
    0: 5,
    5: 0,
    1: 3,
    3: 1,
    2: 4,
    4: 2
}

# 
def dicing(d, bottom_idx):
    top_idx = dice_dict[bottom_idx]
    m = 0
    for i in range(6):
        if i != bottom_idx and i != top_idx:
            if d[i] > m:
                m = d[i]
    return m, d[top_idx]

answer = 0

for first_bottom_idx in range(6):
    total = 0

    smax, top_val = dicing(dice[0], first_bottom_idx)
    total += smax

    for k in range(1, N):
        d = dice[k]

        bottom_idx = d.index(top_val)
        smax, top_val = dicing(d, bottom_idx)
        total += smax

    answer = max(answer, total)

print(answer)