for T in range(1, 10 + 1):

    N = int(input)

    boxes = list(map(int, input().split()))

    for i in range(N):
        
        # 1. 최고층, 최저층 인덱스 파악
        high = boxes.index(max(boxes))
        low  = boxes.index(min(boxes))

        # 2. 중복을 고려한 최고,최저층 
        # 최고층의 가장 앞 인덱스 값을 최고층으로
        # 최저층의 가장 앞 인덱스 값을 최저층으로

        highest = boxes[high]
        lowest = boxes[low]

        # 3. dump 수행

        highest -= 1
        lowest += 1

        if highest == lowest:
            break


    # 4-1. Dump 제한 횟수 모두 소진시 : 정답 출력
        print(f"#{T} {highest - lowest}")





