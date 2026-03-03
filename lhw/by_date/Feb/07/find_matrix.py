# SWEA - 1258
# 행렬찾기
# TTP: 64'42"

# 방문처리로 풀어보자

import sys

sys.stdin = open('find_matrix.txt')

import collections

TC = int(input())

for test_case in range(1, TC+1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]

    # 함수
    # 완전 탐색
    # 전치?
    # 그냥 전부 찾고
    # 행 한 번 다 훑고
    # 같은 수 세면 그게 열 아닌가?
    lst = []
    count = 0
    # 행렬 순회
    for row in range(size):
        for col in range(size):
            # 0이 아닌걸 찾으면 길이 측정 시작
            if matrix[row][col] != 0:
                count += 1
                # 다음이 0이면 기록 후 측정 종료
                if matrix[row][col+1] == 0:
                    lst.append(count)
                    count = 0

    # 기록된 길이에서 같은 값을을 카운팅
    mat_size = collections.Counter(lst)
    # 맵핑되어 있는 값들을 튜플로 추출
    size_lst = list(mat_size.items())
    # 문제에서 요구하는대로 정렬 (행과 열을 곱한 값이 작은 순, 행이 더 작은 순)
    size_lst.sort(key= lambda x: (x[0]*x[1], x[1]))
    
    # 출력, 요구사항에 맞추기 위해 언패킹 후 역순 출력
    print(f'#{test_case} {len(size_lst)}', end=' ')
    for x, y in size_lst:
        print(y, x, end=' ')
    print()