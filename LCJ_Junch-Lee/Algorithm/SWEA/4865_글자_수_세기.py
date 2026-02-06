import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def remove_duplicate(list1):

    uni_list = []
    uni_list.append(list1[0]) # 입력되는 첫 값은 반드시 포함

    for i in range(len(list1)-1): # 마지막 -1자리까지
        for j in range(i+1, len(list1)): # i + 1부터 끝까지

            if list1[i] != list1[j] and list1[j] not in uni_list: # 값이 다르고, 없었던 값의 경우
                uni_list.append(list1[j])                         # uni_list에 추가

    return uni_list

def max_char(p, t): # p : pattern, t : target

    M = len(t) # 타겟의 길이
    max_count = 0

    for char in p: # pattern의 각 글자에 대해
        count = 0  # 글자 수 카운트 초기화
        for idx in range(M): # target의 문자를 순회하며

            if char == t[idx]:
                count += 1

        if max_count < count:
            max_count = count

    return max_count

for tc in range(1, T+1):

    p = list(input()) # 중복 제거를 위해 str의 한 글자씩 리스트
    t = list(input())

    uni_p = remove_duplicate(p)

    result = max_char(uni_p, t)

    print(f"#{tc} {result}")