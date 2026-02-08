# 시험 대비
# 경비병
# TTP: 21'31"

import sys
sys.stdin = open('security_guard.txt')

TC = int(input())

def gaurdsSight(matrix, row, col):
    pass
    size = len(matrix)
    # 좌표 추가할 리스트
    spot_lst = []
    # 방향 리스트
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 방향 순회
    for dx, dy in dirs:
		    # 전진하기 위한 좌표 설정
        px, py = row + dx, col + dy
        # 영역 안에서만 진행
        if 0 <= px < size and 0 <= py < size:
            # 밖으로 나가면 탈출
            while 0 <= px < size and 0 <= py < size:
                # 빈 공간을 만나면 좌표 리스트에 추가
                # 그냥 바로 카운팅을 하는게 나았겠네요
                if matrix[px][py] == 0:
                    spot_lst.append((px, py))
                    px += dx
                    py += dy
                # 기둥이 보이면 탈출
                elif matrix[px][py] == 1:
                    break
    # 좌표 리스트 반환
    # 카운팅 반환하는게 낫다
    return spot_lst

for test_case in range(1, TC+1):
    size = int(input())
    lyoiki = [list(map(int, input().split())) for _ in range(size)]

    # 경비병을 먼저 찾아야겠네
    # 경비병의 위치에서 네 방향으로 1이 있는지 확인하고
    # 1이 있다면 그 직전 위치까지 좌표로 저장
    # 그 좌표들 안에 들어가지 않으면서 값이 0인 지점의 좌표의 개수 카운팅
    # 좌표의 개수랑 1의 개수를 세서 전체 필드에서 빼는게 빠르겠다

    count = 0
    # 순회
    for row in range(size):
        for col in range(size):
		        # 기둥 수 카운팅
            if lyoiki[row][col] == 1:
                count += 1
            # 경비병 찾으면 함수 진입 및 카운팅
            if lyoiki[row][col] == 2:
                danger = gaurdsSight(lyoiki, row, col)
                count += 1
    # 안전한 장소 = 전체 필드 크기 - 위험좌표개수 - 기둥 및 경비원 좌표 개수
    safety = size**2 - len(danger) - count

		# 출력
    print(f'#{test_case} {safety}')