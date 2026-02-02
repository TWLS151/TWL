T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    card_dict = {}
    # 빈 dict을 생성
    card_lst = list(map(int, input()))
    # split을 사용하지 않고 리스트에 정수 형태로 저장 (ex. 49679면 [4, 9, 6, 7, 9] 형태
    for tc2 in card_lst:
        if tc2 in card_dict.keys():
            card_dict[tc2] += 1
        else:
            card_dict[tc2] = 1
        # 만약에 card_dict에 tc2 값이 있으면 value에 1 추가
        # 값이 없으면 새롭게 1을 부여
    max_val = 0
    max_count = 0
    # 최댓값, 최대 카운트 횟수를 임의로 지정
    for val, count in card_dict.items():
    # card_dict의 key와 value 값을 모두 순회
        if max_count < count:
            max_val = val
            max_count = count
        # 더 큰 카운트 횟수를 발견하면 그 카운트로 변경, 최댓값도 마찬가지
        elif max_count == count and max_val < val:
            max_val = val
        # 카운트 횟수가 같은 경우에는 더 큰값을 지정
    print(f'#{tc} {max_val} {max_count}')
    # f-string 형태로 출력