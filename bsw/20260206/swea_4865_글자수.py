import sys

sys.stdin = open('swea_4865_글자수.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    word1 = input()
    word2 = input()
    # print(word1, word2)
    max_count = 0
    # 최댓값 미리 지정
    for i in range(len(word1)):
        count = 0
        for j in range(len(word2)):
            if word1[i] == word2[j]:
                count += 1        
            # 똑같은 문자가 있으면 카운트 +1
        if max_count < count:
            max_count = count
        # 최댓값 갱신
            count = 0
            # 카운트 초기화
    print(f'#{tc} {max_count}')