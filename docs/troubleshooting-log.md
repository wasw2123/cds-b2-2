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

- deliolleh(한재혁): 시나리오 선정, 결과 검토 및 기록 확인
- 명령 실행 및 기록 초안: 사용자 요청에 따라 Claude Code가 수행

### 상황

- 실습을 위해 의도적으로 재현한 상황입니다. (이슈 #31)
- `feat/troubleshooting-reset` 브랜치에서 몫·나머지 정합성 테스트에 음수 피제수 케이스 `(-1, 3)`을 추가하던 중, 값을 눈으로 확인하려고 `src/remainder.py`에 `print(...)` 디버그 줄을 넣었습니다.
- 확인이 끝난 뒤 디버그 줄을 지우는 것을 잊은 채 `git commit -am "update"`로 커밋했습니다. 두 가지 실수가 한 커밋에 들어갔습니다.
  - 커밋 메시지 `update`는 팀 컨벤션에서 금지한 "의미 없는 메시지"입니다.
  - 커밋 내용에 테스트와 무관한 디버그 코드가 섞여 있습니다.

```text
$ git log --oneline -3
664e42d update
a2d48ae Merge pull request #27 from wasw2123/feat/division-consistency
d33cbd8 Merge pull request #28 from wasw2123/feat/troubleshooting-amend

$ git show --stat --oneline HEAD
664e42d update
 src/remainder.py                   | 1 +
 tests/test_division_consistency.py | 1 +
 2 files changed, 2 insertions(+)
```

- 되돌리기 전에 이 커밋이 원격에 없는지 확인했습니다. 브랜치 자체가 아직 push된 적이 없어 `ls-remote` 결과가 비어 있습니다.

```text
$ git ls-remote --heads origin feat/troubleshooting-reset
(출력 없음: 원격에 브랜치 없음)
```

### 시도한 명령/절차

1. 커밋 취소, 변경은 staged 상태로 유지

```text
$ git reset --soft HEAD~1

$ git log --oneline -2
a2d48ae Merge pull request #27 from wasw2123/feat/division-consistency
d33cbd8 Merge pull request #28 from wasw2123/feat/troubleshooting-amend

$ git status
On branch feat/troubleshooting-reset
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   src/remainder.py
	modified:   tests/test_division_consistency.py
```

2. 풀린 커밋의 내용을 staged 상태에서 다시 점검

```text
$ git diff --cached
diff --git a/src/remainder.py b/src/remainder.py
@@ -15,5 +15,6 @@ def remainder(a: int, b: int) -> int:
     dividend = a
     divisor = b
+    print(dividend, divisor)  # debug

     return dividend % divisor
diff --git a/tests/test_division_consistency.py b/tests/test_division_consistency.py
@@ -19,6 +19,7 @@ class TestDivisionConsistency(unittest.TestCase):
         (10, 5),
         (0, 3),
         (3, 5),
+        (-1, 3),
     ]
```

3. 디버그 줄만 커밋 대상에서 제외하고 작업 파일에서도 제거

```text
$ git restore --staged src/remainder.py
$ git restore src/remainder.py

$ git status
On branch feat/troubleshooting-reset
Changes to be committed:
	modified:   tests/test_division_consistency.py
```

4. 테스트 확인 후 컨벤션에 맞는 메시지로 다시 커밋

```text
$ python3 -m unittest tests/test_division_consistency.py -v
test_division_identity ... ok
test_remainder_sign_follows_divisor ... ok
test_remainder_smaller_than_divisor ... ok
Ran 3 tests in 0.000s
OK

$ git commit -m "test: 정합성 테스트에 음수 피제수 케이스 추가"
[feat/troubleshooting-reset 702553d] test: 정합성 테스트에 음수 피제수 케이스 추가
 1 file changed, 1 insertion(+)
```

5. 결과 확인 및 일반 push

```text
$ git log --oneline -3
702553d test: 정합성 테스트에 음수 피제수 케이스 추가
a2d48ae Merge pull request #27 from wasw2123/feat/division-consistency
d33cbd8 Merge pull request #28 from wasw2123/feat/troubleshooting-amend

$ git diff HEAD~1 --stat
 tests/test_division_consistency.py | 1 +
 1 file changed, 1 insertion(+)

$ git push -u origin feat/troubleshooting-reset
To https://github.com/wasw2123/cds-b2-2.git
 * [new branch]      feat/troubleshooting-reset -> feat/troubleshooting-reset
branch 'feat/troubleshooting-reset' set up to track 'origin/feat/troubleshooting-reset'.
```

강제 옵션 없이 일반 push로 올라갔습니다. reset이 원격 히스토리에 영향을 주지 않았다는 뜻입니다.

### 결과

- 잘못된 커밋 `664e42d`(`update`, 2개 파일)가 `702553d`(`test: 정합성 테스트에 음수 피제수 케이스 추가`, 1개 파일)로 바뀌었습니다.
- 커밋 수는 그대로 1개이고, 디버그 코드는 히스토리에 남지 않았습니다.
- `src/remainder.py`는 `main`과 동일한 상태로 돌아갔습니다.
- 취소된 커밋은 삭제된 것이 아니라 reflog에 남아 있어, 실수로 reset했더라도 `git reset --soft 664e42d`로 복구할 수 있습니다.

```text
$ git reflog -3
702553d HEAD@{0}: commit: test: 정합성 테스트에 음수 피제수 케이스 추가
a2d48ae HEAD@{1}: reset: moving to HEAD~1
664e42d HEAD@{2}: commit: update
```

- 주의할 점
  - `reset`은 push하지 않은 로컬 커밋에만 사용합니다. push된 커밋을 reset하면 원격과 히스토리가 갈라져 강제 push가 필요해지고, 이는 팀 규칙에 어긋납니다.
  - 되돌려도 되는 범위는 push 여부로 정합니다. 브랜치가 원격에 있으면 `git status -sb`의 `[ahead N]`이 로컬에만 있는 커밋 수이고, `HEAD~1`은 이 수를 넘지 않아야 합니다. 이번처럼 브랜치가 원격에 없으면 `git ls-remote --heads origin <브랜치>`가 비어 있는 것으로 확인합니다.
  - `--soft`는 index와 작업 파일을 모두 유지합니다. 옵션을 잘못 쓰면 변경이 사라질 수 있으므로 아래 표의 차이를 알고 써야 합니다. 특히 `--hard`는 작업 파일까지 버립니다.
  - `git commit -a`는 추적 중인 모든 수정을 한 번에 담기 때문에 이번처럼 무관한 변경이 섞이기 쉽습니다. 커밋 전 `git diff --cached`로 내용을 확인하는 습관이 재발 방지책입니다.

| 옵션 | 커밋 | staged(index) | 작업 파일 |
| --- | --- | --- | --- |
| `--soft` | 취소 | 유지 | 유지 |
| `--mixed`(기본) | 취소 | 풀림(unstaged) | 유지 |
| `--hard` | 취소 | 버림 | 버림 |

### 왜 이 방법을 선택했는가(Why)

- **왜 `revert`가 아닌가**: 실수 커밋이 아직 원격에 없으므로 공유된 히스토리가 없습니다. 되돌리기 커밋을 추가하면 `update`와 그 되돌리기가 둘 다 남아 히스토리만 지저분해집니다. revert는 push된 커밋에 쓰는 방법입니다.
- **왜 `--amend`가 아닌가**: amend는 직전 커밋에 변경을 덧붙이거나 메시지를 바꿀 때 적합합니다. 이번에는 커밋에서 파일 하나를 빼야 했으므로, 커밋을 완전히 풀어 staged 상태에서 `git diff --cached`로 내용을 확인하고 다시 구성하는 `reset --soft`가 맞습니다. 메시지나 작은 누락은 amend, 커밋 내용을 다시 구성하거나 여러 커밋을 합칠 때(`HEAD~2` 이상)는 `reset --soft`로 구분합니다.
- **왜 `--soft`인가**: 작성한 테스트 케이스는 그대로 살려야 했습니다. `--soft`는 변경을 staged 상태로 유지하므로 필요한 파일만 남기고 바로 다시 커밋할 수 있었습니다.

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
