# 5단계: Pull Request 요청

GitHub에서 Pull Request를 생성하여 코드 리뷰를 요청합니다.

## 📌 Pull Request란?

브랜치의 변경사항을 메인 브랜치에 병합해달라는 요청입니다.

## 🔧 Pull Request 생성 방법

### 1. GitHub 저장소 방문
```
https://github.com/your-org/TWL
```

### 2. "Pull Request" 탭 클릭

### 3. "New Pull Request" 버튼 클릭

### 4. 브랜치 선택
- Base: `main` (병합 대상)
- Compare: `learned/your-feature-name` (병합 할 브랜치)

### 5. Pull Request 제목 작성
```
[타입] 간단한 설명
```

### 예시
```
[Feat] Python 기본 개념 TIL 추가
```

## 📝 Pull Request 설명 작성

```markdown
## 📋 변경사항

- [ ] 새로운 TIL 추가
- [ ] 예제 코드 작성

## 📌 상세 설명

Python의 기본 개념에 대한 TIL을 추가했습니다.

## 🔗 관련 이슈

Closes #123

## 📸 스크린샷 (필요시)

![설명](이미지_URL)
```

## ✅ Pull Request 체크리스트

- [ ] 제목이 명확한가?
- [ ] 설명이 충분한가?
- [ ] 불필요한 파일이 포함되지 않았나?
- [ ] 기본 브랜치가 develop으로 설정되었나?

## 💬 리뷰 요청하기

PR 생성 후:
1. 오른쪽 패널의 "Reviewers" 클릭
2. 팀원 선택
3. "Request" 클릭

## 📋 PR 상태 확인

- **Open**: 리뷰 대기 중
- **Changes Requested**: 수정 필요
- **Approved**: 승인됨
- **Merged**: 병합 완료