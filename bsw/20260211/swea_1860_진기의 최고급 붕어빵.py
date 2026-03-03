# N명의 사람이 자격을 얻음. M초의 시간을 들이면 K개의 붕어빵을 만들 수 있음.
# T
# N, M, K가 주어짐.
# N이 주어지는 데 각 정수는 각 사람이 언제 도착하는 지를 초 단위롤 나타냄.
# 기다리는 시간 없이 제공 가능하면 possible, 아니면 impossible
import sys

sys.stdin = open('swea_1860_진기의 최고급 붕어빵.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    time_lst = sorted(list(map(int, input().split())))
    result = 'Possible'
    for i in range(N):
        boong_num = (time_lst[i] // M * K) - (i + 1) # 각 시간에 따른 붕어빵 개수를 미리 지정
        # 어차피 손님 1명당 붕어빵 1개라 위의 식을 정의 가능
        if boong_num < 0:
            result = 'Impossible'
            break
    print(f'#{tc} {result}')
                