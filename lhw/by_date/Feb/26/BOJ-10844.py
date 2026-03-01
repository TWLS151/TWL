# BOJ - 10844
# 쉬운 계단 수
# DP

N = int(input())
MOD = 1_000_000_000

dp = [[0]*10 for _ in range(N+1)]

for d in range(1, 10):
    dp[1][d] = 1

for length in range(2, N+1):
    dp[length][0] = dp[length-1][1] % MOD
    dp[length][9] = dp[length-1][8] % MOD
    for d in range(1, 9):
        dp[length][d] = (dp[length-1][d-1] + dp[length-1][d+1]) % MOD

print(sum(dp[N]) % MOD)

# 마지막 자리 숫자가 정해지면 자릿수가 하나 적은 계단수의 개수를 이용할 수 있음

# N = int(input())

# dp = [[0]*10 for _ in range(N+1)]

# for d in range(1, 10):
#     dp[1][d] = 1

# for length in range(2, N+1):
#     dp[length][0] = dp[length-1][1]
#     dp[length][9] = dp[length-1][8]
#     for d in range(1, 9):
#         dp[length][d] = (dp[length-1][d-1] + dp[length-1][d+1])
    
# print(sum(dp[N]) % MOD)