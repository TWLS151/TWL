# range(), set

## range()
range는 숫자의 범위를 말을 하는 거다.
range(start, stop, step)이런 형식이다.
start부터 시작을 해서 stop의 숫자 직전까지만 된다.

for i in range(len(list_name)) 이런 방식으로 사용을 한다면 
i의 값과 인덱스의 값이 일치가 되어서 자주 사용하게 된다.


## set
중괄호로 이루어져있다. set은 중복되는 값을 없애준다. 그리고 순서대로 나열을 하기 때문에 인덱싱으로 값을 꺼낼 수 없다.
하지만 for문을 사용을 해서 값을 하나씩 순회를 하면서 꺼내 올 수가 있다. 또는 list()을 사용을 해서 리스트로 바꿀 수도 있다.
빈 set을 만들 때 문제가 있다. a = {}을 하면 set이 아니라 빈 딕셔너리가 만들어진다. 따라서 a = set()을 사용을 해야 빈 set을 만들 수 있다.
예시
```
fruits = {"apple", "banana", "cherry"}
```
