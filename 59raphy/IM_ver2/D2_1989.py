import sys

sys.stdin = open('input_1989.txt')

T = int(input())

for test_case in range(1, T + 1):
    word = input()

    # result = 1 if word == word[::-1] else 0

    result = 1
    N = len(word)

    for i in range(N // 2):
        if word[i] != word[N - 1 - i]:
            result = 0
            break

    print(f'#{test_case} {result}')
