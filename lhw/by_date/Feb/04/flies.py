TC = int(input())

# 함수를 만들어보자 !

def killing_area(effect_size, spot_row, spot_col, flies):
    pass
    # 범위를 정해야겠는데
    # effect_size 만큼 range 를 정해야지
    # 변수도 하나 만들어야겠다.
    kill_log = 0
    # effect_size 만큼의 matrix를 순회하는 이중 for문 생성
    for num in range(effect_size):
        for digit in range(effect_size):
		        # 들린 자리의 파리를 다 죽이고 그 수를 세어냄
            kill_log += flies[spot_row + num][spot_col + digit]
    # 킬로그 반환
    return kill_log

# 테스트 케이스 반복
for test_case in range(1, TC + 1):
    area_size, weapon_size = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(area_size)]

		# 매 시행시마다 반환되는 킬 로그를 기록해둘 장부 생성
    kill_log_lst = []
    # 계산의 기준점이 무기의 좌상단이라 우하단으로 갈 수록 필드를 벗어나 낭비되는 무력이 생김
    # 그래서 무기가 딱 들어맞는 곳 까지만 무력을 사용
    for row in range(area_size - weapon_size + 1):
        for col in range(area_size - weapon_size + 1):
		        # 계산은 만들어두었던 함수를 사용
            kill_log_lst.append(killing_area(weapon_size, row, col, arr))
    # 출력
    print(f'#{test_case} {max(kill_log_lst)}')