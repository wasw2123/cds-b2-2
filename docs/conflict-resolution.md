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
