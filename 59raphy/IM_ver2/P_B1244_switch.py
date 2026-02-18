import sys

sys.stdin = open('input_p_switch.txt')

# T = 6
#
# for test_case in range(1, T + 1):
N = int(input())
switch = list(map(int, input().split()))
M = int(input())
students = [list(map(int, input().split())) for _ in range(M)]

for gender, switch_num in students:
    # 남학생
    if gender == 1:
        """
        for i in range(1, N // switch_num + 1):
            num = switch_num * i - 1
            switch[num] = 1 - switch[num]
        
        # range()의 step 인자 활용
        """
        for i in range(switch_num - 1, N, switch_num):
            switch[i] = 1 - switch[i]

    # 여학생
    else:
        # [PITFALL] 인덱스 넘버로 변경
        idx_num = switch_num - 1
        switch[idx_num] = 1 - switch[idx_num]
        j = 1

        while (idx_num - j >= 0 and idx_num + j < N
                and switch[idx_num - j] == switch[idx_num + j]):
            """
            switch[idx_num + j] = 1 - switch[idx_num + j]
            switch[idx_num - j] = 1 - switch[idx_num - j]
                
            # 한 줄로 합치기
            """
            switch[idx_num + j] = switch[idx_num - j] = 1 - switch[idx_num - j]
            j += 1

"""
K = N // 20
for k in range(K):
    switch_20 = switch[k*20:(k+1)*20]
    print(*switch_20)
print(*switch[K*20:])
    
# range()의 step 인자 활용
"""
for k in range(0, N, 20):
    print(*switch[k:k+20])


#=================================================================
# ver_1
# 260212

"""
for tc in range(1, T + 1):
    N = int(input())
    switch = list(map(int, input().split()))
    K = int(input())
    gender_num = [list(map(int, input().split())) for _ in range(K)]

    for gender, num in gender_num:
        # 남학생
        if gender == 1:
            M = N // num

            for i in range(1, M + 1):
                switch[i * num - 1] = 1- switch[i * num - 1]

        # 여학생
        if gender == 2:
            number = num - 1
            # 중심점 스위치 반전
            switch[number] = 1 - switch[number]
            j = 1
            # 리스트 범위를 벗어나지 않고 좌우 값이 같을 때까지 반복
            while (number - j >= 0 and number + j < N
                   and switch[number - j] == switch[number + j]):
                # 대칭인 두 지점을 가변 인자로 전달하여 반전
                switch[number - j] = switch[number + j] = 1 - switch[number - j]
                j += 1

    print(f'#{tc}')
    for i in range(0, N, 20):
        print(*switch[i:i + 20])
"""
