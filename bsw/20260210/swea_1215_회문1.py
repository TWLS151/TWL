import sys

sys.stdin = open('swea_1215_회문1.txt')
# 8 * 8로 주어짐.
for tc in range(1, 11):
    length = int(input())
    arr = [list(input()) for _ in range(8)]
    count = 0
    # 카운트 초기화
    for r in range(8):
        for c in range(8 - length + 1):
            if arr[r][c : c + length] == arr[r][c : c + length][::-1]:
            # 회문인 경우
                count += 1 # 갯수 1 추가

    zip_arr = list(zip(*arr)) # 전치
    for r in range(8): 
        # 전치된 리스트의 가로줄을 다시 검사(원래의 세로줄 검사)
        for c in range(8 - length + 1):
            if zip_arr[r][c : c + length] == zip_arr[r][c : c + length][::-1]:
                count += 1
    print(f'#{tc} {count}')