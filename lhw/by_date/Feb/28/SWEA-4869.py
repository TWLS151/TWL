# SWEA - 4869
# 종이붙이기
# DP

TC = int(input())
for tesT_case in range(1, TC+1):
    n = int(input())
    l = n//10 + 1

    dp = [0] * (l+1) 

    dp[1] = 1   # 10 세로 하나
    dp[2] = 3   # 10 세로 둘, 20 하나, 10 가로 둘
    dp[3] = 5
    
    # [1] 10 세로 하나로 끝
    # 직전 인덱스

    # [2] 20 하나로 끝
    # 두번째 전 인덱스 * 1

    # [3] 10 가로 둘로 끝
    # [2] 와 동일

    for i in range(4, l):
        dp[i] = dp[i-2]*2 + dp[i-1]

    print(f'#{tesT_case} {dp[l-1]}')
    