# 깃 기본 사용법
26-01-26

## 깃 추가
git init

# 깃 연결
git remote add origin [url_address]

## 깃 클론
git clone [url_address]
git clone -b [branch_name] --single-branch [url_address]

## 깃 상태 확인
git status

## 깃 스테이징 area 이동
git add [file_name]
git add .

## 깃 커밋
git commit -m '[commit_message]'

## 깃 푸쉬
첫 푸쉬: git push -u origin main
이후 푸쉬: git push

## 깃 서명
git config

## 깃 자격
git credential

## 깃 가져오기
git pull
git pull origin [branch_name]

## 브랜치 확인
git branch

## 브랜치 생성
git switch -c [branch_name]