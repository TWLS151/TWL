############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 반드시 재귀 함수 형태로 구현해야 합니다.
def categorize_books(books):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # dict_list = {}
    # # 빈 dict 리스트 생성
    # for num in range (len(books)):
    #     if books[num]['category'] in dict_list.keys():
    #     # 만약에 dict_list에 이미 카테고리가 존재한다면
    #         [dict_list.values()].append(books[num]['title'])
    #         # 진행되는 카테고리에 해당하는 title을 원래 title에다가 추가함.
    #     dict_list.setdefault((books[num]['category']) , [books[num]['title']]) 
    #     # 빈 dict 리스트에 카테고리와 타이틀을 dict 형식으로 추가함.  
    # return dict_list

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
books_data = [
    {'title': 'Python Basic', 'category': 'IT'},
    {'title': 'Java Standard', 'category': 'IT'},
    {'title': 'History of World', 'category': 'History'},
    {'title': 'Cooking 101', 'category': 'Life'}
]
# 결과:
# {
#   'IT': ['Python Basic', 'Java Standard'],
#   'History': ['History of World'],
#   'Life': ['Cooking 101']
# }
print(categorize_books(books_data))
#####################################################