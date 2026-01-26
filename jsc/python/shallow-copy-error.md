# 얕은 복사의 에러
26-01-26

## 개념
얕은 복사의 에러라는 것을 리스트 등을 복사를 해서 값을 쓸 때 값을 저장을 하는게 아니라 저장소의 위치를 저장을 하는것이다.
이것으로 인하여 에러가 발생을 한다. 

에러 코드
```py
import copy

# 원본: 중첩된 리스트
original = [[1, 2], [3, 4]]
# 얕은 복사 수행
shallow = copy.copy(original)

# 복사본의 내부 리스트 요소를 변경
shallow[0][0] = 'ERROR'

print(f"원본: {original}")  # 결과: [['ERROR', 2], [3, 4]]
print(f"복사본: {shallow}") # 결과: [['ERROR', 2], [3, 4]]
```

## 해결방법
copy.copy()가 아니라
copy.deepcopy()를 써야함

## 나의 질문
- shallow = original로 해도 original 값이 들어가는거 아닌가?
  - 이거와 shallow = copy.copy(original)과 뭐가 다른지 헷갈렸다. 결론은 shallow = original은 같은 것을 별명을 두개를 만들어준거다. 후자는 두개의 별개의 리스트인데 같은 주소를 나타낸거다.
- 왜 copy()가 아니라 copy.copy()인가?
  - A: copy라는 모듈안에 있는 여러개 중에서 copy()라는 함수를 가져오는 것이기 때문이다.
