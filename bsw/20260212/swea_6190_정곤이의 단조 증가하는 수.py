import sys

sys.stdin = open('swea_6190_정곤이의 단조 증가하는 수.txt')
def danjo(number):
    number_str = str(number)
    for i in range(len(number_str) - 1):
        if number_str[i] > number_str[i+1]: # 뒷 자릿수가 앞 자릿수보다 작으면?
            return False
    return True

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    max_val = -1 # 안된다고 미리 가정
    for i in range(N - 1):
        for j in range(i+1, N): # 수를 구하는 과정
            sum_ = num[i] * num[j]
            if max_val < sum_: # 단조 확인
                if danjo(sum_): # 최댓값 여부 확인
                    max_val = sum_
    
    print(f'#{tc} {max_val}')