## Data Structure  

**데이터 구조**  
여러 데이터를 효과적으로 사용  
관리하기 위한 구조 (str, list, dict 등)  
= 자료구조  
단순히 데이터를 묶는 것을 넘어, 프로그램의 성능과 효율성, 유지보수성에 큰 영향을 미치는 핵심적인 개념이다.  

**method(메서드)**  
각 데이터 구조의 메서드를 호출하여 다양한 기능 활용 가능  
class 내부에 정의되는 함수이며, 각 데이터 타입 별로 다양한 기능을 가진 메서드가 존재한다.  

```데이터 타입 객체.메서드()```  

# 문제 풀다가 배운 것들

1. 딕셔너리에 키, 값 쌍 추가 혹은 값 수정
```python

# 사물함 [칸 이름] = 채울 내용
# key가 해당 딕셔너리에 없을 때 -> 새로 추가
d = {'name': 'Gemini'}
d['country'] = 'USA'  # 'country'라는 칸이 없으므로 새로 만듦

# 결과: {'name': 'Gemini', 'country': 'USA'}

# key가 해당 딕셔너리에 있을 때 -> 덮어쓰기 (수정)
d = {'name': 'Gemini'}
d['name'] = 'Flash'   # 'name' 칸에 있던 'Gemini'를 빼고 'Flash'를 넣음

# 결과: {'name': 'Flash'}


# 반복문 내에서 작동

for key, value in kwargs.items():
    new_dict[key] = value

# 1. kwargs.items(): "이름표=선물" 뭉치에서 하나씩 꺼냅니다.
# 2. 첫 바퀴: key는 'country', value는 'USA'가 됩니다.
# 3. new_dict['country'] = 'USA': new_dict 사물함의 'country' 칸에 'USA'를 넣습니다.
# 4. 다음 바퀴: 새로운 키와 값을 가져와서 똑같이 사물함에 넣습니다.
```

- 딕셔너리에 키, 값 쌍으로 추가 -> 딕셔너리 메서드 .update() 사용하기

```python

def add_item_to_dict(target_dict, key, value):
    new_dict = target_dict.copy()
    
    # 딕셔너리 메서드 사용: {key: value} 형태의 딕셔너리를 합쳐버림
    new_dict.update({key: value})
    
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
```