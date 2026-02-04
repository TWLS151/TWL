T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    a_lst = list(map(int, input().split()))
    sum_lst = 0
    # sum_lst를 0으로 지정함.
    for i in a_lst[:b]:
        sum_lst += i
    max_sum = sum_lst
    min_sum = sum_lst
    # max_sum과 min_sum을 a_lst의 처음부터 b 범위 만큼까지 합으로 정함.
    for j in range(a - b + 1):
    # a - b + 1로 범위가 시작할 때 마지막 범위까지 합을 구함.
    # out of range 방지
        sum_lst2 = 0
        for k in range(j, j + b):
            sum_lst2 += a_lst[k]
        # j를 시작점으로 하여 j에서 b만큼 떨어진 범위만큼 합을 구하는 새로운 변수 생성.
        if sum_lst2 >= max_sum:
            max_sum = sum_lst2
        if sum_lst2 <= min_sum:
            min_sum = sum_lst2
        # 초기 합인 max_sum, min_sum값이 더 크거나 작은 값을 만났을 때, 각각 작은 값으로 갱신
    print(f'#{tc} {max_sum - min_sum}')

