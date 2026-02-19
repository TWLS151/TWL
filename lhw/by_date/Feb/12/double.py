
import sys
sys.stdin = open('a.txt')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())

    lst = list(map(int, input().split()))
    used = [False for _ in range(N + 1)]
    # lst.insert(0, 0)
    count = 0

    while True:
        if sum(lst) >= N * 2:
            print(f'#{test_case} {count}')
            break
        
        arr = []
        for k, v in enumerate(lst):
            x = max(v + k, k)
            if not used[k]:
                arr.append((k, v-x, x))

        arr.sort(key= lambda x: x[1], reverse= True)
        a, b, c = arr[0]

        lst[a] = c
        count += 1
        used[a] = True

# import sys

# sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))

#     # 문제의 인덱스는 1부터 시작하지만 파이썬은 0부터 시작하므로,
#     # 계산 편의를 위해 맨 앞에 0을 추가하여 인덱스를 맞춤
#     arr.insert(0, 0)

#     # 목표 합계
#     target_sum = 2 * N
#     # 현재 합계
#     current_sum = sum(arr)

#     # 작업 횟수
#     op_count = 0

#     # 이미 목표를 달성했다면 작업을 할 필요가 없음
#     if current_sum >= target_sum:
#         print(f'#{tc} {op_count}')
#         continue  # 다음 테스트 케이스로 넘어감

#     # 1. 각 인덱스(i)별로 작업을 수행했을 때의 '증가량'을 계산
#     gains = []
#     for i in range(1, N + 1):
#         new_value = max(arr[i] + i, i)
#         gain = new_value - arr[i]
#         gains.append(gain)

#     # 2. 계산된 증가량을 내림차순으로 정렬 (가장 이득이 큰 순서)
#     gains.sort(reverse=True)

#     # 3. 가장 이득이 큰 작업부터 차례대로 적용
#     for gain in gains:
#         current_sum += gain  # 현재 합계에 증가량을 더함
#         op_count += 1  # 작업 횟수 1 증가

#         # 목표 합계를 달성했다면 즉시 중단
    #     if current_sum >= target_sum:
    #         break

    # print(f'#{tc} {op_count}')
