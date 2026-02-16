'''
문제 조건
- 행/열의 일직선상 회문 중 가장 긴 회문의 길이
- 입력 배열은 100x100으로 고정
- 한 글자도 회문으로 인정 (최소길이 : 1)

접근
1. 행 단위 검사 -> 열 단위 검사 순으로
- strip()으로 한 글자씩 띄워 리스트 요소로 저장
(1) 짝수 회문 : idx == idx +1 이라면 -> 다를 때 까지 범위를 늘려가며 count = 2 += 2
(2) 홀수 회문 : idx-1 == idx +1 이라면 -> 다를 때 까지 범위 늘려가며 count = 3 += 2

2. 최대 회문 길이 갱신 로직 필요
3. 만약 최대 길이가 2 미만 -> 그냥 1 출력

TIL
1. 범위 검사 로직이 계속해서 필요하다면 -> in_range() 함수 분리
- 추후 DFS, BFS 등에서 유용하게 활용 가능

2. 전치를 활용해 행, 열 단위 검사를 모두 활용하고자 할 경우
- boards = [arr, list(map(list, zip(*arr)))]
-   board in boards:
- 위 코드 활용 가능

'''

import sys
sys.stdin = open('input.txt', 'r')

def in_range(x, N):
    return 0 <= x < N

def check_palindrome(arr):

    N = 100 # 배열 크기는 고정 (100 x 100)
    max_count = 0
    boards = [arr, list(map(list, zip(*arr)))]

    for board in boards:                      # 행 기준, 열 기준 arr를 차례대로 검사 (전치 활용)
        for r in range(N):                    # 1. 짝수 / 홀수 회문 검사
            count = 0                         # 행 변경 시 초기화
            for c in range(N-1):              # 인덱스 에러 방지 (마지막 -1 까지만 값 비교)

                if board[r][c] == board[r][c+1]:  # (1) 짝수 회문일 때 - ex. BAAB
                    count = 0
                    count += 2                # 길이 2인 회문 확보
                    i = 1                     # i : 다음 회문검사 인덱스 (1씩 증가)
                    while (in_range(c-i, N)
                           and in_range(c+1+i, N)
                           and board[r][c-i] == board[r][c+1+i]):   # cf. 범위 검사 팁 ? (함수 분리)

                        count += 2            # 다음 인덱스도 회문 -> 길이 +2
                        i += 1                # 그 다음 칸 탐색을 위해 인덱스 +1

                    else:
                        if max_count < count:
                            max_count = count

                elif (in_range(c-1, N)
                        and in_range(c+1, N)
                        and board[r][c-1] == board[r][c+1]): # (2) 홀수 회문일 때 (BAB)
                    count = 0
                    count += 3                           # 길이 3인 회문 확보
                    i = 2                                # +- 2 범위부터 탐색
                    while (in_range(c-i, N)
                           and in_range(c+i, N)
                           and board[r][c-i] == board[r][c+i]):

                        count += 2
                        i += 1

                    else:
                        if max_count < count:
                            max_count = count

    return max_count


for _ in range(1, 11):
    tc = int(input())
    arr = [list(input().strip()) for _ in range(100)]

    result = check_palindrome(arr)

    print(f"#{tc} {result}")

