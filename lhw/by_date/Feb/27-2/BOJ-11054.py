# BOJ - 11054
# 가장 긴 바이토닉 부분 수열
# DP

N = int(input())
lst = list(map(int, input().split()))
dp = [[1] * (N+1) for _ in range(2)]

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[0][i] = max(dp[0][i], dp[0][j]+1)

            # if lst[i] > lst[i-1]:
            #     dp[i] += 1

for i in range(N-1, -1, -1):
    for k in range(N-1, i, -1):
        if lst[k] < lst[i]:
            dp[1][i] = max(dp[1][i], dp[1][k]+1)

# print(dp)
nlst = list(zip(*dp))
# print(nlst)
print(max(map(sum, nlst)) - 1)
# print(list(map(sum, *nlst)))