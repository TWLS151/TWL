# T 총 testcase
# K = 최대 이동 가능한 정류장 수
# N = 정류장 길이(종점 : b번 정류장)
# M = 충전기가 설치된 정류장개수
# char_lst = 충전기가 설치된 정류장

# 충전기 리스트에서 각 충전기 위치를 뺀것이 K보다 크면 바로 0 출력
# 그것이 아닐 때에는 마지막 충전 위치를 두고 정류장을 더 나아가면서
# K보다 커질 경우 충전을 시키고 마지막 충전 위치를 갱신

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    char_lst = list(map(int, input().split()))
    char_num = 0
    # 충전 횟수를 지정
    char_lst2 = [0] + char_lst + [N]
    # out of 충전기, 처음, 마지막 정류장 위치를 추가로 지정
    last_loc = 0
    # 충전 시킨 마지막 위치를 미리 지정
    for j in range(1, len(char_lst2)):
    # 정류장 쭉 돌기
        if char_lst2[j] - char_lst2[j-1] > K:
            char_num = 0
            break
    # 충전기 위치가 K 값을 벗어나면 바로 0으로 바꾸고 함수를 벗어남.
        else:
            if char_lst2[j] - last_loc > K:
                char_num += 1
                last_loc = char_lst2[j-1]
    # 현재 정류장 위치에서 마지막 위치를 뺐는데 K보다 크면
    # 현재 정류장에서 충전을 시키고 현재 정류장의 직전 위치를 마지막 위치로 지정
    print(f'#{tc} {char_num}')
