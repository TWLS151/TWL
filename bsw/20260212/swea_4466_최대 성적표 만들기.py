import sys

sys.stdin = open('swea_4466_최대 성적표 만들기.txt')

T = int(input())
for tc in range(1, T + 1):
    N, S = map(int, input().split())
    score_lst = list(map(int, input().split()))
    score_lst.sort(reverse=True) # 점수를 내림차순으로 뒤집어서
    sum_ = 0 # 합계를 지정하고
    for i in range(S): # 과목 개수를 돌면서
        sum_ += score_lst[i] # 합계에 저장해주기만 하면 완료
    print(f'#{tc} {sum_}') # 최댓값을 출력할 필요 X(어차피 내림차순 정리했으니 최댓값임.)