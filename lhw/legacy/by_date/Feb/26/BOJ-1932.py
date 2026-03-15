# BOJ-1932
# 정수 삼각형
# DP

N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]


# 후보는 바로 위층의 직전 인댁스 또는 같은 인덱스 두 개

dp = []
for i in range(1, N+1):
    dp.append([0]*i)

dp[0][0] = tri[0][0]
# dp[1][0] = dp[0][0] + tri[1][0]
# dp[1][1] = dp[0][0] + tri[1][1]
for floor in range(1, N):  # 3행부터 시작
    dp[floor][0] = dp[floor-1][0] + tri[floor][0]
    dp[floor][-1] = dp[floor-1][-1] + tri[floor][-1]
    
    for idx in range(1, floor):  # 3행 1열부터 N-2열까지 
        dp[floor][idx] = max(dp[floor-1][idx-1] + tri[floor][idx], dp[floor-1][idx] + tri[floor][idx])

print(max(dp[N-1]))
# print(dp)
