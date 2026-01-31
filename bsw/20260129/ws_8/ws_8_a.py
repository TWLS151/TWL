
# 아래에 코드를 작성하시오.
data = {'name' : '홍길동'}
try:
    data['age'] = 30
    print(data)
except KeyError:
    print('data에는 age라는 키가 없습니다.')
    data.update(age = 30)
    print(data)



    
arr = ['반갑', '하세요', '안녕']


# 아래에 코드를 작성하시오.
try:
    for i in range(4):
        print(arr.pop())
except IndexError:
    print([])
    print('더 이상 pop 할 수 없습니다.')


word = '3.15'

# 아래에 코드를 작성하시오.
try:
    print(int(word))
except ValueError:
    print('정수로 변환 가능한 값을 입력해주세요.')