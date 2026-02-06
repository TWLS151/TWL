## React Native CI 환경 구축하기
CI 환경을 구축하려 한다.

이걸 해두면 코드가 더러우면 아예 PR 머지가 안 되게 막을 수 있어서, 코드 퀄리티가 올라간다.

- lint: 프로젝트 전체의 JS, TS 파일 검사
- typecheck: `tsc --noEmit`은 컴파일은 안 하고 타입 오류가 있는지만 체크하는 명령어

### 할 일

- [x]  로컬 설정: `packages.json` 에 명령어 만들기
- [x]  Github Actions: 자동으로 검사
- [x]  Github 설정: 검사에 실패하면 머지 버튼 막기

### 과정

### 1. 로컬에서 잘 되는지 확인

- `packages.json`

```tsx
"scripts": {
  "android": "react-native run-android",
  "ios": "react-native run-ios",
  "start": "react-native start",
  // 아래 두 줄을 수정 및 추가
  "lint": "eslint . --ext .js,.jsx,.ts,.tsx",
  "typecheck": "tsc --noEmit"
},
```

- 테스트

```bash
yarn lint
yarn typecheck
```

### 2. Github Actions 파일 만들기

**방법1**

- 프로젝트 최상위 폴더에 `.github` 폴더 만들기
- 그 안에 `workflows` 폴더 만들기
- 그 안에 `ci.yml` 파일 만들기

```tsx
name: CI Check (Lint & Type)

on:
  pull_request:
    branches: [ "main" ]
  push:
    branches: [ "main" ]

jobs:
  check:
    name: Lint & Type Check
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: 24
          cahce: 'yarn'
      - run: yarn install --frozen-lockfile
      - run: yarn Lint
      - run: yarn typecheck
```

- 깃허브에 올리기

### 3. Github 설정에서 머지 금지 걸기

- Github 저장소 `Settings` > 왼쪽 탭 `Branches` > `Add classic branch protection rule`
- 브랜치 이름 입력 > `Require status checks to pass before merging` 체크
- 설정한 job 이름 `Lint & Type Check` 검색해서 선택
- `Create` 버튼

![image.png](attachment:8663c54e-1afc-4e1d-a390-213a4ba73087:image.png)

**방법2**

- Github 레포 `Actions` 탭
- `New worflow` 버튼
- `setup a workflow yourself`
- 에디터 수정
- `Commit changes` 버튼

### 결과

- 실패하면 이렇게 메일이 오고, 머지 불가능하다.

![image.png](attachment:10c160d4-509b-434f-a923-1e5f1b9928fd:image.png)

![image.png](attachment:f5359e33-8af6-487a-bfdc-3e77a76245a7:image.png)

### 문서

[**Setup Node.js environment**](`https://github.com/actions/setup-node`)