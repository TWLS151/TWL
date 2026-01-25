# Git 커밋 취소 및 관리 방법
26-01-25

1. 최근 커밋만 취소하기 (작업내용은 staging으로 유지)
Soft Reset: 커밋만 취소하고 수정사항은 staging 상태로 유지
command: git reset --soft HEAD~1

2. 최근 커밋과 작업 내용 모두 삭제
Hard Reset; 커밋과 작업 내요 모두 삭제(하지마...!!)
command: git reset --hard HEAD~1

---
추가 공부하면 좋을것(지금은 이해가 안감)

1. 특정 과거 커밋 삭제(git rebase)
git rebase -i HEAD~[범위]

2. 이미 push된 커밋 되돌리기 (git revert)
기존 이력을 남기면서 반대되는 커밋 추가...??
git revert [커밋ID]
