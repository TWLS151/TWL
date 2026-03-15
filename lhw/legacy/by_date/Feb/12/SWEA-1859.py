# 백만 장자 프로젝트
# 1145 - 1155
# TTP: 10'
# 진짜 이렇게만 나와라 제발

# 연속된 N일 동안 매매가를 알고 있다
# 하루에 최대 1만큼 구입
# 판매는 자유

# 3일 동안 매매가가 1, 2, 3 이면 처음 두 날에 구매해 마지막 날에 팔면 3의 이익
# 최대 이익 출력
# 스택 개념?
# 다 집어 넣고 꺼내면서 확인하는거지
# 처음 꺼내는 걸 기준으로 두고 더 큰 게 나오기 전까지 판다.
# 더 큰게 나오면 더 큰게 기준

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())  # 2<= n <= 백만
    price_list = list(map(int, input().split()))  # 요소 <= 10000

    # 아무것도 안 살 수도 있다.
    result = 0

    # 일단 리스트로 받았으니 다 들어가있고
    # while? 일단 하나 뽑아서 기준 세우고
    max_price = price_list.pop()
    while price_list:
        if max_price > price_list[-1]:
            # 같으면 어떡해야하지? 안사는거지 뭘 어떡해
            # 이자나 카운팅 같은거 없으니까 사도 되고 안사도 됨
            result += max_price - price_list.pop()
        
        else:
            max_price = price_list.pop()  # 팝 해서 제거해줘야 다음 거 나온다

    # 된 거 같은딩

    print(f'#{test_case} {result}')
    