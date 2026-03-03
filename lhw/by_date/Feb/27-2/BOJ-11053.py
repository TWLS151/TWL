# BOJ-11053
# 가장 긴 증가하는 부분 수열
# DP

N = int(input())
lst = list(map(int, input().split()))
dp = [1] * N

# 하나씩 순회하면서
# 본인보다 크면 += 1, 작으면 = 1

for i in range(N):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))