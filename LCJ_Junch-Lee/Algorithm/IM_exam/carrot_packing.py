'''
문제 조건

1. N개의 당근 -> 대, 중, 소 상자에 나눠서 담아야 함
2. 같은 크기의 당근은 같은 상자에
3. 비어있는 상자가 있으면 안 됨
4. 한 상자에 절반이 넘는(N//2 초과) 당근이 들어가면 안 됨
5. 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장해야 함

접근

Hint 1. '임의 분배'가 아니라, -> '구간 나누기'에 가깝다.

Hint 2. 정렬 이후 i, j를 구간의 경계값으로 설정
-> arr[0:i] , arr[i:j], arr[j:N] ->

Hint 3 : 같은 숫자끼리는 '같은 그룹'으로 묶는다
-> 이후 그룹 단위의 개수를 세서 최적의 분리점을 찾는다

Hint 4 : 그룹 (같은 수) 배열을 하나 만들고, 분할점 두개를 고르는 문제로 생각

'''

def grouping_carrot(arr, N):
    '''
    같은 크기의 당근을 묶어 그룹으로 보자!
    그룹 내의 당근 수 배열을 반환하는 함수
    '''
    arr.sort() # 크기 비교를 위한 정렬
    groups = []
    count = 1

    # 1. 당근 배열을 순회하면서 같은 크기의 당근끼리 그룹화
    for idx in range(1, N):

        if arr[idx] == arr[idx-1]:
            count += 1

        else: #이전 값이 현재 값과 다르면
            groups.append(count)
            count = 1
    else: groups.append(count) # 마지막 그룹 업데이트

    return groups

def pack_difference(arr): # 몇 개의 그룹을 포함할 것인가?

    G = len(arr) # N : 그룹의 개수
    prefix = [arr[0]] # prefix : 누적합 배열

    if G < 3:
        return -1

    min_diff = 10000

    for idx in range(1, G):
        prefix.append(prefix[idx-1] + arr[idx])


    # 핵심 : i와 j는 경계선 값이다. arr[:i], arr[i:j], arr[j]
    for i in range(G-2): # 그룹 수 만큼 순회
        for j in range(i+1, G-1): # 해당 그룹을 제외한 나머지 그룹 범위

            S = prefix[i]
            M = prefix[j] - prefix[i]
            L = prefix[G-1] - prefix[j]

            if S > N//2 or M > N//2 or L > N//2: # 불가능한 포장은 skip
                continue

            diff = max(S,M,L) - min(S,M,L)

            if min_diff > diff:
                min_diff = diff

    if min_diff == 10000: # 갱신되지 않았다면
        return -1
    else: return min_diff


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N = int(input()) # 당근 수

    arr = list(map(int, input().split()))

    grouped_carrot = grouping_carrot(arr, N)

    result = pack_difference(grouped_carrot)

    print(f"#{tc} {result}")
