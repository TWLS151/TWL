T = int(input())
result = 0
# 결과 값 0으로 지정
for i in range(1, T + 1):
    lst2 = []
    # 빈 리스트 생성
    lst1 = list(map(int, input().split()))
    # 여기에 for 문이 들어가야 할듯
for l in lst1:
    lst2.append(l)
    # lst1을 계속 input 하면서 lst2에는 lst1의 i번쨰 값을 추가
    # lst2는 세로 줄을 생성하려는 의도인데 아닌듯
for k in range (len(lst1)):
    if (lst1[k] in lst2[:k]) or (lst1[k] in lst2[k+1:]):
        continue
    else:
        result = 1
        # k를 제외한 부분에 수가 있으면 0 유지, 아니면 1로 바꿈
    if (lst2[k] in lst1[:k]) or (lst2[k] in lst1[k+1:]):
        continue
    else:
        result = 1
for j in range(3):
    lst3 = []
    for jj in range(3):
        for jjj in range(3):
            lst3.append(lst1[jjj])
            lst3.append(lst2[jjj])
    if lst1 [jj] in lst3:
        continue
    if lst2[jj] in lst3:
        continue
    else:
        result = 1
    # k 위치의 값이 lst1(가로줄)에 있으면 0 유지 , 아니면 1로 변경

    print(f' #{T} {result}')
    # print 값은 아직 수정 필요