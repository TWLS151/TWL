T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    min_diff = -1 # 포장할 수 없는 상태라고 가정
    carrot_lst = list(map(int, input().split()))
    carrot_lst.sort()
    # 당근 리스트를 일단 오름차순으로 정렬
    for i in range(N-2): # 중, 대에 최소 1개가 담겨야 하기 때문
        if carrot_lst[i] == carrot_lst[i+1]:
            continue
            # 다음 인덱스와 같으면 continue(같은 크기 당근 사이에 경계 x)
        for j in range(i + 1, N-1): # 대에도 최소 1개
            if carrot_lst[j] == carrot_lst[j + 1]:
                continue
                # 중간 박스에서도 마찬가지
            if i + 1 > N//2 or j - i > N //2 or N - 1 -j > N // 2:
                continue
                # 각 박스가 과반수인 경우 못 들어감.
            current_diff = max(i + 1, j - i, N - 1 - j)- min(i + 1, j - i, N - 1 - j)

            if min_diff == -1 or current_diff < min_diff:
                min_diff = current_diff # 최대 최소 차이가 0 이상이면 갱신
    print(f'#{tc} {min_diff}')
    # i, j가 소, 중, 대를 나누는 범위를 정하는 과정