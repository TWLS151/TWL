import sys
sys.stdin = open('input.txt', 'r')

# V = int(input())
# E = int(input())

# arr = [[0]*V for _ in range(V)] # 인접 행렬 연결 정보를 저장할 2차원 배열
# lst =[] # 인접 행렬 정보 (노드 - 노드)를 받을 리스트

# for _ in range(E):
#     lst.append(tuple(map(int, input().split()))) # 간선 수 만큼 연결 정보를 입력


# for i, j in lst: # i - j 노드간 연결 정보를 입력
#     arr[i][j] += 1

# for row in arr:

#     print(row)


# 인접 리스트

# 장점 : 연결 여부만 기록하는 개념 -> 구현 난이도 쉽고, 메모리 낭비가 적음
# 단점 : 연결 여부 확인을 위해서는 리스트를 탐색해야 하므로 인접 행렬에 비해 복잡도는 높다

# 1. dict 

V = int(input()) # 노드 개수
E = int(input()) # 간선 개수

adj_lst = {} # 노드 연결 정보를 저장하기 위한 리스트

for _ in range(E):

    key, value = map(int, input().split())

    if key not in adj_lst.keys(): # 해당 노드에 대한 연결 정보가 하나도 없다면 키를 추가하고 연결 노드 정보 리스트 생성
        adj_lst[key] = [value]

    if value not in adj_lst.keys():
        adj_lst[value] = [key]

    else: 
        adj_lst[key] += [value]
        adj_lst[value] += [key]

sorted_adj_lst = dict(sorted(adj_lst.items()))

print(sorted_adj_lst)

# [2 ,3, 4, 5, 7] -> for 