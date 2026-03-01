# BOJ-14501
# 퇴사
# SW 달리기 // SILVER III

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0] * (N + 1)

for i in range(N-1, -1, -1):
    dp[i] = dp[i+1]

    if i + T[i] <= N:
        dp[i] = max(dp[i], P[i] + dp[i + T[i]])

print(dp[0])


# 약간 dp인데
# 수영장 회원권 문제랑 비슷함

