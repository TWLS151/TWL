# 리스트를 보면서 1이 있으면 count를 1 올리기, 아니면 count를 반환함. count 리스트에 추가, count의 최댓값을 계산

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input()))
    count = 0
    count_lst = []
    # 숫자를 셀 카운트와 카운트 갯수를 저장할 리스트 생성
    num2 = num + [0]
    # out of range를 방지하기 위해서 결과와 관계없는 0을 추가
    for i in range(N + 1):
        if num2[i] == 0:
            count_lst.append(count)
            if count == 0:
                count_lst.pop()
    # i가 N 범위를 순회하면서 0을 만나면 count리스트에 추가했다가 만약 횟수가 0이면 다시 뺌.
            count = 0
        else:
            count += 1   
        # 그 밖의 경우(1을 만났을 때)에는 count횟수를 1을 늘림.(0을 만날때까지 추가)        
    print(f'#{tc} {max(count_lst)}')
    # 모인 count 리스트 중에서 최댓값을 출력
    
