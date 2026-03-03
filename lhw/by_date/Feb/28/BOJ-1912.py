# BOJ - 1912
# 연속합
# DP

# 반복되는 계산, 상태를 찾아라.
# 모든 경우를 다 보되, 같은 상태는 한 번만 본다.

N = int(input())
lst = list(map(int, input().split()))

dp = [-1000] * (N+1)
dp[0] = lst[0]

for i in range(1, N):
    dp[i] = max(lst[i], dp[i-1] + lst[i])

print(max(dp))