# 켜져 있으면 1, 꺼져 있으면 0
T = int(input())
switch_lst = list(map(int, input().split()))
student_N = int(input())
for i in range(student_N):
    gender_type , num = map(int, input().split())
    # 성별 타입과 주어진 숫자
    if gender_type == 1: # 남자인 경우
        for j in range(num-1, T, num): # 지정된 번호 인덱스부터 num 간격으로
            if switch_lst[j] == 1: 
                switch_lst[j] = 0
            else:
                switch_lst[j] = 1 # 1이면 0으로, 0이면 1로
    elif gender_type == 2: # 여자인 경우
        num1 = num-1 # 뒤로 가는 숫자 정함
        num2 = num-1 # 앞으로 가는 숫자 정함.
        while num1 >= 0 and num2 < T and switch_lst[num1] == switch_lst[num2]:
            # 뒤로 가는 숫자 혹은 앞으로 가는 숫자가 범위를 벗어나거나 서로 다른 경우에 중단
            if switch_lst[num1] == 0 and switch_lst[num2] == 0: 
                switch_lst[num1], switch_lst[num2] = 1, 1
            else:
                switch_lst[num1], switch_lst[num2] = 0, 0 # 0인 경우에는 1로 아니면 0으로
            num1 -= 1
            num2 += 1 # 1씩 더하고 뺌
for i in range(0, T, 20):
    print(*switch_lst[i : i + 20])
