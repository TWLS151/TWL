import sys
sys.stdin = open('med.txt')

def inorder(idx):

    # 정점의 정보가 2개밖에 없으면 정점 번호랑 문자밖에 없다.
    if len(info[idx]) == 2:
        # 정점 값 반환
        return info[idx][1] # 문자열

    # if len(node) == 2:
    #     return print(node[1], end=' ')
    # 정점의 정보가 3개이면 정점 번호, 문자, 왼쪽 자식의 정점 번호    
    elif len(info[idx]) == 3:
        left_idx = info[idx][2]

        # 왼쪽 먼저 보고 문자열 가져와서 내거랑 합쳐서 반환
        left_val = inorder(int(left_idx))
        return left_val + info[idx][1]
    
    # 정점의 정보가 4개인 경우 번호, 문자, 왼쪽, 오른쪽
    else:
        # 왼쪽 정보 먼저 가져와잇
        left_idx = int(info[idx][2])
        right_idx = int(info[idx][3])

        left_val = inorder(left_idx)
        right_val = inorder(right_idx)

        # 왼쪽 + 내거 + 오른쪽
        return left_val + info[idx][1] + right_val




for test_case in range(1, 11):
    V = int(input())
    info = [[] for _ in range(V+1)]

    for _ in range(V):
        node = input().split()
        # node[0]이 정점 번호
        info[int(node[0])] = node
        # info idx 에 idx 번호를 정점 번호로 하는 정점의 정보가 들어가있음.
    result = inorder(1)
    print(f'#{test_case} {result}')

