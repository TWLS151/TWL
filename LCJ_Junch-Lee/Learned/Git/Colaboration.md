## 원격 저장소 (Remote Repository)

ex. 서비스 : GitLab, GitHub, Bitbucket

- Git으로 저장하는 프로젝트를 저장하는 Drive의 개념

### origin : 

- 추가하는 원격 저장소 별칭, url을 저장하는 변수



## remote (목적지 할당)

```bash
git remote add origin remote_repo_url

```
- 의미 : 내가 전달할 목적지는 `origin`이고, url은 `remote_repo_url`이다.


## push 

```bash

git push origin master

```

- git아, push해줘 origin 이라는 이름의 원격 저장소에 matser 라는 이름의 브랜치를 (master로 만든 commit들을)

- 내 로컬 repo에서 Git 서비스에 업로드 하는 것.

- 내 로컬 repository의 **commit을** 원격으로 업로드하는 것


### connect to GitHub 창이 또 뜨는 이유 ?


### cf. git config와의 차이점 

- config : '~가 썼음' 일종의 저자를 알리는 방법

- git push 이후 뜨는 'Sign in' : 일종의 창고지기가 Git 서비스의 Repository에 업로드 할 수 있는 권한이 있는 지를 확인하는 절차


## pull or clone (복제)

- #### pull : 원격 저장소의 변경사항'만' 가져옴
 
- 외부 저장소에서 내 Local Repo로 당겨오는 것

```bash

git pull origin master

```
- #### clone (다른 개발자) : 
- 원격 저장소 전체를 복제(다운로드)
```bash
git clone (remote_repo_url)
```


## gitignore

- Git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는데 사용되는 텍스트 파일
- 프로젝트에 따라 공유하지 않아야 하는 파일도 존재
  - ex. venv. .venv

- 이미 git에 추가가 된 파일의 경우, gitignore에 넣더라도 modified 처리가 됨

[gitignore 예시](https://www.toptal.com/developers/gitignore/api/python)

## Git revert

```bash

git revert <commit id> # commit id는 log로 확인, 최소 4자 이상 구분되게 입력할 것
```

- 특정 commit을 없었던 일로 만드는 작업
- commit에서 잘못된 작업을 수행했을 때

- 작동원리 : '재설정'
- 반드시 다른 commit을 추가해야 함 -> Git은 내 프로젝트의 기록을 남기는 것 (다른 개발자가 혼선을 겪지 않게끔)
- commit 기록에 'Revert commit"이라는 변경사항을 반전시키는 새 commit을 생성
- 순방향 실행 취소

## Git reset 

- 일종의 '되돌아가기' (과거로)



```bash

git reset [옵션] <commit id>

# 추가 옵션

--soft 
# 삭제된 commit들의 기록을 staging area에 남김
# 의미 : 삭제된 commit의 변경사항들이 다음 commit 상에 저장이 된다

--mixed #default
# 삭제된 commit들의 기록을 working directory에 남김

--hard
# 삭제된 commit들의 기록을 남기지 않음

```

- 되돌아간 commit 이후의 commit은 모두 삭제


## GitHub 활용

### 1. TIL : Today I Learned 

- 매일 내가 배운 것을 마크다운으로 정리해서 문서화시키기 

- 문서화의 중요성 : 스스로 학습한 내용을 정리하며 성장 가능, 팀에게 공유할 수 있는 능력 향상


## Git amend : 바로 직전 commit 수정하기

- vim 편집창이 뜨면서 메세지 수정 가능


## Gir restore : Modified 상태의 파일 되돌리기


## Unstage 명령어 :

- git restore --staged 
  - staging area에 추가된 변경 사항을 현재 버전으로 되돌리기
  - add 내역이 취소
  - 마지막 버전이 있어야 함, commit이 있어야 함

- git rm --cached 


## git reflog



