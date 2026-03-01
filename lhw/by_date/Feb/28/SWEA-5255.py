# SWEA-5255
# 타일 붙이기

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    dp = [0] * (N+1)

    dp[1] = 1
    dp[2] = 3
    dp[3] = 6

    # [1]
    # 직전 인덱스 값

    # [2]
    # 두번째 인덱스 값 * 2

    # [3]
    # 세번째 인덱스 값

    for idx in range(4, N+1):
        dp[idx] = dp[idx-1] + dp[idx-2]*2 + dp[idx-3]

    print(f"#{test_case} {dp[N]}")