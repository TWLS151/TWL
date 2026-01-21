# 6단계: Pull Request 스쿼시 앤 머지

승인된 Pull Request를 스쿼시 앤 머지로 develop 브랜치에 병합합니다.

## 📌 스쿼시 앤 머지란?

여러 커밋을 하나의 커밋으로 합쳐서 병합하는 방식입니다.

### 장점
- 커밋 히스토리가 깔끔해집니다
- 메인 브랜치의 로그가 명확합니다
- 되돌리기(Revert)가 쉽습니다

## 🔧 스쿼시 앤 머지 방법

### 1. Pull Request 페이지 방문
```
GitHub의 PR 페이지
```

### 2. "Squash and merge" 선택
- "Merge pull request" 드롭다운 클릭
- "Squash and merge" 선택

### 3. 커밋 메시지 확인 및 수정
```
[Feat] Python 기본 개념 TIL 추가

- 변수와 자료형 설명
- 코드 예시 포함
```

### 4. "Confirm squash and merge" 클릭

## ✅ 병합 완료

```
✓ Pull request successfully merged and closed
```

## 🔄 로컬 저장소 동기화

병합 후 로컬에서:

```bash
# develop 브랜치로 이동
git checkout develop

# 최신 코드 동기화
git pull origin develop
```

## 💡 병합 후 처리

### 브랜치 삭제 (GitHub)
- **PR 페이지의 "Delete branch" 버튼 클릭** 

### 로컬 브랜치 삭제
```bash
git branch -d feature/your-feature-name
```

## 📋 스쿼시 앤 머지 vs 다른 병합 방식

| 방식 | 설명 | 사용 |
|------|------|------|
| Squash and merge | 여러 커밋을 하나로 | ✅ 우리 프로젝트 |
| Merge | 모든 커밋 유지 | PR 히스토리 필요시 |
| Rebase and merge | 커밋을 순서대로 재배치 | 고급 사용자 |

## ⚠️ 주의사항

- main 브랜치에만 병합하세요
- 항상 병합후 브랜치를 삭제하세요