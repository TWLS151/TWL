
# for문을 이용해 API로 받아온 데이터를 순회하며 원하는 카테고리를 찾으며 그 수를 카운팅 할 수 있는 코드

# 도서 수 카운팅
book_data, publisher_counts = []
for book in book_data:
    if book["publisher"] in publisher_counts: # 카운팅이 되고 있으면 +1
        publisher_counts[book["publisher"]] += 1
    else:                                     # 카운팅이 안 되고 있으면 1로 설정
        publisher_counts[book["publisher"]] = 1

#---------------------------------------------------------------#

# 위의 코드를 활용 해 기능을 추가한 코드

# Dictionary 의 'key'에 f-string 을 넣을 수 있다는 점을 배웠습니다.
# 카테고리의 수를 카운팅 하는 건 간단히 할 수 있었는데 그 카테고리의 데이터를 새로운 키값에 할당하는 코드를 작성하는데 애를 먹었습니다.

data, category_stats = []
for book in data: # 카테고리별로 도서 수와 가격을 집계하는 코드
        if book['categoryName'] in category_stats: ## 스탯딕셔너리 안에 category 키가 없으면 추가 및 카운팅
            category_stats[book['categoryName']] += 1 
            category_stats[f"{book['categoryName']} price"] += book['priceSales']
            # f-string을 활용한 본래 key 값이 포함되는 새로운 key 값을 갱신
        
        else :
            category_stats[book['categoryName']] = 1
            category_stats[f"{book['categoryName']} price"] = book['priceSales']
            # 처음 집계될 때, 키값이 존재하지 않을때는 키값을 생성.

#--------------------------------------------------------------#

# None-sequence Data 인 Dictionary 를 정렬할 수 있는 코드

# .items 메서드를 활용해 딕셔너리를 튜플 구조로 뽑아내고 그 튜플을 정렬함으로서 딕셔너리를 정렬하는 것과 같은 기능을 하는 코드
# 후에 'key' 함수와 lambda 를 이용해 튜플의 몇 번 인덱스를 기준으로 정렬할 것인지도 결정할 수 있음
data_dict = {}
sorted_dict = sorted(data_dict.items(), key = lambda x: x[1])
# 딕셔너리에서 뽑아낸 튜플의 1번 인덱스 {(x, y)에서 y} 를 기준으로 오름차순 정렬.

#----------------------------------------------------------------#

######################
#   딕셔너리 분기처리   #
######################

# 다뤄본 데이터 중 대규모에 속하는 데이터를 처리한 문제
# 처음 봤을 때 분기마다 변수를 하나씩 만들어 마지막에 변수를 한데 모아 처리를 하려했으나 코드가 너무 복잡해져 폐기 후 추가 변수 없이 처리
# 복잡한 딕셔너리 구조를 처리하느라 조금 머리가 아팠지만 하다보니 점점 익숙해지긴 했습니다. 조금 더 공부해서 개선할 계획입니다.

user_data = 'input 데이터'
black_list = 'list'
blood_types = 'list'

fault_list = [] # global로 사용할 리스트
user_list = []
count = 0
def is_validation(num):
    global fault_list # 글로벌 변수 호출
    fault_list = [] # 함수가 호출 될때마다 청소
## 블랙리스트에 있으면 바로 종료해야하기 때문에 제일 먼저 확인 // 명세
    if user_data[num]['company'] in black_list:
        return 'blocked'
## 혈액형
    if user_data[num]['blood_group'] not in blood_types:
        fault_list.append('blood_group')
## 메일
    if '@' not in user_data[num]['mail']:
        fault_list.append('mail')
## 이름
    if len(user_data[num]['name']) <= 2 or len(user_data[num]['name']) >= 30:
        fault_list.append('name')
## 사이트
    if len(user_data[num]['website']) == 0:
        fault_list.append('website')
## 각 분기마다 조건 해당 시 Fault_list 에 추가해 fault가 있었는지 확인
    if len(fault_list) >= 1: # fault_list가 True가 되면 False가 있었다는 것이니 False 반환 및 False 를 반환한 사한 동시 반환
        return False, fault_list # 명세에 리스트로 반환하라는 내용이 있어 리스트로 반환
## 전부 통과하면 True 반환    
    return True

def create_user(num):
    global user_list # 함수 밖에서 출력해야해서 글로벌
    global count # 위와 동일
    if is_validation(num) == 'blocked': # blocked 는 표시 생략하니 pass
        count += 1 # blocked count 추가
        pass
    if is_validation(num) == True:
        user_list.append(user_data[num]) # True 면 모든 데이터 표시
    else:
        user_list.append(user_data[num]) # False 면 추가하고 해당 데이터 None 재할당
 # list 만들어뒀으니 사용해 하나씩 확인 / global로 해야할듯
        for i in fault_list:
            user_list[num][i] = None # fault 값에 None 할당
        count += 1 # False count 추가

## 주어지는 user_data 의 수 만큼 반복
for num in range(len(user_data)):
    create_user(num)

## 출력
print(f"잘못된 데이터로 구성된 유저의 수는 {count} 입니다.") # blocked 와 False 가 있던 유저 수 반환
print(user_list) # 정상 데이터 출력