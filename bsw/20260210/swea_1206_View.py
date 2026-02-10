import sys

sys.stdin = open

for tc in range(1, 11):
    N = int(input())
    b_lst = list(map(int, input().split()))
    sum_ = 0 # 합계 지정
    for i in range(2, N- 2): # 어차피 양끝 두 개에는 0이 붙어있어서 상관 X
        v_lst = [b_lst[i-2],
                 b_lst[i-1],
                 b_lst[i],
                 b_lst[i+1],
                 b_lst[i+2]]
        if b_lst[i] == max(v_lst): # 현재 위치가 주변 대비 최대일때,
            v_lst2 = [b_lst[i-2],
                 b_lst[i-1],
                 b_lst[i+1],
                 b_lst[i+2]]
            sum_ += b_lst[i] - max(v_lst2) # 현재 위치를 제외한 건물에서 최대 높이의 건물 높이 빼기
    print(f'#{tc} {sum_}')
