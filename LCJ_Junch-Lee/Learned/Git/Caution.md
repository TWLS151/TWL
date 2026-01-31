## 1. Git의 push 조건

- 반드시 로컬과 Git 상의 이전 역사(commit)이 같아야 한다.


---

## 2. Clone과 pull
- README.md 파일 생성 옵션을 활성화 할 경우, 로컬에서 처음 내려받을 때는 push가 아닌 clone을 통해 받아야 함.
  
---

## 3. Github의 Initial commit 

 

- Github에서 먼저 생성한 경우, `.git`파일이 생성되어 있음, 이는 즉 `git init`이 지정되어 있는 상태임 

- `origin` 역시도 이미 내려받은 Repository로 지정이 되어있는 상태! 


## 4. Git credential 

- 원격 저장소(Git) 입장에서 본인에게 `push`하는 사용자가 원격 저장소에 권한이 있는 사람인지 확인하는 절차


- 팀 프로젝트를 진행할 경우, 레포지토리에 `Colaborator`를 지정하여 권한 부여

- 컴퓨터 변경 시 -> (이전 사용자가 있다면) git credential을 지워줘야 함
  - `자격 증명 관리자` 메뉴에서 확인


## 5. Git ignore 설정

- [gitignore.io](https://www.toptal.com/developers/gitignore/)
- 상기 링크를 통해 운영체제, IDE, 언어 별로 PJT에 포함되지 않아야 할 파일 리스트를 생성 가능
