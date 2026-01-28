############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 제한 내장 함수: map, max, sum
# 기본 점수 (9점): 제한 내장 함수를 사용한 해결
# 가산점(+3점): 제한 내장 함수 없이 직접 구현 (총 12점)

def sum_row_maximums(matrix):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    sum_value = 0
    # 합을 담을 값을 0으로 설정
    for num_list1 in matrix:
        max_value = num_list1[0]
        for num_list2 in num_list1:
            if num_list2 >= max_value:
                max_value = num_list2
    # 최댓값을 출력하는 과정(리스트 첫 변수를 최댓값으로 정하고 for문을 돌리면서 더 큰값을 만나면 대체)
        sum_value += max_value
    return sum_value 

   
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(sum_row_maximums([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # 18
print(sum_row_maximums([[-1, -2, -3], [-10, -5, -1], [-100, -200, -300]])) # -102
print(sum_row_maximums([[5]])) # 5
#####################################################