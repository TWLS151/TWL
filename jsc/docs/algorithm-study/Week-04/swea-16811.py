"""
Docstring for TWL.jsc.docs.algorithm-study.Week-04.swea-16811
"""
import sys

sys.stdin = open('swea-16811.txt')

T = int(input())

for tc in range(1, T+1):
    carrot_num = int(input())
    half_carrot_num = carrot_num // 2
    carrots = list(map(int, input().split()))
    carrots.sort()
    min_diff = float('inf')

    for i in range (carrot_num-2):
        for j in range(i+1, carrot_num - 1):
            if carrots[i] == carrots[i+1]:
                continue
            
            if carrots[j] == carrots[j+1]:
                continue
            
            # 여기서 배운점은 continue를 하기위해서 변수 설정을 해야한다면 먼저 변수설정을 하고
            # 그 이후에 continue문을 써도된다.

            # 여기서 결국 원하는것은 갯수이기 때문에 슬라이싱이 아니라 수를 넣어도 된다.
            small = carrots[:i+1]
            middle = carrots[i+1:j+1]
            big = carrots[j+1:]

            if len(small) > half_carrot_num or len(middle) > half_carrot_num or len(big) > half_carrot_num:
                continue
            
            diff = (max(len(small), len(middle), len(big)) - min(len(small), len(middle), len(big)))

            if diff <= min_diff:
                min_diff = diff

    if min_diff == float('inf'):
        min_diff = -1
    
    print(min_diff)


# AI 피드백 ===
# 1. slicing을 쓸 데 없이 많이 하고 있다.
# 2. len함수 호출을 너무 많이 하고 있다.


import sys
from itertools import combinations

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()

    min_diff = float('inf')

    for i, j in combinations(range(N-1), 2):
        if carrots[i] ==




# ai풀이 ===

# T = int(input())



# for tc in range(1, T + 1):

#     N = int(input())

#     carrots = list(map(int, input().split()))

    

#     # 1. 당근을 크기순으로 오름차순 정렬

#     carrots.sort()

    

#     # 최솟값을 갱신하기 위해 초기값은 충분히 큰 수로 설정

#     min_diff = 1000 

    

#     # 2. 이중 for문으로 두 개의 경계선(i, j) 긋기

#     # i: '소' 상자의 마지막 당근 인덱스

#     # j: '중' 상자의 마지막 당근 인덱스

#     for i in range(N - 2):

#         for j in range(i + 1, N - 1):

            

#             # 3. 같은 크기 분리 금지 (가장 중요한 가지치기)

#             # 소 상자와 중 상자의 경계선에 있는 당근 크기가 같다면 쳐내기

#             if carrots[i] == carrots[i + 1]:

#                 continue

#             # 중 상자와 대 상자의 경계선에 있는 당근 크기가 같다면 쳐내기

#             if carrots[j] == carrots[j + 1]:

#                 continue

                

#             # 4. 각 상자에 담긴 당근 개수 계산

#             small = i + 1

#             medium = j - i

#             large = N - 1 - j

            

#             # 5. 과적 검사 (어느 한 상자라도 N // 2개를 초과하면 안 됨)

#             if small > N // 2 or medium > N // 2 or large > N // 2:

#                 continue

                

#             # 6. 모든 깐깐한 조건을 통과했다면? 차이의 최솟값 갱신!

#             diff = max(small, medium, large) - min(small, medium, large)

#             if diff < min_diff:

#                 min_diff = diff

                

#     # 7. 만약 조건을 만족하는 포장 방법이 단 하나도 없었다면 -1 출력

#     if min_diff == 1000:

#         min_diff = -1

        

#     print(f"#{tc} {min_diff}")