import requests
from pprint import pprint as print

cencored_user_list = {}

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

API_URL = 'https://jsonplaceholder.typicode.com/users' 


# def cencorship():
#     for i in black_list: # 블랙리스트 하나씩 훑기
#         if i in new_dict: # new dict에 블랙리스트 있는지 확인
#             print(f'{i} 소속의 {new_dict[i]} 은/는 등록할 수 없습니다.')
#             return False ## 함수의 반환값이 false 가 나오면 함수는 그대로 멈춤
#         else:
#             return True
# 그럼 함수에 for문을 넣지 말고 매개변수에 인수를 넣어야겠다.

def cencorship(company):
    if company in black_list:
        print(f'{company} 소속의 {new_dict[company]} 은/는 등록할 수 없습니다.')
        return False
    else:
        return True

new_dict = {}
company = None
name = []
def create_user():
    global new_dict
    global company
    global name
    global cencored_user_list
    company = None # 변수 청소
    new_dict = {} # 청소
    response = requests.get(API_URL) # API 요청
    parsed_data = response.json() # 데이터 > DICT 변환
    ## 여기까지 데이터 받아와서 dict 변경

    for i in range(10): ####### 10까지 밖에 안됨. API가 원인?
        name = [] # 리스트 청소 
        company = parsed_data[i]['company']['name'] # 회사명 변수
        name.append(parsed_data[i]['name']) # 명세에 있는 리스트로 이름 추가
        new_dict[company] = name # 회사명과 이름 매치 후 추가
        if cencorship(company): # 완성된 cencorship 함수 호출 / 계획대로 인수 삽입
            print('이상 없습니다.') # True 반환할 때 이상없습니다 출력
        else:
            cencored_user_list[company] = new_dict[company]
            # cencored_user_list.append(new_dict[company]) # False 일 때 name 추가
    ## 함수 완성

create_user() # 완성된 함수 호출
print(cencored_user_list) # 출력


###
# 47번 라인 range 제한
# 출력의 따옴표 지울 수 있는가
# .json() 이 뭔지



