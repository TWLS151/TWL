T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    idx = int(input()) # 개수를 입력받고
    lst = list(map(int, input().split())) # 값 입력받고
    mx = lst[0] 
    mn = lst[0] # 최대 최소 초기화
    for i in range(idx): # 개수가 틀리지 않았다는 가정 하에 인덱스로 치고 전체를 돌면서
        if mx < lst[i]:
            mx = lst[i] # 최대
        if mn > lst[i]:
            mn = lst[i] # 최소
    print(f'#{test_case} {mx - mn}') # 차 출력