#


tc = int(input())

for test_case in range(1, tc + 1):

    height, width = map(int, input().split())

    field = [list(map(int, input().split())) for _ in range(height)]

    # 필드에서 풍선 하나 선택
    # 그 선택한 풍선의 숫자만큼 네 방향으로 터짐
    # 터진 풍선의 숫자 전부 총합

    # 각 타겟의 총합을 담아둘 리스트
    total_list = []

    # 필드를 순회하며 풍선 파괴
    for row in range(height):
        for col in range(width):
            effect_area = field[row][col]

            # 변수 설정
            # 풍선을 선택하면 터져서 그 풍선의 숫자도 더해야한다.
            total = effect_area

            # 필드 밖으로 나가는 경우의 수 분기처리
            # 십자방향으로 터지기 때문에 네 가지로 충분하다.
            for idx in range(1, effect_area + 1):
                effect_row_pos = row + idx
                effect_col_pos = col + idx
                effect_row_neg = row - idx
                effect_col_neg = col - idx
                if effect_row_neg >= 0:
                    total += field[effect_row_neg][col]
                if effect_row_pos < height:
                    total += field[effect_row_pos][col]
                if effect_col_neg >= 0:
                    total += field[row][effect_col_neg]
                if effect_col_pos < width:
                    total += field[row][effect_col_pos]

            # 총합 저장
            total_list.append(total)
    
    # 출력
    print(f'#{test_case} {max(total_list)}')    