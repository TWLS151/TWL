# 파리 잡기 문제입니다.
# 전체 코드는 파일 하단부에 넣겠습니다.

'''
쉽지만은 않은 문제였습니다.
문제 특성상 분기처리를 해야하는데 분기처리 하기가 너무너무너무너무 귀찮아서 한번에 해결하려 머리를 써봤지만 결국 실패했습니다.
'''
try:
    if i-k <= 0 or j-k <= 0:
        raise IndexError("negative is not allowed")
    plus_sum += arr[i][j-k] + arr[i][j+k] + arr[i-k][j] + arr[i+k][j]
    
except IndexError:
    pass
'''
위 코드가 문제의 코드인데 인덱스가 음수로 넘어가면 리스트 끝부분이 인풋이 들어온다는 걸 알고
음수가 되면 에러처리를 하려고 머리를 써봤습니다만 그렇게되면 그 경우의 수 자체를 버리는 결과가 되어버려서 결국 포기했습니다.

그 과정에서 원래 몰랐던 raise 라는 기능을 알게되었고 이는 if 문에 넣어 조건이 달성되면 자동으로 에러를 띄우는 기능을 가지고 있었습니다.
자세히는 잘 모르지만 알아두면 어느정도 쓸모가 있어 보입니다.
'''

#-------------------------------------------#

T = int(input()) # 테스트 케이스 개수

def plus(arr): # 십자 모양 스프레이 함수 정의
    plus = [] # 각 경우의 수 담을 리스트
    for i in range(len(arr)): 
        for j in range(len(arr[i])): # i, j 행렬 순회 이중 for 문
            plus_sum = arr[i][j] # 초기값 설정
            for k in range(1, M): # 반복문으로 M 범위 파리 수 합산
                # 각 인덱스가 음수이거나 리스트 범위를 초과하면 생략하도록 분기처리
                # 파이썬 특성상 리스트 인덱스가 음수가 되면 역순으로 탐색하기 때문에 생략해야함
                if i+k < N:
                    plus_sum += arr[i+k][j]
                if j+k < N:
                    plus_sum += arr[i][j+k]
                if i-k >= 0:
                    plus_sum += arr[i-k][j]
                if j-k >= 0:
                    plus_sum += arr[i][j-k]
            
            plus.append(plus_sum) # 경우의 수 리스트에 추가
    return max(plus) # 그 중 최대값 리턴

def x(arr): # x 모양 함수로 십자모양과 구조는 같으나 인덱스 계산 부분만 차이가 있음
    x = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            x_sum = arr[i][j]
            for k in range(1, M):
                if i+k < N and j+k < N:
                    x_sum += arr[i+k][j+k]
                if j+k < N and i-k >= 0:
                    x_sum += arr[i-k][j+k]
                if i-k >= 0 and j-k >= 0:
                    x_sum += arr[i-k][j-k]
                if j-k >= 0 and i+k < N:
                    x_sum += arr[i+k][j-k]
            x.append(x_sum)
    return max(x)


for test_case in range(1, T+1): # 반복 및 테스트 케이스 출력을 위한 반복문
    N, M = map(int, input().split()) # N 과 M 입력
    arr = [list(map(int, input().split())) for _ in range(N)] # 컴프리헨션을 이용한 주어진 행렬 입력

    # 각 함수 호출
    fly_plus = plus(arr)
    fly_x = x(arr)

    # 둘 중 더 큰 값 출력
    print(f'#{test_case} {max(fly_plus, fly_x)}')