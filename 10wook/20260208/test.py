T = int(input())

for tc in range(1, T+1):
    N = int(input())
    portals = list(map(int, input().split()))
    answer = N-1 + (N-2)
    for i in range(1,N-1):
        # portals[i]-1 #이게 인덱스 상의 숫자까지 이동해서 생긴 손해
        # 현재 위치 ==> 인덱스 상으로 현재 숫자
        answer = answer + (i+1 - (portals[i]))
    print(f'#{tc} {answer}')
