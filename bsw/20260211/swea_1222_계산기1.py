import sys

sys.stdin = open('swea_1222_계산기1.txt')


for tc in range(1, 11):
    _ = int(input())
    str_ = input()

    total_sum = 0
    for ch in str_:
        if ch.isdigit():
            total_sum += int(ch)
    print(f'#{tc} {total_sum}')



