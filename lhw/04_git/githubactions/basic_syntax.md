# Actions

---

### 주요 개념
  
  1. Events
    - Actions 시작의 트리거가 되는 사건을 의미 ( push | pr | merge 등 )
  
  2. Workflow
    - Event 에 의해 액션이 실행되면 워크 플로우 내의 시퀀스가 진행됨

  3. Jobs
    - Workflow의 내용. 내부 시퀀스 작업을 의미. 블럭으로 구분해두면 각각 병렬적으로 실행된다.

  4. Actions
    - Jobs 안에 들어가는 라이브러리 같은 개념. 여러가지 기능들을 자동화해둔 함수 같은 것

  5. Runners
    - 병렬적으로 진행되는 Jobs를 시행하는 vessels

---
### CODE

```python
name: GitHub Actions Demo
run-name: ${{ github.actor }} is testing out GitHub Actions 🚀
on: [push]
jobs:
  Explore-GitHub-Actions:
    runs-on: ubuntu-latest
    steps:
      - run: echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event."
      - run: echo "🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!"
      - run: echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}."
      - name: Check out repository code
        uses: actions/checkout@v5
      - run: echo "💡 The ${{ github.repository }} repository has been cloned to the runner."
      - run: echo "🖥️ The workflow is now ready to test your code on the runner."
      - name: List files in the repository
        run: |
          ls ${{ github.workspace }}
      - run: echo "🍏 This job's status is ${{ job.status }}."
```

1. WorkFlow's Name
> name: GitHub Actions Demo  
워크 플로우의 이름이 되는 부분
  
2. Event
> on : [push]  
푸쉬가 발생하면 이 워크 플로우를 실행한다고 명시
  
3. jobs
> from `jobs:` to `- run: echo "🍏 This job's status is ${{ job.status }}."`
`jobs` 블럭 시작부터 블럭 마지막 줄까지, 이 워크 플로우에서 실행 될 액션과 해당 액션의 러너의 나열