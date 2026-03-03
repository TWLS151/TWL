# BOJ - 9251
# LCS
# DP

astr = input()
bstr = input()

N = len(astr)
M = len(bstr)

dp = [[0]*(M+1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, M+1):
        if astr[r-1] == bstr[c-1]:
            dp[r][c] = dp[r-1][c-1] + 1
        else:
            dp[r][c] = max(dp[r-1][c], dp[r][c-1])

print(dp[N][M])