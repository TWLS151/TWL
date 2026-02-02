for i in range(1, 11):
    T = int(input())
    num_lst = list(map(int, input().split()))
    result = 0
    # 계산 결과를 담을 result 생성
    for j in range (2, T - 2): # 얘를 어떻게 범위를 지정하죠? 진짜 모르겠음.
    # num_lst의 첫번째, 두번째, 뒤에서 첫번째와 두번째는 의미 없으니 2 범위에서 T-2 범위로 계산
        left_side = [num_lst[j-2], num_lst[j-1]]
        right_side = [num_lst[j+1], num_lst[j+2]]
        # num_lst의 왼쪽, 오른쪽 각각 두 개씩 리스트 지정
        max_val = max(left_side + right_side)
        # 왼쪽 오른쪽 리스트를 합침.
        diff = num_lst[j] - max_val
        # 가운뎃 값에서 각 리스트의 차이를 계산
        if diff > 0:
            result += diff
        # 차가 0 초과일 때만 result에 차이를 더함.
    print(f'#{i} {result}')