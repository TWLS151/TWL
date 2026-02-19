# SWEA - 5656
# 벽돌 깨기

# 파리잡기 느낌인데

TC = int(input())
for test_case in range(1, TC+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    