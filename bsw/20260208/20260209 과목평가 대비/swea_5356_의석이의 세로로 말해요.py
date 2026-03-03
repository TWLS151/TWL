# import sys

# sys.stdin = open('swea_5356_의석이의 세로로 말해요.txt')


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(str, input())) for _ in range(5)]
    arr2 = [[''] * 15 for _ in range(15)]
    for r in range(5):
        for c in range(len(arr[r])):
            arr2[r][c] = arr[r][c]
    zip_arr = list(zip(*arr2))
    result = []
    for r in range(15):
        for c in range(15):
            if zip_arr[r][c] == '':
                continue
            else:
                result.append(zip_arr[r][c])
    print(f'#{tc}', ''.join(result))
