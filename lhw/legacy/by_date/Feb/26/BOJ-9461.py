# BOJ-9461.py
# 파도반 수열
# DP


TC = int(input())
N = []
for test_case in range(1, TC+1):
    N.append(int(input()))

dp = [0] * (max(N) + 1)

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2


for n in range(5, max(N)+1):
    dp[n] = dp[n-1] + dp[n-5]
    
for i in N:
    print(dp[i])
