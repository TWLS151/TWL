TIL README의 작성을 자동화해보려 합니다.
"https://github.com/marketplace/actions/til-auto-format-readme"
  
---
  
```yaml
name: Build-README
run-name: ${{ github.actor }} is writing til
permissions:
  contents: write
on:
  push:
      branches:
      - master
      paths-ignore:
      - README.md
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Check out repo
      uses: actions/checkout@v4
      with:
        fetch-depth: 0    
    - name: TIL Auto-Format README
      uses: cflynn07/github-action-til-autoformat-readme@1.2.4
      with:
        decription: |
            매일이 쌓여 한 달이 되고 한 달이 쌓여 일 년이 되고 일 년이 쌓여 인생이 됩니다. 매일매일 꾸준히 노력하는 사람이 되고 싶고, 되어 나가고 있습니다. 힘이 들 땐 힘을 내자. 
        list_most_recent: 3
        date_format: "2026 Mar 14:01"
```

권한 설정으로 인한 에러가 발생해서 repo settings 에서 권한 설정도 변경하고 위 코드에 `permission` 파트를 추가했습니다.