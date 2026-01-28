############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 제한 내장 함수:  len
# 기본 점수 (9점): 제한 내장 함수를 사용하여 해결
# 가산점(+3점): 제한 내장 함수 없이 직접 구현 (총 12점)

def count_long_words(words, min_length):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    try_num = 0
    # 시도 횟수 변수를 0으로 설정
    for word1 in words:
        spell = 0
        # 각 리스트의 단어의 객수를 매길 spell이라는 변수 설정
        for word2 in word1:
            spell += 1
            # spell에 for 문이 반복될때마다 1씩 추가해 단어 개수 파악
        if spell >= min_length:
            try_num += 1
            # spell에 저장된 정수 값이 min_length이상이면 출력값인 try_num에 1추가
    return try_num    

        
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(count_long_words(['apple', 'banana', 'cat', 'dog'], 4))  # 2 ('apple', 'banana')
print(count_long_words(['a', 'bb', 'ccc'], 5))                 # 0
#####################################################