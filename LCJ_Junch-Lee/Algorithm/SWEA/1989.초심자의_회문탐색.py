import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    word = input()

    N = len(word)

    for idx in range(N//2):
        if word[idx] != word[N -idx -1]:
            result = 0
            break

    else:
        result = 1

    print(f"#{tc} {result}")