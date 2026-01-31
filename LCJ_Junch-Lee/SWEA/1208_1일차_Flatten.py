# 테스트 케이스가 제공되지 않았으므로 range() 내 값을 임의로 지정

import sys

sys.stdin = open("./input.txt", "r")

for T in range(1, 10 + 1):

    # 1. 입력
    # dump 제한 수 입력
    N = int(input())

    # 상자 높이 문자열 입력(int로 변환)
    boxes = list(map(int, input().split()))

    # 2. loop : dump 제한 수 만큼

    for i in range(N):
        
        # 1. 최고층, 최저층 인덱스 파악
        high = boxes.index(max(boxes))
        low  = boxes.index(min(boxes))

        # 2. 중복을 고려한 최고,최저층 
        # 최고층의 가장 앞 인덱스 값을 최고층으로
        # 최저층의 가장 앞 인덱스 값을 최저층으로

        boxes[high] -= 1
        boxes[low] += 1

        # 3. dump 수행 이후 최고, 최저층 파악
        # 해맸던 이유 : dump 수행 이후 달라진 최고층, 최저층의 높이를 파악해 if문을 걸어야했음


        high_dump = boxes[boxes.index(max(boxes))]
        low_dump = boxes[boxes.index(min(boxes))]

        # 4. dump 수행 이후 높이 차가 1보다 작을 시 : dump를 더 진행하는 것이 의미가 없음 -> 종료
        if high_dump - low_dump <= 1:
            break

        else: continue

    # 4. Dump 제한 횟수 모두 소진 or 평탄화 완료 시 : 정답 출력

    print(f"#{T} {high_dump - low_dump}")