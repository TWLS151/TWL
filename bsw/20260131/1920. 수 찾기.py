import sys
input = sys.stdin.readline
# input()과 사용되는 목적은 비슷하지만 속도가 더 빠르며
# 줄바꿈 처리를 알아서 지워주는 input과 달리 그대로 포함
def call():
    return int(input())
def call2():
    return list(map(int, input().split()))
def call3():
    return set(map(int, input().split()))
# call : 정수 입력, call2 : 입력 값을 분리하여 리스트로
# call3 : 입력 값을 분리하여 집합으로
# 집합으로 한 이유는 어차피 포함 여부를 묻는 문제이고,
# gpt피셜 리스트보다 읽는 속도가 더 빠르다 하여 참고하였습니다.
call()
num_list1 = call3()
call()
num_list2 = call2()
# 정수, 집합, 정수, 리스트 순으로 입력
for num in num_list2:
    if num in num_list1:
        print(1)
    if num not in num_list1:
        print(0)
# 만약 리스트 안에 집합 안의 값이 존재하면 1 출력,
# 존재하지 않으면 0을 순서대로 출력