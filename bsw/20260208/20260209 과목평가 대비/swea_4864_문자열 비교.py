T = int(input())
for tc in range(1, T + 1):
    word1 = input()
    word2 = input()
    for i in range(len(word2) - len(word1) + 1):
        if word2[i:i + len(word1)] == word1:
            result = 1
            break
        else:
            result = 0
    print(f'#{tc} {result}')
