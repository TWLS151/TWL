import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def calculate_maxlen(list): # 주어진 5개의 단어 중 가장 긴 단어의 길이를 출력하는 함수

    max_len = 0                     # 초기값 지정

    for word in list:               # 리스트 안의 각 단어에 대해

        if max_len < len(word):     # 최대 단어 길이를 갱신
            max_len = len(word)
    return max_len

def column_speak(list, N):          # 세로 읽은 값을 출력하는 함수

    words = ""                      # 세로로 읽은 결과물을 출력하기 위한 빈 문자열 지정

    for c in range(N):              # 열 : 단어의 최대 길이만큼
        for r in range(len(list)):  # 행 : 단어 리스트의 길이만큼

            if c < len(list[r]):    # 핵심 로직 : 현재 단어 길이보다 작을 경우에만 읽어야 함
                words += list[r][c]

    return words



for tc in range(1, T+1):

    arr = [input() for _ in range(5)] # 5개의 단어를 읽어옴

    N = calculate_maxlen(arr)

    result = column_speak(arr, N)

    print(f"#{tc} {result}")


