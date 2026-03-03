import sys

sys.stdin = open('swea_1961_숫자 배열 회전.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n_lst = [list(map(int, input().split())) for _ in range(N)]
    rotated_lst_90 = list(zip(*n_lst[::-1]))
    rotated_lst_180 = list(zip(*rotated_lst_90[::-1]))
    rotated_lst_270 = list(zip(*rotated_lst_180[::-1]))
    print_lst = [rotated_lst_90, rotated_lst_180, rotated_lst_270]
    for i in print_lst:
            for j in range(N):
                i[j] = ''.join(map(str, i[j]))
    print(f'#{tc}')
    for i in range(N):
        print(f'{rotated_lst_90} {rotated_lst_180} {rotated_lst_270}')
