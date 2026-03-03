# SWEA - 1248
# 공통조상

import sys
sys.stdin = open('samesame.txt')

def findSame(idx):

    if idx == 0:

        if idx in val_lst:
            return idx
        
        else:
            left_val, right_val = left[idx], right[idx]

            if left_val in val_lst:
                val_lst.append(idx)
            elif right_val in val_lst:
                val_lst.append(idx)
            else:
                findSame(left_val)
                findSame(right_val)

def countTree(num):

    global count

    if num != 0:

        countTree(left[num])
        countTree(right[num])
        count += 1

    return count


TC = int(input())

for test_Case in range(1, TC+1):
    V, E, N, K = map(int, input().split())
    edge = list(map(int, input().split()))

    left = [0] * (V+1)
    right = [0] * (V+1)

    for idx in range(E):
        p, c = edge[idx*2], edge[idx*2 +1]

        if left[p] == 0:
            left[p] = c

        else:
            right[p] = c

    # dfs 만들고
    # 1 넣고
    # N, K 찾으면
    # 인덱스 반환 후 리스트 추가
    # 리스트에서 겹치는 부분 찾으면
    # 스택 ?
    # 인덱스 반환하고 리스트 추가하면서 안에 있으면
    # 리턴
    # 그리고 그거 재귀 넣어서 카운트
    # 가보자

    val_lst = [N, K]
    
    result = findSame(1)

    count = 0
    countTree(result)

    print(f'#{test_Case} {result} {count}')