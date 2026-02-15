# 오늘은 문제 풀면서 FILTER를 배위ㅓㅆ어요!!!




필터 함수 쓸만해요

이거 보세용

```python

small = list(filter(lambda x : x <= size_of_carrots[sep[0]],carrots))
medium = list(filter(lambda x : x > size_of_carrots[sep[0]] and x <= size_of_carrots[sep[1]],carrots))
large = list(filter(lambda x : x > size_of_carrots[sep[1]], carrots))
        # print(small)

```


이렇게 하면 원하는 값들을 리스트로 부터 추출해서 새로운 리스트들을 만들 수 있습니다.


람다와 활용할 수 잇는게 참 좋은거 같아요.

이걸하면 퀵소트도 쉽게 짤 수 있어요.