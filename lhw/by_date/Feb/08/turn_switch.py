# BOJ - 1244
# 스위치 켜고 끄기
# Fail: 26'59"



import sys
sys.stdin = open('turn_switch.txt')

num_switch = int(input())
# state_switch = [0]
state_switch = [-1] + list(map(int, input().split()))
num_student = int(input())


# 남학생은 스위치 번호가 자기가 받은 수의 배수이면 그 스위치의 상태를 바꾼다
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서
# 가장 많은 스위치를 포함하는 구간을 찾아서 바꾼다.

# 남학생은 배수
# 여학생은 대칭

def switch(switch_number):
    state = state_switch[switch_number]
    return 1 - state

for num in range(num_student):
    gender, number = map(int, input().split())
    plus = 1

    if gender == 1:
        for i in range(number, num_switch + 1, number):
            state_switch[i] = switch(i)
    
    else:
        state_switch[number] = switch(number)
        while number + plus < num_switch and number - plus >= 0 and state_switch[number + plus] == state_switch[number - plus]:
            state_switch[number + plus] = switch(number + plus)
            state_switch[number - plus] = switch(number - plus)
            plus += 1

for i in range(1, num_switch+1):
    print(state_switch[i], end=' ')
    if i % 20 == 0:
        print()
