# 앞 뒤를 확인하면서 검사
T = int(input())
for tc in range(1, T + 1):
    word = list(map(str, input()))
    result = 1
    # if len(word) % 2 == 0: <- 이건 필요 없겠죠?
    for i in range(len(word) // 2):
        if word[i] != word[-(i+1)]:
            result = 0
            break 
        else: 
            result = 1
    print(f'#{tc} {result}')

# 슬라이싱
T = int(input())
for tc in range(1, T + 1):
    word = input().strip()
    if word != word[::-1]:
        result = 0
        break
    else:
        result = 1
    print(f'#{tc} {result}')