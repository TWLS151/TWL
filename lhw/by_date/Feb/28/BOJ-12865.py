# BOJ - 12865
# 평범한 배낭
# DP

N, K = map(int, input().split())
dp = [0] * (K+1)

for _ in range(N):
    W, V = map(int, input().split())
    for w in range(K, W-1, -1):
        dp[w] = max(dp[w], dp[w-W] +V)

print(dp[K])