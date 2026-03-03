import sys

sys.stdin = open('swea_1974_스도쿠 검증.txt')

# 가로,세로, 사각형 순으로 검사하면서 set의 길이가 9인지 아닌지의 여부를 검사
T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        if len(set(arr[i])) != 9:
            result = 0
            break
    if result: # 위에서 예외를 발견하지 못했을 때
        zip_arr = list(zip(*arr)) # 전치
        for i in range(9):
            if len(set(zip_arr[i])) != 9:
                result = 0
                break
    if result:
        for squ1 in range(0, 9, 3):
            for squ2 in range(0, 9, 3):
                num_lst = []
                for r in range(3):
                    for c in range(3):
                        num_lst.append(arr[squ1 + r][squ2 + c])
                if len(set(num_lst)) != 9:
                    result = 0
                    break
    print(f'#{tc} {result}')