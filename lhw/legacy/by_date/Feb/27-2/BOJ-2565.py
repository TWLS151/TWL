# BOJ-2565
# 전깃줄
# DP

# 기준을 하나 정하고 그 줄을 살렸을 때 몇 개의 줄을 잘라야하는지를 dp에 저장

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

B = [b for _, b in lst]
dp = [1] * (N)

for i in range(N):
    for j in range(i):
        if B[j] < B[i]:
            dp[i] = max(dp[i], dp[j] + 1)

lis_len = max(dp)
print(N-lis_len)