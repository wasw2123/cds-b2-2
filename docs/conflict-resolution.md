# Conflict Resolution Log

## 충돌 기록 #1: 트러블슈팅 문서의 revert·stash 기록 통합

### 참여자

- 작성자: 서민혁(wasw2123) — stash 기록 작성 및 충돌 해결 내용 확인
- 상대 변경 작성자: ADOHI — main에 반영된 revert 기록 작성
- 문서 통합 및 검증: 사용자 요청에 따라 Codex가 수행

### 상황(What happened)

- 작업 브랜치: `feat/docs-stash-troubleshooting`
- 병합 대상: `main` (`ef22071baf0d7f5619c0c9eea09d716091d54c07`)
- 병합 전 작업 브랜치 커밋: `90ba16ea7a1b1e25a0fe3e20bcd6a146aa4d5349`
- 공통 조상: `77321b234ce3ede06b2cc4850eff7c24fccc4d9f`
- 충돌 파일: `docs/troubleshooting-log.md`

공통 조상에서 해당 파일은 비어 있었습니다. 작업 브랜치는 stash/pop 기록을 작성했고, main에는 amend/reset/revert/stash 항목과 ADOHI의 revert 기록이 추가되었습니다.
같은 파일의 동일한 빈 구간에 서로 다른 문서 전체를 추가하여, main을 작업 브랜치에 병합하는 과정에서 충돌이 발생했습니다.

저장된 병합 메시지는 `Merge branch 'main' into feat/docs-stash-troubleshooting`이며, 충돌 파일 목록에 `docs/troubleshooting-log.md`가 기록되어 있습니다.
이 기록을 작성할 때는 충돌 마커가 이미 제거되고 두 문서가 단순히 이어 붙여진 상태였으므로, Git의 `AUTO_MERGE` 스냅샷에서 원래 충돌 내용을 확인했습니다.

### 충돌 내용(Conflict markers)

아래는 `AUTO_MERGE:docs/troubleshooting-log.md`에 남은 실제 충돌의 발췌이며, `...`는 생략한 본문입니다.

```text
    <<<<<<< HEAD
    # Git 트러블슈팅 기록

    ## 시나리오: stash와 stash pop으로 문서 변경을 작업 브랜치로 이동
    ...
    =======
    # Troubleshooting Log

    ## 시나리오: amend
    ...
    ## 시나리오: revert
    ...
    ## 시나리오: stash

    <!-- TODO(담당자 작성): git stash / git stash pop (작업 보관 후 전환) -->
    >>>>>>> main
```

- `HEAD`: 작업 브랜치의 stash/pop 실습 기록입니다.
- `=======`: 양쪽 변경을 나누는 구분선입니다.
- `main`: 병합해 들어오는 원격 기준 문서 틀과 revert 실습 기록입니다.

같은 파일의 같은 hunk를 양쪽에서 다르게 수정한 충돌이므로 미션의 비자명 충돌 조건에 해당합니다.

### 해결 과정(How)

1. `git status`로 병합 진행 중임을 확인하고, HEAD·MERGE_HEAD·공통 조상을 비교했습니다.

```bash
git status
git rev-parse HEAD MERGE_HEAD
git merge-base HEAD MERGE_HEAD
git show AUTO_MERGE:docs/troubleshooting-log.md
git show HEAD:docs/troubleshooting-log.md
git show MERGE_HEAD:docs/troubleshooting-log.md
```

2. 어느 한쪽을 버리는 대신 양쪽의 기록을 모두 보존하는 전략을 선택했습니다. 서로 다른 실습 내용이므로 둘 다 필요했습니다.
3. main의 `# Troubleshooting Log` 제목과 amend/reset/revert/stash 순서를 유지했습니다.
4. ADOHI의 revert 기록은 그대로 보존하고, stash TODO 위치에 서민혁의 실습 내용을 넣었습니다.
5. stash 기록의 제목을 기존 문서와 맞춰 `참여자`, `상황`, `시도한 명령/절차`, `결과`, `왜 이 방법을 선택했는가(Why)`로 정리하고 재현 조건·주의점도 유지했습니다.
6. 중복된 문서 제목·stash 제목·해당 TODO를 제거하고, 문서 구조와 기존 기록 보존 여부를 확인했습니다.

검증 결과: 전체 단위 테스트 16개 통과, 기존 원격 기록 보존 및 중복 제목 제거 확인.

검증 명령:

```bash
git diff --check
python3 -m unittest discover -s tests -v
```

### 결과(Outcome)

- 트러블슈팅 문서를 main의 틀에 맞춰 하나로 통합했습니다.
- 기존 revert 기록과 새 stash/pop 기록을 모두 보존했습니다.
- amend·reset TODO는 담당자가 작성할 수 있도록 유지했습니다.
- 충돌 마커 발췌는 이 문서의 코드 블록에만 증빙으로 남겼습니다.
- 이 기록 작성 시점에는 병합 완료 커밋을 만들기 전이며, 최종 커밋·PR 링크는 병합 완료 후 추가합니다.

참고 커밋:

- [작업 브랜치의 병합 전 상태](https://github.com/wasw2123/cds-b2-2/commit/90ba16ea7a1b1e25a0fe3e20bcd6a146aa4d5349)
- [병합 대상 main](https://github.com/wasw2123/cds-b2-2/commit/ef22071baf0d7f5619c0c9eea09d716091d54c07)
- [main의 revert 기록 추가](https://github.com/wasw2123/cds-b2-2/commit/525c517)

### 주의점 및 배운 점(Learnings)

- 같은 문서를 여러 명이 수정할 때는 먼저 공통 틀을 main에 반영하고, 담당 항목만 수정하면 충돌 범위를 줄일 수 있습니다.
- 충돌 마커만 지우거나 양쪽 문서를 이어 붙이면 제목과 빈 항목이 중복될 수 있으므로 최종 문서 구조도 확인해야 합니다.
- 다른 팀원이 작성한 내용과 증빙 링크를 누락하지 않도록 원격 문서와 대조합니다.
- 기록 문서에 증빙으로 넣은 충돌 마커와 실제 미해결 충돌을 구분합니다.

## 충돌 기록 #2: 트러블슈팅 문서의 reset 섹션을 두 명이 동시에 작성

### 참여자

- 작성자: 한재혁(deliolleh) — `--soft` 사례 기록 작성, 충돌 해결 수행 및 확인
- 상대 변경 작성자: 조시내(Sinai-Cho) — main에 먼저 병합된 `--mixed` 사례 기록 작성 (PR #34)
- 충돌 마커 재현 및 기록 초안: 사용자 요청에 따라 Claude Code가 수행

### 상황(What happened)

- 작업 브랜치: `feat/troubleshooting-reset` (PR #33)
- 병합 대상: `origin/main` (`f2f04f6cd12aa70b6ca54acffebcc46fcd9d0b3e`, PR #34 병합 직후)
- 병합 전 작업 브랜치 커밋: `2599f4c7cca1e6afd49c974693aef99d42493d0c`
- 공통 조상: `a2d48ae3ff60270a1ce5b68a2ca30421cfa72d81` (PR #27 병합 커밋)
- 충돌 파일: `docs/troubleshooting-log.md`

공통 조상에서 reset 섹션은 담당자가 채우도록 남겨 둔 TODO 주석 한 줄이었습니다.

```text
    ## 시나리오: reset

    <!-- TODO(담당자 작성): git reset --soft HEAD~1 (로컬 커밋 취소 + 변경 유지) -->
```

조시내는 이 줄을 `git reset --mixed`로 잘못된 브랜치의 커밋을 취소하고 새 브랜치에서 다시 커밋한 사례로 바꿔 PR #34를 열었고, 한재혁은 같은 줄을 `git reset --soft`로 커밋 내용을 재구성한 사례로 바꿔 PR #33을 열었습니다. 두 PR 모두 열려 있던 중 #34가 먼저 main에 병합되었습니다.

GitHub의 PR #33 화면에 "This branch has conflicts that must be resolved" 경고와 함께 `docs/troubleshooting-log.md`가 충돌 파일로 표시되었습니다. 웹 편집기 대신 로컬에서 main을 가져와 해결했습니다.

```text
$ git fetch origin
$ git merge origin/main
Auto-merging docs/troubleshooting-log.md
CONFLICT (content): Merge conflict in docs/troubleshooting-log.md
Automatic merge failed; fix conflicts and then commit the result.
```

### 충돌 내용(Conflict markers)

아래는 병합 시점의 `docs/troubleshooting-log.md` 충돌 발췌이며, `...`는 생략한 본문입니다. 마커 블록은 79행에서 306행까지 228줄이고, 기록 작성 시점에는 이미 해결된 뒤였으므로 양쪽 커밋을 `git merge-tree --write-tree 2599f4c f2f04f6`로 다시 병합해 같은 충돌을 재현했습니다.

```text
    ## 시나리오: reset

    ### 참여자
    <<<<<<< HEAD

    - deliolleh(한재혁): 시나리오 선정, 결과 검토 및 기록 확인
    - 명령 실행 및 기록 초안: 사용자 요청에 따라 Claude Code가 수행

    ### 상황

    - 실습을 위해 의도적으로 재현한 상황입니다. (이슈 #31)
    ...
    - **왜 `--soft`인가**: 작성한 테스트 케이스는 그대로 살려야 했습니다. ...
    =======
    - Sinai-Cho(조시내) : 커밋 리셋

    ### 1) 문제 상황 (Problem)
    ...
    이후 팀원들과 협의하여 두 작업 브랜치를 통합하기로 결정했고, ... 기존 PR에 반영했습니다.
    >>>>>>> origin/main

    ## 시나리오: revert
```

- `HEAD`: 작업 브랜치의 `--soft` 사례 기록(150줄)입니다.
- `=======`: 양쪽 변경을 나누는 구분선입니다.
- `origin/main`: 먼저 병합된 조시내의 `--mixed` 사례 기록(78줄)입니다.
- 양쪽 기록이 모두 `### 참여자` 제목으로 시작해, Git이 그 한 줄은 공통으로 처리하고 그 아래부터 충돌로 표시했습니다.

공통 조상의 한 줄(TODO 주석)을 양쪽이 서로 다른 내용으로 교체한 것이므로, 같은 파일의 같은 hunk를 다르게 수정한 충돌이며 미션의 비자명 충돌 조건에 해당합니다.

### 해결 과정(How)

1. VS Code 머지 에디터로 충돌 파일을 열어 Incoming(`origin/main`, 조시내), Current(`feat/troubleshooting-reset`, 한재혁), Result(공통 조상의 TODO 한 줄) 세 창을 비교했습니다. Result가 TODO 한 줄이라는 점에서 양쪽이 같은 자리를 바꿨음을 확인했습니다.
2. 두 기록은 같은 명령의 다른 옵션(`--mixed`와 `--soft`)을 다른 상황에 적용한 별개의 사례이므로, 한쪽을 버리지 않고 둘 다 보존하는 keep both 전략을 택했습니다. 다른 팀원의 기록을 임의로 삭제하지 않는다는 원칙도 같습니다.
3. main에 먼저 들어간 조시내의 기록을 앞에, 한재혁의 기록을 뒤에 두고 사이에 구분선(`---`)을 넣었습니다. 머지 에디터에서 Incoming을 먼저 수용한 뒤 Current를 수용했습니다.
4. 마커가 남지 않았는지, 다른 섹션(amend, revert, stash)이 그대로인지 확인한 뒤 병합을 완료했습니다.

```bash
grep -n '^<<<<<<<\|^=======\|^>>>>>>>' docs/troubleshooting-log.md   # 출력 없음
grep -n '^## ' docs/troubleshooting-log.md                            # amend, reset, revert, stash 순서 유지
git diff --check
python3 -m unittest discover -s tests -v
```

5. 병합 커밋을 만들었습니다. 메시지는 Git 기본값을 그대로 두었습니다.

```text
bb42e24 Merge remote-tracking branch 'origin/main' into feat/troubleshooting-reset
```

검증 결과: 마커 없음, 섹션 순서 유지, `git diff --check` 통과, 전체 단위 테스트 23개 통과.

### 결과(Outcome)

- reset 섹션에 조시내의 `--mixed` 사례와 한재혁의 `--soft` 사례가 순서대로 모두 남았습니다.
- 공통 조상 175줄, 작업 브랜치 324줄, main 325줄이던 문서가 병합 후 478줄이 되었습니다. 양쪽 추가분이 모두 포함된 수치입니다.
- 병합 커밋: [`bb42e24`](https://github.com/wasw2123/cds-b2-2/commit/bb42e244c57d0d8d1609be3255f78184169f3431)
- 이 병합은 PR #33에 포함되어 main에 반영됩니다.

참고 커밋:

- [작업 브랜치의 병합 전 상태 `2599f4c`](https://github.com/wasw2123/cds-b2-2/commit/2599f4c7cca1e6afd49c974693aef99d42493d0c)
- [병합 대상 main `f2f04f6`](https://github.com/wasw2123/cds-b2-2/commit/f2f04f6cd12aa70b6ca54acffebcc46fcd9d0b3e)
- [main의 reset 기록 추가 `a182233`](https://github.com/wasw2123/cds-b2-2/commit/a182233159cbc3bb2c500d510f086b071075acc0)
- [공통 조상 `a2d48ae`](https://github.com/wasw2123/cds-b2-2/commit/a2d48ae3ff60270a1ce5b68a2ca30421cfa72d81)

### 주의점 및 배운 점(Learnings)

- 한 섹션을 TODO 한 줄로 비워 두고 담당자를 정하지 않으면, 두 명이 같은 줄을 채우는 순간 반드시 충돌합니다. 시나리오별 담당자를 먼저 정하거나, 한 사람이 쓴 뒤 다른 사람은 그 아래에 사례를 추가하는 식으로 순서를 정해야 합니다.
- 충돌을 판단할 때는 양쪽 변경만 보지 말고 공통 조상(base)을 봐야 합니다. base가 TODO 한 줄이라는 사실이 "둘 다 같은 자리를 바꿨다"는 원인을 바로 보여 줍니다. 머지 에디터의 Result 창이 그 역할을 했습니다.
- 마커가 있는 상태를 해결 전에 저장해 두면 기록이 쉬워집니다. 이번에는 해결 후였지만 `git merge-tree`로 같은 충돌을 재현할 수 있었습니다.
- keep both로 해결하면 제목이 중복될 수 있습니다. 지금 reset 섹션에는 `### 참여자`가 두 번 나오므로, 사례별 제목을 붙이는 정리가 후속 작업으로 남아 있습니다.
- 이미 push된 작업 브랜치이므로 rebase 대신 merge로 main을 가져왔습니다. 강제 push 없이 일반 push로 끝납니다.
