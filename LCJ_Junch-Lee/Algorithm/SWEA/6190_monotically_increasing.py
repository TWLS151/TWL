import sys

sys.stdin = open('./input.txt', 'r')

T = int(input())

def multiply_sort(list, N):

    multi_num = []
    for i in range(N-1):                      # 리스트 내의 (끝-1) 원소에 대해
        for j in range(i+1, N):
            multi_num.append(list[i]*list[j]) # 다른 요소들과 모두 곱해 리스트에 할당

    multi_num.sort(reverse=T)                 # Hint! 내림차순 정렬 : 큰 값부터 단조증가를 검사하기 위함 !

    return multi_num


def is_monotic_increse(list1):                # 단조 증가값을 판단하는 함수

    str_list = list(map(str, list1))          # 1. 자리수 비교를 위해 int -> str

    for num in str_list:                      # 2. 리스트 안을 큰 값부터 검사
        is_increase = True                    # 초기 단조증가 여부 : True -> 처음 검사가 진행될 수 있도록

        if len(num) == 1:                     # 2-1. 한 자리수일 경우 -> 무조건 단조증가
            target = num

        for idx in range(len(num)-1):         # 3. 오른쪽 숫자를 검사 (끝 -1 자리까지)
            
            if is_increase is False:          # 3-1. 단조증가가 아닐 경우 : 안쪽 for 문을 벗어나 다음 숫자로
                break                        

            if int(num[idx]) <= int(num[idx+1]): # 3-2. 다음 자리수에 대해 단조증가 or 동일할 시: 다음 자리 수 검사
                is_increase = True

            else: is_increase = False

        else:                       # 4. 모든 자릿수 검사 이후

            if is_increase is True: # 4-1. 단조 증가일 시

                target = int(num)   # 해당 값이 목표값이므로 target에 할당
                break               # 반복문 강제 종료 (else로 넘어가지 않게)

    else: target = -1               # 4-2. 모든 값이 단조증가가 아닐 시 -> -1 반환


    return target



for tc in range(1, T+1):

    N = int(input())

    num_list = list(map(int, input().split()))

    multi_list = multiply_sort(num_list, N) # 1. 주어진 리스트의 모든 곱 요소를 계산 -> 내림차순 정렬 (큰 값부터 보기 위함)

    result = is_monotic_increse(multi_list)          # 2. 단조증가 여부 파악 -> 단조증가하는 최댓값 반환

    print(f"#{tc} {result}")

################################
# 수학적 개념 : 단조성 (by. Wikipedia)
# 모든 자리수에 대해 같거나 커지는, 같은 방향으로의 변화만 가지는 성질

# Q1. 모든 자릿수 값이 같다면? (ex. 111)
# >>> 단조증가, 단조감소 모두 해당한다.

# 무조건 커져야 하는 것이 아니다. 같아도 단조성을 가지는 것

# Q2. 한 자리수 값은 ? (ex. 5, 6)
# 비교할 자리 수가 없는 경우,
# 단조 증가에 대한 반례(왼쪽 > 오른쪽)를 찾을 수 없으므로, 단조성을 가진다고 간주함
# 심화 : 수학적 증명에서 '공허한 참(Vacuously True)'이라 불리는 논리적 약속


# test 1. 2 4 7 10
# 단조증가 최댓값 28 반환

# test 2. 2 3 10
# 단조증가 최대값 6 반환

# test 3. 2 10 11
# 단조증가 최대값 22 반환

# test 4. 2 10 20
# -1 반환 (단조증가 X)
