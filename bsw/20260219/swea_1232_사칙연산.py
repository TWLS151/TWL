def calc(node):

    if len(tree[node]) == 2: # 둘다 숫자인 경우
        return int(tree[node][1])
    
    else:
        L = calc(int(tree[node][2])) # 왼쪽 자식
        R = calc(int(tree[node][3])) # 왼쪽 자식
        op = tree[node][1] # op는 연산자
        
        if op == '+': 
            return L + R
        elif op == '-': 
            return L - R
        elif op == '*': 
            return L * R
        elif op == '/': 
            return L // R


for tc in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N + 1)] # N + 1로 저장하여 1부터 세기

    for _ in range(N):
        temp = input().split()
        tree[int(temp[0])] = temp
    
    print(f'#{tc} {calc(1)}')
