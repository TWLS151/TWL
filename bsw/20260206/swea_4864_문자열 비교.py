import sys

sys.stdin = open('swea_4864_문자열 비교.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    word1 = input()
    word2 = input()
    N = len(word1)
    M = len(word2)
    
    for i in range(M - N + 1):
        # N<=M 이므로 M 문자를 도는 for문
        if word1 == word2[i:i + N]:
            result = 1
            break
            # break을 해주어야 다음까지 검사를 안 함.
        else:
            result = 0
    print(f'#{tc} {result}')