import sys
sys.stdin = open('sample_input_4828.txt')  #샘플 코드

T = int(input())  # 테스트 케이스를 입력받는다
for test in range(1, T+1):
    N = int(input())  # 각 케이스에 입력받을 양수의 개수
    arr = list(map(int, input().split()))  # 리스트 값들을 입력받는다
    print(f'#{test} {max(arr)-min(arr)}')  # 리스트의 최대값이랑 최소값을 빼서 출력
