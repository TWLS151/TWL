# 숫자를 차례로 나눔.
# 2로 나누는 것을 반복 : 카운트를 세서 카운트를 반환
# 3, 5, 7, 11도 마찬가지
T = int(input())
div_list = [2, 3, 5, 7, 11]
# 나눌 리스트를 미리 지정
for tc in range(1, T + 1):
    num_lst = []
    # 숫자 나눌 리스트를 생성
    num = int(input())
    for i in div_list:
    # 나누는 숫자 순회
        result = True
        count_num = 0
        # while을 중단시키는 조건인 result와 나누는 횟수를 세는 count_num 변수 생성
        while result:
            if num % i == 0:
                num //= i
                count_num += 1
            # 나누어 떨어지면 num을 i로 나누고 나누는 횟수 1 증가
            else:
                result = False
            # 떨어지지 않으면 while문 중단
        num_lst.append(count_num)
        # 최종적인 count 횟수를 리스트에 순서대로 추가
    print(f'#{tc} {num_lst[0]} {num_lst[1]} {num_lst[2]} {num_lst[3]} {num_lst[4]}')
                