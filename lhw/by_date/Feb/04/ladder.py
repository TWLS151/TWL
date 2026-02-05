# 절대 단축 실행을 잊지 마.


TC = 10

for test_case in range(1, TC + 1):
    test_case_num = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    # 인덱스 값이 필요하기 때문에 enumerate 활용해 인덱스와 밸류 같이 뽑기
    # 제일 위에서 구멍을 찾기 때문에 0번 리스트만 확인하면 됨
    for idx, val in enumerate(ladder[0]):
		    # 실행시마다 row 초기화하고 col 은 idx 에서 시작
        row = 0
        col = idx
        # val 값이 1일때 내려가기 시작
        if val == 1:
		        # 내려가다가 row 가 99가 되면 밑바닥이므로 탈출
            while row + 1 != 100:
		            # 한 칸 내려가기
                row += 1
                # 오른쪽에서 1을 발견하면 오른쪽으로 들어가기
                # 절대절대 if 문의 순서를 지켜야함
                # ladder 값을 먼저 확인하면 그냥 인덱스 에러가 나버림
                if col + 1 < 100 and ladder[row][col + 1] == 1:
                    while col + 1 < 100 and ladder[row][col + 1] == 1:
                        col += 1
                # 왼쪽으로 들어가기 // 오른쪽과 동일
                elif col - 1 >= 0 and ladder[row][col - 1] == 1:
                    while col - 1 >= 0 and ladder[row][col - 1] == 1:
                        col -= 1
        # while 문을 탈출했을때, row 가 99일 때 그 지점의 값이 2면 목적지 도착, 탈출
        if ladder[row][col] == 2:
            break
		# 출력
    print(f'#{test_case} {idx}')
