# import sys
#
# sys.stdin = open('./input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    K, N, M = map(int, input().split())

    arr = list(map(int, input().split()))


    # 해결 아이디어

    # 1. 도로 리스트 생성
    way_list = [0]*(N+1)

    # 2. 충전소 정류장 인덱스 값을 +1

    for idx in arr:

        way_list[idx] = 1


    # 3. 이동 반복문 : while

    # Hint : idx는 '현재 버스가 서있는 위치'와 정확히 일치하고 있는가?
    # 사고 전환 포인트 : 현재 갈 수 있는 범위 중, 다음으로 어디까지 가는 것이 최선인가?
    ## 이건 당연히 최대 거리에 있는 정류장이지.

    # my 현재 위치를 인덱스 개념처럼 사용할 필요성이 존재!

    position = 0
    charge_count = 0


    # 주의 ! while은 조건이 충족되는 동안 돌아간다.
    while position < N:

        # 3-1. 목적지에 도달이 가능한 경우 : 반복문 종료 후 결과 출력
        if position + K >= N:

            break

        # 3-2. 목적지에 도달할 수 없는 경우 -> 충전소 탐색
        # 주의! charge_area를 통해 파악해야 할 정확한 범위는?
        # 충전소를 찾았는 지 여부를 판단하기 위한 이진 변수 found 도입
        # 필요한 이유 : 충전소를 찾지 못했을 때 while을 빠져나갈 추가 방법이 필요하기 때문

        found = False # 아직 못찾았으므로

        # 4. 전진을 위한 경우의 수
        # 현재 위치에서 +K 만큼의 범위를 charge_area 범위로 지정


        if position + K < N:
            charge_area = way_list[position + 1:position + K + 1]

        # 주의 ! position이 다음으로 가야할 절대 거리는 어디인가?
        # charge_area를 뒤부터 탐색하도록 설정 : 맨 뒤 거리에 충전소가 있을 경우, 그 전의 충전소는 고려하지 않아도 되기 때문
            for idx in range(K-1, -1, -1):

                # 4-1. 앞에 충전소가 없을 경우 : 반복을 종료하고 0을 출력
                # found = False를 그대로 유지

                if 1 not in charge_area:
                    charge_count = 0
                    break

                # 4-2. charge_area에 충전소가 있을 경우 : 가장 먼 거리로 position을 이동

                elif charge_area[idx] == 1:
                    position += (idx + 1) # not (idx + 1)!
                    found = True
                    charge_count += 1
                    break # Greedy의 경우, 첫 번째 선택이 곧 최적의 선택

                    # 왜 오류가 발생했나? - 목적지에 도달해줄 수 있는 경우에도 charge_area를 보려고 했기 때문


            if found is False:
                break

                # 주의! break 다음의 구문은 실행되지 않는다.
                # 따라서 charge_count = 0임을 지정하고 멈춘 뒤 통일된 출력 양식에서 나오도록 해주는 것이 적절하다.
                # print(f"#{T} 0")

    print(f"#{tc} {charge_count}")