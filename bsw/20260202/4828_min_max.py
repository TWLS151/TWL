T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
# 1부터 T까지의 범위를 tc에 부여
    N = int(input())
    ai = list(map(int, input().split()))
    # 정수 N 값을 부여
    # 입력된 값을 정수처리 하여 ai에 리스트로 부여함.
    max_val = ai[0]
    min_val = ai[0]
    # 최대, 최솟값을 ai 리스트의 맨 앞의 값으로 임시 설정
    for j in range(N):
        if max_val < ai[j]:
            max_val = ai[j]
        # ai 리스트 중 더 큰 값이 있으면 최댓값을 변경
        if min_val > ai[j]:
            min_val = ai[j]
        # 더 작은 값이 있으면 최솟값으로 설정
    print(f'#{tc} {max_val - min_val}')
        # f-string 형식으로 최댓값과 최솟값의 차를 구함.