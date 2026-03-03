import sys

sys.stdin = open('input_1206.txt')

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))

    view_right_cnt = 0

    for i in range(2, N-2):
        floor = buildings[i]
        max_floor = 0
        for j in [-2, -1, 1, 2]:
            view_right = floor - buildings[i+j]
            if buildings[i+j] >= floor:
                break
            elif max_floor < buildings[i+j]:
                max_floor = buildings[i+j]
        else:
            view_right_cnt += floor - max_floor

    print(f'#{test_case} {view_right_cnt}')






    """
    for i in range(2, N-2):
        floor = buildings[i]
        view = buildings[i-2:i] + buildings[i+1:i+3]
        max_floor = max(view)
        if max_floor < floor:
            view_right_cnt += floor - max_floor

    print(f'#{test_case} {view_right_cnt}')
    """

    """
    for i in range(2, N-2):
        floor = buildings[i]
        view = sorted(buildings[i-2:i+3])
        if view[-1] == floor:
            view_right_cnt += floor - view[-2]
    """
