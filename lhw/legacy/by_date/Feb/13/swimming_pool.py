import sys
sys.stdin = open('input.txt')


TC = int(input())

for test_case in range(1, TC+1) :
    # 하루하고 한달 비교 먼저 하고
    # 그 다음 3달 슬라이싱으로 브루트포스 돌리고
    # 그 다음 1년 비교
    fee = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    plan.insert(0, 0)  # 더미 insert

    dm = [0] * 13  # 일일권, 한달권 비교
    for i in range(1, 13):
        dm[i] = min(plan[i]* fee[0], fee[1])

    # DP 진입
    dp = [0] * 13
    # 점화식 계산
    for i in range(1, 13):
        dp[i] = dp[i-1] + dm[i]

        # i 가 3보다 커지면 3개월권 계산이 가능
        if i >=3:
            dp[i] = min(dp[i], dp[i-3] + fee[2])
            
    best = min(dp[12], fee[3])
    print(f'#{test_case}', best)

    # 누적합이랑 비슷한 느낌인 것 같았는데 누적합과는 다른 부분이 있었습니다.


    # 슬라이싱을 활용해서 3개월 구간을 잡아내려헀는데 실패했습니다.
    # 이렇게 진행하면 3개월권을 띄엄띄엄 사는 부분을 캐치하지 못합니다.
    # b= []
    # for j in range(1, 4):
    #     mest = 0
    #     for i in range(j, 11, 3):
    #         if dm[i] + dm[i+1] + dm[i+2] > fee[2]:
    #             mest -= dm[i] + dm[i+1] + dm[i+2]
    #             mest += fee[2]

    #     b.append(mest)
        
        # print(best)
    # best += min(b)
