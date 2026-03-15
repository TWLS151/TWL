# 369 문제입니다. swea 1926

# 최근에 re 모듈을 학습했기에 연습을 해보고자 re 모듈을 이용해 해결해보려합니다.

import re

n = int(input())

first_lst = [] # 반복문을 통한 입력 리스트화
for i in range(1, n+1): 
    first_lst.append(i)

for d in first_lst: # 리스트 순회
    result = re.sub(r'[369]', '-', str(d)) # 문자열 순회하며 369 1차 제거
    if '-' in result:
        result = re.sub(r'[0-9]', '', result) # 369가 있던 문자열이 있으면 남은 숫자 2차 제거 // 제거하지 않으면 13은 1- 으로 출력됨
    print(result, end=' ') # 출력

#---------------------------------#
# 광민님 코드
# 반복문과 조건문을 활용하여 깔끔하게 해결

# n=int(input())
# for i in range(1,n+1):
#     cnt=0
#     lst=list(str(i))
#     cnt+=lst.count('3')
#     cnt+=lst.count('6')
#     cnt+=lst.count('9')
#     if cnt==0:
#         print(i,end=' ')
#     else:
#         print('-'*cnt,end=' ')
    
    