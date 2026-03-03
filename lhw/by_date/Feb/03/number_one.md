# SWEA - 9386
## 연속한 1의 개수

- 개인적으로 너무 어려웠던 문제.. 피로감이 쌓여서 그런 건지 사고가 잘 안되어서 오래 걸렸습니다. 풀이도 정말 마음에 안드는 방식입니다. 추후 다시 풀이하겠습니다.


```python
# MY CODE

import sys
sys.stdin = open('nnnnn.txt')

TC = int(input())  # 테스트 케이스

# 테스트 케이스 순회
for test_case in range(1, TC + 1):
    N = int(input())
    strs = input()
    # 문자열 리스트화
    str_lst = [int(i) for i in strs]

    # 변수 설정
    cnt = 0
    
    # 카운트 기록용 리스트
    cnt_lst = []
    
    # 리스트화한 문자열 순회
    for i in str_lst:
        # i 가 1이면 카운트 증가 및 카운트 리스트에 추가
        if i == 1:
            cnt += 1
            cnt_lst.append(cnt)
        # i 가 0이면 카운트 초기화
        else:
            cnt = 0

    # 테스트케이스 번호와 최대 카운트값 출력
    print(f'#{test_case} {max(cnt_lst)}')


```