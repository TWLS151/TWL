# SWEA - 16504
# GRAVITY

tc = int(input())

for test_case in range(1, tc + 1):
    width = int(input())
    box_height_lst = list(map(int, input().split()))

    # 오른쪽으로 가장 가까운 벽이나 박스까지의 거리를 구한다.
    # 가장 큰 낙차를 구하는 문제이니
    # 높이가 가장 높은 박스를 구하면 안되는구나
    # 마지막 인덱스의 높이는 100으로 정하고
    # 오른쪽으로 가며 자기와 같거나 자기보다 높은 높이가 나오면 인덱스의 차를 구하자.

    # 리스트 마지막에 100 추가
    box_height_lst.append(100)

    # 가장 큰 낙차 변수 설정
    max_diff = 0

    # 이중 for문으로 순회하며 비교
    # 100 추가했으니 100까지 비교해야함
    for idx in range(width):
        for higher_idx in range(idx + 1, width + 1):
            if box_height_lst[idx] <= box_height_lst[higher_idx]:
                # 높이가 같거나 더 높은 박스의 위로 올라가는거니까 -1 을 꼭 해줘야한다.
                if max_diff <= higher_idx - idx - 1:
                    max_diff = higher_idx - idx - 1
                    break
            else:
                continue

    print(f'#{test_case}', max_diff)