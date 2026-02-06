## **Python Module**

**모듈**  
한 파일로 묶인 변수와 함수의 모음  
특정한 기능을 하는 코드가 작성된 파이썬 파일  
- import 모듈명 사용
모듈명.변수명 or 모듈명.함수명()  
- from 모듈명 import 변수명, 함수명 사용  
그냥 바로 변수명 or 함수명()쓰면 됨  
- as 키워드 사용하여 별칭 부여 가능  
- 직접 정의한 모듈 사용 가능  

<br>

**패키지**  
연관된 모듈들을 하나의 디렉토리에 모아 놓은 것  
- 직접 패키지 만들어 사용 가능  
```python
from 폴더명.패키지명(그 아래 폴더명) import 모듈명
모듈명.함수명()
```

- 외부 패키지 다운  
``` $ pip install 패키지명```
```python
# requests 패키지 사용 예제
# requests 패키지 설치해야 정상 동작

import requests

# 공휴일 정보 API
url = "https://date.nager.at/api/v3/publicholidays/2026/KR"

# URL 주소에 요청을 보내서 응답 데이터를 받아 딕셔너리로 변경하는 코드
response = requests.get(url).json()
print(response)
```