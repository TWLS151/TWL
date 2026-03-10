import sys

sys.stdin = open("swea-5202.txt")

T = int(input())

for tc in range(1, T + 1):
    truck_nums = int(input())
    times = [list(map(int, input().split())) for _ in range(truck_nums)]

    # for i in range(truck_nums):

    times.sort(key=lambda x: x[1])

    count = 0
    last_end_time = 0

    # 그리디
    for i in range(truck_nums):
        start = times[i][0]
        end = times[i][1]

        if start >= last_end_time:
            count += 1
            last_end_time = end

    print(f"#{tc} {count}")
