############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# 제한 내장 기능: collections.Counter, List.count
# 기본 점수 (9점): 제한 내장 기능을 사용한 해결
# 가산점(+3점): 제한 내장 기능없이 직접 구현 (총 12점)

def count_menus(orders):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    order_list = {}
    for order in orders:
        if order in order_list:
            order_list[order] += 1
        # order_list에 order가 있으면 value값의 횟수를 1회 추가
        else:
            order_list[order] = 1
        # order가 없으면 새롭게 1을 생성
    return order_list
    
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(count_menus(['Ice Americano', 'Latte', 'Ice Americano', 'Mocha', 'Latte']))
# {'Ice Americano': 2, 'Latte': 2, 'Mocha': 1} (순서는 무관)
print(count_menus(['Cocoa', 'Cocoa', 'Cocoa'])) # {'Cocoa': 3}
#####################################################