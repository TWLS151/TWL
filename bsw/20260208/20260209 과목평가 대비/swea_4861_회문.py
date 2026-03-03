T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = None
    for r in range(N):
        for c in range(N - M + 1):
            if arr[r][c:c + M] == arr[r][c :c +M][::-1]:
                result = arr[r][c :c + M]
                break
    if not result:
        for r in range(N):
            for i in range(N - M + 1):
                word_lst = []
                for c in range(M):
                    word_lst.append(arr[i + c][r])
                word = ''.join(word_lst)
                if word == word[::-1]:
                    result = word
                    break
    print(f'#{tc} {result}')
