# Troubleshooting Log

## 시나리오: amend

### 참여자

- Yoonsik-Shin: 실습 수행 및 기록

### 상황

- 실습을 위해 의도적으로 재현한 상황입니다.
- PR 템플릿(`.github/pull_request_template.md`)에 이슈 자동 연동을 위한 `Closes #` 항목을 추가하는 과정에서 실수 발생:
  - 파일 본문에 오타 작성: `Closes` 대신 `Clsoes` 입력
  - 커밋 메시지 컨벤션 및 오타 발생: `docs:` 대신 `doc:`, `추가` 대신 `추갖` 입력
- 원격에 push하기 전 로컬 커밋 상태에서 오타 및 컨벤션 위반을 발견했습니다.

```text
$ git log -1
commit 4d5c848ec81e95119d5976a47bbc20698f6886c7 (HEAD -> feat/troubleshooting-amend)
Author: Yoonsik-Shin <sys25800994@gmail.com>
Date:   Thu Oct 15 11:29:23 2026 +0900

    doc: PR 템플릿에 Clsoes 이슈 연동 항목 추갖
```

### 시도한 명령/절차

1. 파일 내용 오타 수정 후 Staging

```text
# 파일 내용 수정 (Clsoes -> Closes) 후 스테이징
$ git add .github/pull_request_template.md
```

2. `git commit --amend`로 직전 커밋 내용 및 메시지 덮어쓰기

```text
$ git commit --amend -m "docs: PR 템플릿에 관련 이슈(Closes) 항목 추가"
[feat/troubleshooting-amend 88b4953] docs: PR 템플릿에 관련 이슈(Closes) 항목 추가
 Date: Thu Oct 15 11:29:23 2026 +0900
 1 file changed, 4 insertions(+)
```

3. 결과 확인

```text
$ git log -1 --stat
commit 88b4953c829e1f5795cb99f46487e6fa78c80fd2 (HEAD -> feat/troubleshooting-amend)
Author: Yoonsik-Shin <sys25800994@gmail.com>
Date:   Thu Oct 15 11:29:23 2026 +0900

    docs: PR 템플릿에 관련 이슈(Closes) 항목 추가

 .github/pull_request_template.md | 4 ++++
 1 file changed, 4 insertions(+)
```

### 결과

- 수정 커밋: `88b4953` `docs: PR 템플릿에 관련 이슈(Closes) 항목 추가`
- 새로운 커밋을 추가로 만들어 불필요한 "오타 수정" 커밋 히스토리를 남기지 않고, 직전 커밋 하나로 깔끔하게 통합되었습니다.
- 커밋 해시가 `4d5c848`에서 `88b4953`으로 변경되었습니다.

### 왜 이 방법을 선택했는가(Why)

- **원격(Remote)에 push되지 않은 로컬 커밋**:
  - 아직 원격 저장소에 공유되지 않은 커밋이므로 다른 팀원에게 영향을 주지 않고 안전하게 히스토리를 재작성할 수 있습니다.
- **불필요한 수정 커밋 방지**:
  - 오타 수정이나 파일 누락 때문에 불필요한 별도 커밋(`fix typo` 등)을 계속 쌓지 않고, 원래 의도했던 단일 원자적 커밋(Atomic Commit)으로 유지할 수 있습니다.
- **주의할 점**:
  - `git commit --amend`는 기존 커밋을 수정하는 것이 아니라 **새로운 커밋 객체를 생성해 대체**하는 작업입니다.
  - 따라서 이미 원격 저장소에 push된 커밋에 `amend`를 수행하면 로컬과 원격의 히스토리가 갈라져 `git push --force`가 필요하게 되며, 이는 다른 협업자의 작업에 충돌을 유발할 수 있습니다.
  - **이미 push된 커밋은 `git revert`를 사용하거나 추가 커밋을 작성하고, `amend`는 오직 로컬 커밋에만 사용**해야 합니다.


## 시나리오: reset

<!-- TODO(담당자 작성): git reset --soft HEAD~1 (로컬 커밋 취소 + 변경 유지) -->

## 시나리오: revert

### 참여자

- ADOHI: 실습 수행 및 기록

### 상황

- 실습을 위해 의도적으로 재현한 상황입니다. (이슈 #21)
- `feat/troubleshooting-revert` 브랜치에서 몫 연산을 `a // b`에서 `int(a / b)`로 바꾼 커밋을 원격에 push했습니다.
  - 커밋: [`33001af`](https://github.com/wasw2123/cds-b2-2/commit/33001afa0e9d37cef9d27ac5d2d4c4f5029c9c71) `refactor: 몫 연산을 int(a / b) 방식으로 변경`
- 동작이 같다고 생각하고 `refactor`로 바꿨지만, `int(a / b)`는 0 방향으로 버리기 때문에 음수에서 결과가 달라집니다.
- 단위 테스트로 문제를 발견했습니다.

```text
FAIL: test_negative_numbers (test_quotient.TestQuotient)
    self.assertEqual(quotient(-7, 2), -4)
AssertionError: -3 != -4

FAILED (failures=1)
```

### 시도한 명령/절차

1. 되돌릴 커밋 확인

```text
$ git log --oneline -3
33001af refactor: 몫 연산을 int(a / b) 방식으로 변경
77321b2 Merge pull request #14 from wasw2123/feat/update-contributing
f1d2241 Merge pull request #15 from wasw2123/feat/quotient
```

2. revert 실행 (커밋 메시지를 팀 컨벤션에 맞추기 위해 `--no-commit` 후 직접 커밋)

```text
$ git revert --no-commit 33001af
$ git commit -m "fix: 몫 연산 기준 변경 되돌리기" -m "This reverts commit 33001afa0e9d37cef9d27ac5d2d4c4f5029c9c71."
[feat/troubleshooting-revert c43e8c9] fix: 몫 연산 기준 변경 되돌리기
 1 file changed, 1 insertion(+), 1 deletion(-)
```

3. 복구 확인 후 일반 push

```text
$ python -m unittest discover -s tests
Ran 8 tests in 0.000s
OK

$ git diff 33001af^ HEAD --stat
(출력 없음: 실수 커밋 직전 상태와 동일)

$ git push
   33001af..c43e8c9  feat/troubleshooting-revert -> feat/troubleshooting-revert
```

### 결과

- 되돌리기 커밋: [`c43e8c9`](https://github.com/wasw2123/cds-b2-2/commit/c43e8c9742da565ed46bc1107670845020dabd20) `fix: 몫 연산 기준 변경 되돌리기`
- 실수 커밋을 지우지 않고, 그 변경을 정반대로 적용하는 커밋을 추가해 코드를 원래대로 되돌렸습니다.
- 히스토리에는 실수 커밋과 되돌리기 커밋이 모두 남아, 무엇이 왜 되돌려졌는지 추적할 수 있습니다.

```text
* c43e8c9 fix: 몫 연산 기준 변경 되돌리기
* 33001af refactor: 몫 연산을 int(a / b) 방식으로 변경
*   77321b2 Merge pull request #14 from wasw2123/feat/update-contributing
```

- 주의할 점
  - revert는 커밋을 없애는 것이 아니라 새 커밋을 추가합니다. 되돌린 변경을 다시 적용하려면 revert 커밋을 다시 revert해야 합니다.
  - 머지 커밋을 되돌릴 때는 기준 부모를 지정하는 `-m 1` 옵션이 필요합니다.
  - git 기본 메시지(`Revert "..."`)는 팀 컨벤션과 맞지 않으므로 메시지를 직접 작성하고, 본문에 `This reverts commit <hash>.`를 남겨 추적할 수 있게 합니다.
  - 이 PR을 Squash로 병합하면 두 커밋이 하나로 합쳐져 기록이 사라지므로 Merge commit으로 병합합니다.

### 왜 이 방법을 선택했는가(Why)

- 실수 커밋이 이미 원격에 push되어 있어, 다른 팀원이 받아갔을 수 있는 히스토리를 바꾸지 않는 revert를 선택했습니다.
- `reset`으로 커밋을 지우면 로컬과 원격 히스토리가 갈라져 일반 push가 거부됩니다. 아래는 reset 후 상태(`77321b2`)를 push하는 경우를 `--dry-run`으로 확인한 결과입니다.

```text
$ git push --dry-run origin 77321b2:refs/heads/feat/troubleshooting-revert
 ! [rejected]        77321b2 -> feat/troubleshooting-revert (non-fast-forward)
error: failed to push some refs to 'https://github.com/wasw2123/cds-b2-2'
```

- 이를 push하려면 강제 push가 필요한데, 이는 팀 규칙(합의 없는 강제 push 금지)에 어긋나고 `main`에서는 ruleset으로 차단됩니다. revert는 일반 push로 끝나므로 이런 문제가 없습니다.

| | `reset` | `revert` |
| --- | --- | --- |
| 동작 | 커밋을 히스토리에서 지움 | 반대 변경을 담은 커밋을 추가 |
| 이미 push된 커밋 | 강제 push 필요, 팀원 히스토리와 어긋남 | 일반 push로 해결 |
| 적합한 상황 | 아직 push하지 않은 로컬 커밋 | 이미 공유된 커밋 |

## 시나리오: stash

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

### 시도한 명령/절차

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

### 결과

- `feat/add`에서 작성한 미커밋 문서 변경을 `feat/docs-examples`로 옮겼습니다.
- `stash pop`이 충돌 없이 성공하여 보관 항목이 삭제되었습니다.
- 예시 변경은 `4c4928d` 커밋에 기록했습니다.
- [예시 변경 커밋](https://github.com/wasw2123/cds-b2-2/commit/4c4928d) — 브랜치를 원격에 push한 뒤 확인 가능
- 관련 Issue 및 PR: 생성 후 링크 추가

기록 문서는 예시 변경과 분리하기 위해 `feat/add`에서 `git checkout -b feat/docs-stash-troubleshooting`으로 만든 별도 브랜치에 작성했습니다.

### 왜 이 방법을 선택했는가(Why)

변경 사항은 아직 커밋되지 않았으므로, 기존 커밋을 취소하는 `reset`이나 `revert` 대신 `stash`로 임시 보관했습니다.
새 브랜치에서 `stash pop`으로 복원하여 파일을 다시 작성하지 않고 문서 작업을 분리할 수 있었습니다.

### 주의점 및 배운 점

- 작업 시작 전에 현재 브랜치를 확인하고 작업 목적에 맞는 브랜치를 생성합니다.
- 기본 `git stash`는 미추적 파일을 보관하지 않습니다. 이번에는 이미 추적 중인 문서를 수정했으므로 추가 옵션이 필요하지 않았습니다.
- `stash pop` 성공 시 해당 보관 항목이 삭제됩니다. 충돌이 발생하면 항목이 남을 수 있으므로 상태를 확인하고 해결해야 합니다.
- `git checkout -b`는 현재 커밋을 기준으로 브랜치를 생성합니다. 이번 두 작업 브랜치는 모두 `feat/add`의 `4413264`에서 생성했습니다.
- 공유 브랜치의 커밋 이력을 재작성하거나 강제 push하지 않았습니다.
