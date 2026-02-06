import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) # 테스트 케이스

def find_palindrome(arr, N , M):

    # 1. 기준점부터 M의 거리만큼 탐색 (i : 0 ~ N - M + 1, j : M/2))
    # 행 단위의 탐색만 진행, 없을 경우 전치해서 열-> 행으로
    for idx in range(N):
        row = arr[idx]

        for i in range(N - M + 1): # 2. 회문 탐색의 시작점 범위


            for j in range(M//2):  # 자릿수 검사용 # 0 1 2 3 4 (range(5))

                if row[i+j] != row[i + M -1 -j]: # Hint 2: 회문의 비교 지점에 대한 부분 !!!
                    is_palindrome = False
                    break

            else:                         # 3. 회문 검사를 끝까지 마쳤을 경우
                if is_palindrome is True: # 회문 여부를 True로 지정
                    target = "".join(row[i:i+M])
                    return target


for tc in range(1, T+1):

    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    result = find_palindrome(arr, N, M)    # 행 단위 회문 검사

    if result is None:                     # 만약 행에 회문이 없을 경우

        t_arr = list(map(list, zip(*arr))) # 문자열 전치

        result = find_palindrome(t_arr, N, M) # 열 단위 회문 검사

    print(f"#{tc} {result}")
########################################################
# GPT 참고 아이디어 정리

# 1. for row in arr 가 아닌  for idx in range(N):인 이유?
# 행 -> 열로의 확장성을 확보하기 위해

# 2. 회문의 비교 지점?
# 집중력의 차이이긴 하나,
# 우리가 쓰는 i, j 인덱스에 대해 경우의 수를 직접 계산해보며 규칙을 찾는 것이 좋겠다

# 3. 함수 기능에서 return 이후의 동작?
# feat. 중첩 반복문 탈출
# 함수로 기능을 정의해 원하는 결과값이 나왔을 경우, 바로 중단하고 싶다면
# return을 원하는 결과 (조건) 검사 이후에 바로 이어서 작성
# 그 이후 반복은 돌지 않고 자동 종료.

