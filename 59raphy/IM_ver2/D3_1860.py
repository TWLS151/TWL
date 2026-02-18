import sys

sys.stdin = open('input_1860.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M, K = list(map(int, input().split()))
    customer = list(map(int, input().split()))

    result = 'Possible'

    customer.sort()  # 손님 도착시간 오름차순 정렬

    # 첫 번째 판이 나오기 전(M초 전)에 도착하는 손님이 있는지 확인
    # 0번 손님이 M초 이후에 도착한다면, 모든 손님이 M초 이후에 도착
   if customer[0] < M:
        result = 'Impossible'

    # 모든 손님에게 팔기 위해 구워야 하는 판 수
    plate_num = N // K + 1

    # 각 판의 첫 번째 붕어빵을 받는 손님이 완성 시간 이후에 도착하는지 확인
    for plate in range(1, plate_num):
        # (K * plate)번 손님은 앞선 판들의 재고를 모두 소진한 후,
        # (plate + 1)번째 판이 완성되어야만 빵을 받을 수 있는 첫 번째 대기자
        # 이 손님이 해당 판 완성 시간인 M * (plate + 1)보다 일찍 도착하면 즉시 실패
        if K * plate < N and customer[K * plate] < M * (plate + 1):
            result = 'Impossible'
            break

    print(f'#{test_case} {result}')
