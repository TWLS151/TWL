import sys

sys.stdin = open("swea-5201.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 0. 변수 설정
    freights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    freights_visited = [False] * N
    trucks_visited = [False] * M

    total = 0

    freights.sort(reverse=True)
    trucks.sort(reverse=True)

    # 1. 그리디 시작 why? 트럭과 짐 중에 그냥 큰거를 고르면 이게 최대니깐
    for fre_idx, freight in enumerate(freights):
        for truck_idx, truck in enumerate(trucks):
            # if 줄바꿈으로 쓰기 why? 블랙 스타일가이드가 알아서 해줌
            if (
                freights_visited[fre_idx] == False
                and trucks_visited[truck_idx] == False
            ):
                if freights[fre_idx] <= trucks[truck_idx]:
                    total += freights[fre_idx]
                    freights_visited[fre_idx] = True
                    trucks_visited[truck_idx] = True
                    break

    print(total)
