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

### 참여자
- Sinai-Cho(조시내) : 커밋 리셋

### 1) 문제 상황 (Problem)

빼기 연산 함수에 대한 코드 리뷰 의견을 반영하기 위해 기존 작업 브랜치인 `feat/subtract`에서 아래의 내용을 수정했습니다.

- 함수에 Docstring 추가
- 매개변수와 반환값에 `int` 타입 힌트 추가
- 함수 아래 개행 수정

그러나 해당 변경 사항을 새로운 브랜치에서 별도로 관리하기로 결정했음에도, 기존 `feat/subtract` 브랜치에서 먼저 커밋하는 문제가 발생하여 기존 커밋을 취소하고, 수정한 코드 내용은 유지한 상태로 새로운 브랜치에서 다시 커밋해야하는 상황이 되었습니다.

### 2. 문제 원인 (Cause)

코드를 수정하기 전에 새로운 작업 브랜치를 생성하지 않았기 때문입니다.

### 3. 해결 과정 (Solution)

#### 1) 기존 커밋 확인

먼저 현재 브랜치와 최근 커밋 기록을 확인했습니다.
```bash
git branch --show-current
git log -3 --oneline
git status
```
(가장 최근 커밋이 Docstring과 타입 힌트 수정 작업에 해당하는지 확인)

#### 2) Git Reset 실행

가장 최근 커밋을 취소하되 수정한 파일 내용은 유지하기 위해 다음 명령어를 사용했습니다.

```bash
git reset --mixed HEAD~1
```
< 참고 : 각 명령어 뜻 >
- `reset`: 브랜치의 HEAD를 이전 커밋으로 이동
- `--mixed`: 스테이징 상태를 초기화하고 수정 파일 내용은 유지
- `HEAD~1`: 현재 커밋의 바로 이전 커밋

이를 통해 최근 커밋을 취소하면서 `src/subtract.py`의 수정 사항은 작업 폴더에 유지할 수 있었습니다.

#### 3) 새로운 브랜치 생성

수정 내용을 별도로 관리하기 위해 새로운 브랜치를 생성했습니다.

```bash
git switch -c feat/subtract-refactor
```

#### 4) 수정 내용 다시 커밋

새로운 브랜치에서 수정된 파일을 스테이징하고 다시 커밋을 진행했습니다.

```bash
git add src/subtract.py

git commit -m "refactor: 빼기 연산 함수에 docstring, 타입 힌트 및 개행 추가"
```

#### 5) GitHub에 Push

새로운 브랜치를 원격 저장소에 Push 했습니다.

```bash 
git push -u origin feat/subtract-refactor
```

### 4. 결과 (Result)

- 기존 브랜치에서 잘못 작성한 커밋 취소.
- 수정한 Python 코드 내용은 삭제하지 않고 유지.
- `feat/subtract-refactor` 브랜치에서 수정 사항을 다시 커밋.
- 새로운 브랜치에 변경 내용을 Push하여 작업을 분리.

이후 팀원들과 협의하여 두 작업 브랜치를 통합하기로 결정했고, `feat/subtract-refactor`의 변경 사항을 `feat/subtract`에 Fast-forward Merge하여 최종적으로 기존 PR에 반영했습니다.

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

<!-- TODO(담당자 작성): git stash / git stash pop (작업 보관 후 전환) -->
