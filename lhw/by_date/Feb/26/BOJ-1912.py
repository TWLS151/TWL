# BOJ-1912
# 연속합
# DP

n = int(input())
lst = list(map(int, input().split()))

dp = [-1000] * (n+1)
dp[0] = lst[0]

for i in range(1, n):
    dp[i] = max(lst[i], dp[i-1] + lst[i])

print(max(dp))