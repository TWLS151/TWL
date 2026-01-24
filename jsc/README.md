# TIL

> Today I Learned

배운 내용들을 컨텐츠별로 구분을 해서 올릴 생각입니다.
폴더 구조
영어공부도 하고 싶어서 익숙해지면 영어로 올리겠습니다.
거창하게 쓰지 말기.
추후에 github actions을 이용해서 README 목차 자동업데이트 하기.(강사님 추천해주신거..!)
성실하게 쓰기.

## ToDoList
[] 바이브 코딩 할 때 검증을 하는 방법 공부하기
[] 리드미 대시보드 자동화
    [예시: README.md에 자동으로 그려질 대시보드 형태] | 날짜 | 카테고리 | 주제 | 링크 | | :--- | :--- | :--- | :--- | | 2026-01-26 | Git | Cherry-pick 활용법 | Link | | 2026-01-25 | Java | JVM 메모리 구조 | Link | | 2026-01-24 | Python | List Comprehension | Link |

    README 대시보드 자동화 구현 방법
    개발자들이 만든 TIL-auto-readme 같은 스크립트가 있습니다.
    동작 원리: * 새로운 .md 파일을 폴더에 넣고 Push합니다.
    GitHub Actions가 이 파일을 감지해서 파일명에서 날짜와 제목을 추출합니다.
    최상위 README.md에 최신순으로 표를 다시 그려서 자동으로 커밋해줍니다.
    구체적인 적용 방법:
    Python이나 Node.js로 된 간단한 스크립트를 저장소에 넣어둡니다.
    .github/workflows/main.yml 파일을 만들어 "푸시할 때마다 스크립트 실행" 명령을 내립니다.


---
## Categories
* [Python](#python)
* [Git](#git)
* [Inbox](#inbox)


---
### Python


### Git


### Inbox

