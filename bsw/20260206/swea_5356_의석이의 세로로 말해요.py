# import sys

# sys.stdin = open('swea_5356_의석이의 세로로 말해요.txt')

# 의석이랑 이제 안 놀아..
T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(str, input())) for _ in range(5)]
    new_arr = [[''] * 15 for _ in range(15)]
    # 새로운 2차원 리스트 생성
    for r in range(5):
        for c in range(len(arr[r])):
        # 각 row의 길이 만큼 돌면서 새로운 리스트에 갱신    
            new_arr[r][c] = arr[r][c]
    zip_arr = list(zip(*new_arr))
    # 행렬 전치
    result = []
    for r in range(15):
        for c in range(15):
            # zip_arr의 범위를 순회
            if zip_arr[r][c] == '':
                continue # 공백이면 건너뛰기
            else:
                result.append(zip_arr[r][c])
            # 아니면 결과값에 추가
    print(f'#{tc}', ''.join(result))