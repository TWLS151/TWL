# BOJ - 2156
# 포도주 시식
# DP

# 잔을 선택하면 모두 마셔야하고 마신 후에는 원래 위치에 둔다.
# 연속으로 세 잔을 마실 수는 없다.

N = int(input())
wine = [0] + [int(input()) for _ in range(N)]

dp = [[0]*3 for _ in range(N+1)]

dp[0][0] = wine[0]
dp[1][0] = wine[1]
dp[1][1] = dp[0][0] + wine[1]

for i in range(1, N+1):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + wine[i]
    dp[i][2] = dp[i-1][1] + wine[i]

print(max(dp[N-1]))











# N = int(input())
# wine = [0]
# for _ in range(N):
#     wine.append(int(input()))

# if N == 1:
#     print(wine[1])

# elif N == 2:
#     print(wine[1] + wine[2])

# else:
#     best = 0
#     for i in range(3):
#         dp = [0] * (N+1)
#         for j in range(2+i, N, 3):
#             dp[j] = wine[j] + wine[j-1]

#         best = max(best, sum(dp))
#     print(best)

# # 패딩 x
# N = int(input())
# wine = []
# for _ in range(N):
#     wine.append(int(input()))

# # print(wine)

# best = 0
# for i in range(3):
#     dp = [0] * (N+1)
#     for j in range(i, N+1, 3):
#         if j-1 < 0:
#             dp[j] = wine[j]
#         else:
#             dp[j] = wine[j] + wine[j-1]
#     # print(dp)
#     best = max(best, sum(dp))
# print(best)

# # dp = [[0] * 2 for _ in range(N+1)]
# dp = [0] * (N+1)
# # 각 잔마다 첫 번째, 두 번째 선택일 때를 고려

# # 첫 잔, 둘째 잔은 따로 구해야하네
# # 첫 잔은 첫 번째 선택만 고려해야하고
# # 둘째 잔은 첫 번쨰, 두번째 선택을 고려해야함
# # dp[1][0] = wine[1]
# # dp[2][0] = wine[2]
# # dp[2][1] = dp[1][0] + wine[2]
# # dp[1] = wine[1]  # 0번 인덱스에 더미를 넣어서 없어도 괜찮은 것 같음

# # for i in range(2, N+1):
# #     # dp[i][0] = wine[i]
# #     # dp[i][1] = wine[i] + dp[i-1][0]
# #     dp[i] = wine[i] + wine[i-1]

# best = 0
# for i in range(3):
#     dp = [0] * (N+1)
#     for j in range(2+i, N+1, 3):
#         dp[j] = wine[j] + wine[j-1]

#     best = max(best, sum(dp))
# print(best)

# # dp의 직전 인덱스 2번에 값이 있으면 해당 인덱스는 선택을 못함

# # even_sum = sum(dp[i] for i in range(2, N+1) if i % 2 == 0)
# # odd_sum = sum(dp[i] for i in range(2, N+1) if i % 2 == 1)

# # print(even_sum)

