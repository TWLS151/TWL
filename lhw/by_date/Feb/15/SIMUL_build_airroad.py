# SWEA - 4014
# 활주로 건설

import sys
sys.stdin = open('input.txt')


def check_slope(row):  # 매개변수 행
    cnt = 1  # 시작점까지 카운트
    for i in range(1, N):
        if row[i] == row[i-1]:
            cnt += 1  # 높이가 같으면 카운트 하나씩 추가
        elif row[i] - row[i-1] == 1 and cnt >= X:  # 높이가 1 높아지면
            cnt = 1  # 카운트 초기화
        elif row[i-1] - row[i] == 1 and cnt >= 0:  # 높이 1 낮아지면
            cnt = -X + 1
        else:  # 위에 해당하지 않으면 실패
            return 0
    if cnt >= 0:  # 다 통과해도 카운트가 음수면 실패
        return 1  # 양수면 성공
    return 0  # cnt 음수인 경우 실패


TC = int(input())
for test_case in range(1, TC+1):
    N, X = map(int, input().split())
    A = []
    result = 0
    for i in range(N):
        A.append(list(map(int, input().split())))
        result += check_slope(A[i])  # 행 넣을때마다 한 줄씩 판별


    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(A[j][i])
        result += check_slope(temp)  # 열 하나씩 만들어서 확인
    
    print (f"#{test_case} {result}")