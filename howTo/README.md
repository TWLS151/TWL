# Git 협업 워크플로우 가이드

이 폴더에서는 TWL 프로젝트에 기여하기 위한 Git 워크플로우를 단계별로 설명합니다.

## 📋 전체 사이클

```
1. Git Pull (최신 코드 동기화)
   ↓
2. 브랜치 생성 (learned 브랜치)
   ↓
3. 코드 수정 및 작업
   ↓
4. 커밋 (변경사항 기록)
   ↓
5. 리모트에 브랜치 올리기 (Push)
   ↓
6. Pull Request 요청
   ↓
7. Pull Request 검토 및 스쿼시 앤 머지
   ↓
8. 로컬 정리 (브랜치 삭제 및 다시 동기화)
```

## 🔄 각 단계별 상세 가이드

- [01-git-pull.md](./01-git-pull.md): Git Pull로 최신 코드 동기화
- [02-branch-create.md](./02-branch-create.md): 브랜치 생성
- [03-code-modify-commit.md](./03-code-modify-commit.md): 코드 수정 및 커밋
- [04-push-remote.md](./04-push-remote.md): 리모트에 브랜치 올리기
- [05-pull-request.md](./05-pull-request.md): Pull Request 요청
- [06-merge-squash.md](./06-merge-squash.md): Pull Request 스쿼시 앤 머지
- [07-cleanup-cycle.md](./07-cleanup-cycle.md): 로컬 정리 및 사이클 반복

## 📌 주요 규칙

- `main` 브랜치에는 직접 커밋하지 않습니다
- 모든 작업은 `feature/*` 브랜치에서 진행합니다
- Pull Request를 통해 코드 리뷰를 거칩니다
- 최종 병합은 스쿼시 앤 머지로 진행합니다