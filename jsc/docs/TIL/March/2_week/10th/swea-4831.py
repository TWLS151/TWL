import sys

sys.stdin = open("swea-4831.txt")

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())

    bus_stops = list(map(int, input().split()))
    # 도착지점 추가 why? 도착도 같이 볼려고
    bus_stops.append(N)

    battery = K
    count = 0
    for move in range(1, N):
        # 한칸당 배터리 감소
        battery -= 1

        for stop in bus_stops[:-1]:
            if stop == move and battery < (bus_stops[bus_stops.index(stop) + 1] - move):
                battery = K
                count += 1
        if battery == 0:
            count = 0
            break
    print(f"#{tc} {count}")
