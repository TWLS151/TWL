# Put-Dictionay-In-A-List
> 리스트안에 딕셔너리 형태로 key, value값 같이 넣기

TS
- S
  - WS-05
  - 26-01-25
- T
  - 리스트 안에 dictionary로 key, value 넣기
- A
  - [x]try1: .items()을 사용
  ex: list_name.append(data.items('company'))
  reuslt: items는 key값을 특별하게 지정을 할 수가 없다.
  - [o]try2: ('key': 'value')로 append
  ex: list_name.appen('company': data.get('company'))
  result: success
- R
  - list에 dictionary형태로 넣을 때에는 'key': 'value' 형태로 넣자