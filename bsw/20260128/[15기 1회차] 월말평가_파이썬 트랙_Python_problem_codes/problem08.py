############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def find_second_largest(numbers):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    for num1 in range(len(numbers)):
        if numbers[num1] == max(numbers):
            numbers.pop(num1)
            break
        # 최댓값을 만나면 그 인덱스에 위치한 값을 뺌.
    second_largest_value = numbers[0]
    for num2 in numbers:
        if num2 > second_largest_value:
            second_largest_value = num2
    # 다시 최댓값을 찾는 코드를 완성하여 두번째로 큰 값을 반환
    return second_largest_value
            
    
        

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_second_largest([1, 5, 3, 8, 2]))      # 5
print(find_second_largest([10, 10, 20, 5]))      # 10
#####################################################