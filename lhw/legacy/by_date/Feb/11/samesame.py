# SWEA - 1248
# 공통조상

import sys
sys.stdin = open('samesame.txt')

def dfs(node, depth):
    # 해당 노드의 깊이 기록
    depths[node] = depth
    # 노드 사이즈 1 기록
    subtree_size[node] = 1
    # 그래프에서 해당 노드 인접 노드 순회
    for child in treeinfo[node]:
        # 부모 리스트에서 부모 탐색
        parent[child] = node
        # 자식 노드의 자식노드 탐색 및 깊이 1 추가
        dfs(child, depth + 1)
        # 자식노드에서 찾아온 사이즈를 부모 사이즈에 병합
        subtree_size[node] += subtree_size[child]

def lca(a, b):
    # 깊이가 다르면 깊이를 맞춰준다 (동시탐색을 하기 위해)
    while depths[a] != depths[b]:
        # a 가 더 크면
        if depths[a] > depths[b]:
            # a의 부모를 불러오고
            a = parent[a]
        # 아니면
        else:
            # b의 부모를 불러온다.
            b = parent[b]
    # a와 b가 다르면 (깊이는 맞춰짐)
    while a != b:
        # 둘 다 부모를 불러온다
        a= parent[a]
        b= parent[b]
    # 값이 같아지면 (부모가 같아지면) 부모 반환
    return a


TC = int(input())

for test_case in range(1, TC+1):
    V, E, n, k = map(int, input().split())
    edge = list(map(int, input().split()))

    # 인접 리스트 그래프 생성
    treeinfo = [[] for _ in range(V+1)]
    # 간선 순회하며 리스트 채워넣기
    for i in range(E):
        p, c = edge[i*2], edge[i*2 + 1] 

        treeinfo[p].append(c)

    # 필요한 리스트 생성
    # 깊이
    depths = [0] * (V + 1)
    # 서브트리 사이즈 (문제 요구사항)
    subtree_size = [0] * (V + 1)
    # 해당 인덱스의 부모 정보 저장
    parent = [0] * (V + 1)
    # 전처리 함수 호출
    dfs(1, 0)
    # lca 함수 호출
    anc = lca(n, k)

    print(f'#{test_case} {anc} {subtree_size[anc]}')

















# def findSame(idx):

#     if idx == 0:

#         if idx in val_lst:
#             return idx
        
#         else:
#             left_val, right_val = left[idx], right[idx]

#             if left_val in val_lst:
#                 val_lst.append(idx)
#             elif right_val in val_lst:
#                 val_lst.append(idx)
#             else:
#                 findSame(left_val)
#                 findSame(right_val)

# def countTree(num):

#     global count

#     if num != 0:

#         countTree(left[num])
#         countTree(right[num])
#         count += 1

#     return count


# TC = int(input())

# for test_Case in range(1, TC+1):
#     V, E, N, K = map(int, input().split())
#     edge = list(map(int, input().split()))

#     left = [0] * (V+1)
#     right = [0] * (V+1)

#     for idx in range(E):
#         p, c = edge[idx*2], edge[idx*2 +1]

#         if left[p] == 0:
#             left[p] = c

#         else:
#             right[p] = c

#     # dfs 만들고
#     # 1 넣고
#     # N, K 찾으면
#     # 인덱스 반환 후 리스트 추가
#     # 리스트에서 겹치는 부분 찾으면
#     # 스택 ?
#     # 인덱스 반환하고 리스트 추가하면서 안에 있으면
#     # 리턴
#     # 그리고 그거 재귀 넣어서 카운트
#     # 가보자

#     val_lst = [N, K]
    
#     result = findSame(1)

#     count = 0
#     countTree(result)

#     print(f'#{test_Case} {result} {count}')