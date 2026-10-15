# Git 트러블슈팅 기록

## 시나리오: stash와 stash pop으로 문서 변경을 작업 브랜치로 이동

### 참여자

- 서민혁: 시나리오 선정 및 변경 내용 확인
- 명령 실행 및 기록 작성: 사용자 요청에 따라 Codex가 수행

### 상황

`main`의 변경 사항을 `feat/add`에 병합한 상태에서 기여 가이드를 확인했습니다.
`docs/CONTRIBUTING.md`의 커밋 유형 표에는 `chore`와 `test`가 있었지만, 커밋 메시지 예시에는 두 유형이 빠져 있었습니다.

`feat/add`에서 예시를 추가한 뒤, 문서 변경을 별도의 작업 브랜치에 커밋하기 위해 미커밋 변경을 보관하고 이동했습니다.

### 재현 조건 및 수정 내용

- 시작 브랜치: `feat/add`
- 기준 커밋: `4413264` (`Merge branch 'main' into feat/add`)
- 시작 시 작업 폴더: 미커밋 변경 없음
- 수정 파일: `docs/CONTRIBUTING.md` — 이미 Git이 추적 중인 파일
- 새로 추가한 예시:

```text
chore: Git 제외 목록에 Python 캐시 추가
test: 덧셈 함수의 양수·음수·0 검증 추가
```

### 실행 절차 및 실제 결과

파일을 수정하고 저장한 뒤 다음 명령을 순서대로 실행했습니다.

```bash
git stash
git checkout -b feat/docs-examples
git stash pop
```

실제 출력의 주요 내용:

```text
Saved working directory and index state WIP on feat/add: 4413264 Merge branch 'main' into feat/add
Switched to a new branch 'feat/docs-examples'
Changes not staged for commit:
    modified:   docs/CONTRIBUTING.md
Dropped refs/stash@{0} (5acd8cf8b0ffa13fec08fa90e27021b0b6a68eb0)
```

복원 후 `git diff -- docs/CONTRIBUTING.md`로 예시 두 줄이 유지된 것을 확인했습니다.
`git diff --check`는 통과했고 `git stash list`는 비어 있었습니다.

```bash
git add docs/CONTRIBUTING.md
git commit -m "docs: chore 및 test 커밋 메시지 예시 추가"
```

### 결과 및 증빙

- `feat/add`에서 작성한 미커밋 문서 변경을 `feat/docs-examples`로 옮겼습니다.
- `stash pop`이 충돌 없이 성공하여 보관 항목이 삭제되었습니다.
- 예시 변경은 `4c4928d` 커밋에 기록했습니다.
- [예시 변경 커밋](https://github.com/wasw2123/cds-b2-2/commit/4c4928d) — 브랜치를 원격에 push한 뒤 확인 가능
- 관련 Issue 및 PR: 생성 후 링크 추가

기록 문서는 예시 변경과 분리하기 위해 `feat/add`에서 `git checkout -b feat/docs-stash-troubleshooting`으로 만든 별도 브랜치에 작성했습니다.

### 이 방법을 선택한 이유

변경 사항은 아직 커밋되지 않았으므로, 기존 커밋을 취소하는 `reset`이나 `revert` 대신 `stash`로 임시 보관했습니다.
새 브랜치에서 `stash pop`으로 복원하여 파일을 다시 작성하지 않고 문서 작업을 분리할 수 있었습니다.

### 주의점 및 배운 점

- 작업 시작 전에 현재 브랜치를 확인하고 작업 목적에 맞는 브랜치를 생성합니다.
- 기본 `git stash`는 미추적 파일을 보관하지 않습니다. 이번에는 이미 추적 중인 문서를 수정했으므로 추가 옵션이 필요하지 않았습니다.
- `stash pop` 성공 시 해당 보관 항목이 삭제됩니다. 충돌이 발생하면 항목이 남을 수 있으므로 상태를 확인하고 해결해야 합니다.
- `git checkout -b`는 현재 커밋을 기준으로 브랜치를 생성합니다. 이번 두 작업 브랜치는 모두 `feat/add`의 `4413264`에서 생성했습니다.
- 공유 브랜치의 커밋 이력을 재작성하거나 강제 push하지 않았습니다.
