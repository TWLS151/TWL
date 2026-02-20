T = int(input())

for tc in range(1, T+1):

    E, N  = map(int, input().split()) # 간선 수 E, 노드 N을 루트로 하는 서브트리
    arr = list(map(int, input().split()))

    V = E + 1   # 마지막 정점 번호

    # 부모번호를 인덱스로 자식 번호 저장하는 배열
    c1 = [0]*(V+1) # 인덱스로 쓰기 때문에 V+1개
    c2 = [0]*(V+1)

    # 자식 번호를 인덱스로 부모 번호를 저장하는 배열
    par = [0] * (V + 1)


    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if c1[p] == 0: # 자식 1이 없으면
            c1[p] = c
        
        else: 
            c2[p] = c

        # 자식 번호를 인덱스로 부모 번호를 저장
        par[c] = p

    print(c1)
    print(c2)
    print(par)

    root = 0
    for i in range(V+1):
        if par[i] == 0:
            root = i
            break


# 5번 노드의 조상 찾기

c = 5
anc = []
while par[c] != 0:
    c = par[c]
    anc.append(c)

root = c