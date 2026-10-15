# 동료평가 문항별 정리

- 기준 시점: 2026-10-15 11:51 (KST), `main` = [`ef22071`](https://github.com/wasw2123/cds-b2-2/commit/ef22071)
- 저장소: <https://github.com/wasw2123/cds-b2-2>
- 이 문서는 동료평가 준비용으로 `feat/peer-evaluation` 브랜치에만 두며 `main`에 병합하지 않습니다.
- 상태 표기: ✅ 충족 / ⏳ 진행 중(PR 열림) / ❌ 미충족

## 팀원

| GitHub | 권한 | 담당 연산 |
| --- | --- | --- |
| [wasw2123](https://github.com/wasw2123) | admin (저장소 소유자) | 더하기 [#2](https://github.com/wasw2123/cds-b2-2/issues/2) |
| [Yoonsik-Shin](https://github.com/Yoonsik-Shin) | write | 곱하기 [#5](https://github.com/wasw2123/cds-b2-2/issues/5) |
| [Sinai-Cho](https://github.com/Sinai-Cho) | write | 빼기 [#4](https://github.com/wasw2123/cds-b2-2/issues/4) |
| [deliolleh](https://github.com/deliolleh) | write | 나머지 [#6](https://github.com/wasw2123/cds-b2-2/issues/6) |
| [ADOHI](https://github.com/ADOHI) | write | 몫 [#7](https://github.com/wasw2123/cds-b2-2/issues/7) |

---

## 항목 1. 증빙 체크

### 1-1. 저장소 1개 + 협업 권한 ✅

- 옵션 B(개인 저장소 + Collaborator 초대)로 구성했습니다. 소유자 wasw2123 외 4명이 모두 `write` 권한으로 참여합니다.

### 1-2. main Branch Protection + PR로만 병합 ✅

- `main` ruleset: <https://github.com/wasw2123/cds-b2-2/rules/24971554>
  - `pull_request`: PR을 통해서만 병합, 승인 1명 필요
  - `non_fast_forward`: 강제 push 차단
  - `deletion`: 브랜치 삭제 차단
- 문서화: [CONTRIBUTING > 브랜치 보호 규칙](https://github.com/wasw2123/cds-b2-2/blob/main/docs/CONTRIBUTING.md#브랜치-보호-규칙-branch-protection-rule) ([#11](https://github.com/wasw2123/cds-b2-2/pull/11))
- `main`의 first-parent 히스토리는 모두 `Merge pull request #n` 커밋입니다. 유일한 예외인 `first commit`(10-13 13:12)은 ruleset 생성(10-13 13:22) 이전의 초기 커밋입니다.

```text
ef22071 Merge pull request #11 from wasw2123/feat/branch-protection-rule
cdc71a4 Merge pull request #22 from wasw2123/feat/troubleshooting-revert
9f87f86 Merge pull request #16 from wasw2123/feat/add
ef08031 Merge pull request #18 from wasw2123/feat/remainder
77321b2 Merge pull request #14 from wasw2123/feat/update-contributing
f1d2241 Merge pull request #15 from wasw2123/feat/quotient
86307dd Merge pull request #9 from wasw2123/feat/multiplier
c0b3645 Merge pull request #1 from wasw2123/docs/convention
89382e5 first commit
```

### 1-3. PR-이슈 연동(`Closes #n`) ✅ (일부 확인 필요)

| PR | 작성자 | 상태 | 연결 이슈 |
| --- | --- | --- | --- |
| [#1](https://github.com/wasw2123/cds-b2-2/pull/1) | wasw2123 | 병합 | 없음 (이슈 운영 규칙 이전) |
| [#9](https://github.com/wasw2123/cds-b2-2/pull/9) | Yoonsik-Shin | 병합 | [#5](https://github.com/wasw2123/cds-b2-2/issues/5) |
| [#11](https://github.com/wasw2123/cds-b2-2/pull/11) | Yoonsik-Shin | 병합 | [#10](https://github.com/wasw2123/cds-b2-2/issues/10) |
| [#14](https://github.com/wasw2123/cds-b2-2/pull/14) | ADOHI | 병합 | [#13](https://github.com/wasw2123/cds-b2-2/issues/13) |
| [#15](https://github.com/wasw2123/cds-b2-2/pull/15) | ADOHI | 병합 | [#7](https://github.com/wasw2123/cds-b2-2/issues/7) |
| [#16](https://github.com/wasw2123/cds-b2-2/pull/16) | wasw2123 | 병합 | [#2](https://github.com/wasw2123/cds-b2-2/issues/2) |
| [#18](https://github.com/wasw2123/cds-b2-2/pull/18) | deliolleh | 병합 | [#6](https://github.com/wasw2123/cds-b2-2/issues/6) |
| [#22](https://github.com/wasw2123/cds-b2-2/pull/22) | ADOHI | 병합 | [#21](https://github.com/wasw2123/cds-b2-2/issues/21) |
| [#12](https://github.com/wasw2123/cds-b2-2/pull/12) | Sinai-Cho | 열림(승인됨) | [#4](https://github.com/wasw2123/cds-b2-2/issues/4) |
| [#20](https://github.com/wasw2123/cds-b2-2/pull/20) | wasw2123 | 열림 | [#19](https://github.com/wasw2123/cds-b2-2/issues/19) |
| [#24](https://github.com/wasw2123/cds-b2-2/pull/24) | wasw2123 | 열림 | [#23](https://github.com/wasw2123/cds-b2-2/issues/23) |
| [#28](https://github.com/wasw2123/cds-b2-2/pull/28) | Yoonsik-Shin | 열림 | [#25](https://github.com/wasw2123/cds-b2-2/issues/25) |
| [#27](https://github.com/wasw2123/cds-b2-2/pull/27) | deliolleh | 열림 | ⚠️ 미연결 (이슈 [#26](https://github.com/wasw2123/cds-b2-2/issues/26)은 존재) |

- 확인 필요: #27 본문에 `Closes #26` 추가, #24는 실제 변경(커밋 메시지 예시)과 `Closes #23`(stash 기록) 불일치([리뷰](https://github.com/wasw2123/cds-b2-2/pull/24#pullrequestreview-5527207503)).

### 1-4. 팀원별 PR 2개 이상 병합 + `SUBMISSION.md`

| 팀원 | 병합된 PR | 열린 PR | 상태 |
| --- | --- | --- | --- |
| wasw2123 | [#1](https://github.com/wasw2123/cds-b2-2/pull/1), [#16](https://github.com/wasw2123/cds-b2-2/pull/16) | #20, #24 | ✅ |
| Yoonsik-Shin | [#9](https://github.com/wasw2123/cds-b2-2/pull/9), [#11](https://github.com/wasw2123/cds-b2-2/pull/11) | #28 | ✅ |
| ADOHI | [#14](https://github.com/wasw2123/cds-b2-2/pull/14), [#15](https://github.com/wasw2123/cds-b2-2/pull/15), [#22](https://github.com/wasw2123/cds-b2-2/pull/22) | - | ✅ |
| deliolleh | [#18](https://github.com/wasw2123/cds-b2-2/pull/18) | #27 | ⏳ (1개 더 필요) |
| Sinai-Cho | - | #12 (승인됨) | ⏳ (2개 필요) |

- `SUBMISSION.md`: ❌ `main`에 아직 없음. 기본 틀이 [#20](https://github.com/wasw2123/cds-b2-2/pull/20)(`feat/add-readme`)에 있으며, 팀원별 링크 채우기 필요.

### 1-5. 팀원별 리뷰 2개 이상 + 본인 PR에서 리뷰 반영

| 팀원 | 다른 팀원 PR 리뷰 | 본인 PR 리뷰 반영 증빙 | 상태 |
| --- | --- | --- | --- |
| wasw2123 | #9 [docstring 지적](https://github.com/wasw2123/cds-b2-2/pull/9#discussion_r4256029061), #11 [이슈 누락 지적](https://github.com/wasw2123/cds-b2-2/pull/11#issuecomment-6162274971), #12 [테스트 형식 제안](https://github.com/wasw2123/cds-b2-2/pull/12#discussion_r4270113077), #15, #18, #22 | #16 코멘트 6개 전부 답글 + 수정 커밋 ([예](https://github.com/wasw2123/cds-b2-2/pull/16#discussion_r4268660413)) | ✅ |
| Yoonsik-Shin | #12 [Request changes](https://github.com/wasw2123/cds-b2-2/pull/12) + [docstring 인라인](https://github.com/wasw2123/cds-b2-2/pull/12#discussion_r4259085275), #14, #1 | #9 [docstring 반영 답글](https://github.com/wasw2123/cds-b2-2/pull/9#discussion_r4256644461), #11 [제안 반영 커밋 `fbd96c3`](https://github.com/wasw2123/cds-b2-2/pull/11#discussion_r4268950868) | ✅ |
| ADOHI | #11 [리뷰](https://github.com/wasw2123/cds-b2-2/pull/11#pullrequestreview-5514092005), #12 [리뷰](https://github.com/wasw2123/cds-b2-2/pull/12#pullrequestreview-5514092418), #16 [리뷰](https://github.com/wasw2123/cds-b2-2/pull/16#pullrequestreview-5514279998)·[승인](https://github.com/wasw2123/cds-b2-2/pull/16#pullrequestreview-5515783424), #24 [리뷰](https://github.com/wasw2123/cds-b2-2/pull/24#pullrequestreview-5527207503) | #15 deliolleh 코멘트에 [답글](https://github.com/wasw2123/cds-b2-2/pull/15#issuecomment-6182338705) | ✅ |
| deliolleh | #20 [인라인 질문](https://github.com/wasw2123/cds-b2-2/pull/20#discussion_r4272356865), #15 [정합성 코멘트](https://github.com/wasw2123/cds-b2-2/pull/15#issuecomment-6169167427) | #18 [답글](https://github.com/wasw2123/cds-b2-2/pull/18#discussion_r4271196940) + [제목 수정](https://github.com/wasw2123/cds-b2-2/pull/18#issuecomment-6169127285) | ✅ (#15는 일반 코멘트라 정식 리뷰 1건 더 권장) |
| Sinai-Cho | #18 [부호 규칙 리뷰](https://github.com/wasw2123/cds-b2-2/pull/18#discussion_r4270819751) + [제목 형식 코멘트](https://github.com/wasw2123/cds-b2-2/pull/18#issuecomment-6168700641) | #12 [unittest 전환 답글](https://github.com/wasw2123/cds-b2-2/pull/12#discussion_r4278492856) + 수정 커밋 | ⏳ (다른 PR 리뷰 1건 더 필요) |

- 참고: #1의 리뷰는 `LGTM`뿐이었으나, 이후 [코드 리뷰 규칙](https://github.com/wasw2123/cds-b2-2/blob/main/docs/CONTRIBUTING.md#코드-리뷰-규칙)을 정해 실질 코멘트를 남기도록 개선했습니다.

### 1-6. 충돌 해결 기록 2회 이상(1회 비자명 충돌) ❌

- `docs/conflict-resolution.md`가 아직 비어 있습니다.
- 예정된 비자명 충돌: `feat/docs-stash-troubleshooting`(stash 기록)과 병합된 #22(revert 기록)가 `docs/troubleshooting-log.md`의 같은 영역을 다르게 수정해 충돌합니다(`git merge-tree`로 확인, [#24 리뷰](https://github.com/wasw2123/cds-b2-2/pull/24#pullrequestreview-5527207503)에서 공유). 이 해결 과정을 기록하면 "같은 파일 같은 hunk" 기준을 충족합니다.
- 1건 더 필요합니다.

### 1-7. 트러블슈팅 4종 수행 + 팀원별 1개 이상 참여

| 시나리오 | 담당 | 상태 | 링크 |
| --- | --- | --- | --- |
| amend | Yoonsik-Shin | ⏳ | [#28](https://github.com/wasw2123/cds-b2-2/pull/28) / [#25](https://github.com/wasw2123/cds-b2-2/issues/25) |
| reset | 미정 | ❌ | - |
| revert | ADOHI | ✅ | [#22](https://github.com/wasw2123/cds-b2-2/pull/22), [기록](https://github.com/wasw2123/cds-b2-2/blob/main/docs/troubleshooting-log.md#시나리오-revert) |
| stash | wasw2123 | ⏳ | `feat/docs-stash-troubleshooting` 브랜치 (PR 없음) / [#23](https://github.com/wasw2123/cds-b2-2/issues/23) |

- 팀원별 참여: ADOHI ✅, Yoonsik-Shin ⏳, wasw2123 ⏳, Sinai-Cho ❌, deliolleh ❌ → reset 시나리오를 Sinai-Cho 또는 deliolleh가 맡고, 나머지 한 명은 다른 시나리오 기록에 참여자로 들어가야 합니다.

### 1-8. 문서 3종 템플릿 수준 구조

| 문서 | 상태 | 구성 |
| --- | --- | --- |
| [CONTRIBUTING.md](https://github.com/wasw2123/cds-b2-2/blob/main/docs/CONTRIBUTING.md) | ✅ | 브랜치 운영·보호 규칙, 커밋 메시지, PR 작성 규칙, 코드 리뷰 규칙, 충돌 대응 흐름 |
| [troubleshooting-log.md](https://github.com/wasw2123/cds-b2-2/blob/main/docs/troubleshooting-log.md) | ✅ 구조 / ⏳ 내용 | 시나리오 4종 섹션, 각 섹션 참여자/상황/시도한 명령/결과/Why (revert 작성 완료) |
| [conflict-resolution.md](https://github.com/wasw2123/cds-b2-2/blob/main/docs/conflict-resolution.md) | ❌ | 빈 파일 |

---

## 항목 2. 우리 팀이 정한 규칙 설명

### 2-1. 브랜치를 "작업 단위"로 나눈 기준

- **이슈 1개 = 브랜치 1개 = PR 1개**를 기준으로 했습니다. 작업은 먼저 이슈로 만들고, 그 이슈만 처리하는 브랜치를 땁니다.
  - 기능 단위: 연산 함수를 팀원별 이슈로 나눔 → 몫 [#7](https://github.com/wasw2123/cds-b2-2/issues/7) → `feat/quotient` → [#15](https://github.com/wasw2123/cds-b2-2/pull/15)
  - 문서 단위: CONTRIBUTING 보강 [#13](https://github.com/wasw2123/cds-b2-2/issues/13) → `feat/update-contributing` → [#14](https://github.com/wasw2123/cds-b2-2/pull/14)
  - 실습 단위: revert 실습 [#21](https://github.com/wasw2123/cds-b2-2/issues/21) → `feat/troubleshooting-revert` → [#22](https://github.com/wasw2123/cds-b2-2/pull/22)
- 이름은 `feat/작업명` 형식입니다([CONTRIBUTING > 브랜치 운영](https://github.com/wasw2123/cds-b2-2/blob/main/docs/CONTRIBUTING.md#브랜치-운영)). #8은 이 규칙(`feature/` → `feat/`)에 맞추려고 닫고 #9로 다시 열었습니다.
- 기준이 필요한 이유를 실제로 겪었습니다. 같은 이슈(#4)의 변경을 두 브랜치·두 PR(#12, #17)로 나눴다가 변경과 리뷰가 흩어져 하나로 다시 합쳤고([#17 코멘트](https://github.com/wasw2123/cds-b2-2/pull/17#issuecomment-6166127049)), #24는 브랜치와 PR 내용이 어긋나 리뷰에서 지적됐습니다.

### 2-2. PR 본문 What/Why/How + 이슈 연동을 일관되게 남긴 방법

- **도구**: [`.github/pull_request_template.md`](https://github.com/wasw2123/cds-b2-2/blob/main/.github/pull_request_template.md)(#9에서 도입)로 PR을 열면 What/Why/How 칸이 자동으로 채워집니다. #28에서 `Closes` 항목을 템플릿에 추가하는 중입니다.
- **규칙**: [CONTRIBUTING > PR 작성 규칙](https://github.com/wasw2123/cds-b2-2/blob/main/docs/CONTRIBUTING.md#pr-작성-규칙) — 제목은 커밋 메시지 형식, 본문은 템플릿 3항목, `Closes #이슈번호` 필수, 승인 1명 후 병합.
- **운영**: 누락은 리뷰에서 바로 지적하고 고쳤습니다. #11·#12의 `Closes` 누락, #12·#18의 제목 형식이 리뷰 후 수정됐습니다.

### 2-3. 리뷰가 LGTM에 그치지 않도록 한 기준과 운영

- **기준**([CONTRIBUTING > 코드 리뷰 규칙](https://github.com/wasw2123/cds-b2-2/blob/main/docs/CONTRIBUTING.md#코드-리뷰-규칙)): LGTM만 남기는 리뷰 금지, PR마다 특정 라인/파일을 근거로 질문·대안·리스크·개선 중 하나 이상, 작성자는 답글 또는 수정 커밋으로 응답.
- **운영 예시**
  - [#16](https://github.com/wasw2123/cds-b2-2/pull/16): 리뷰어가 브랜치를 직접 실행해 "테스트가 실패해도 exit 0으로 끝난다"는 문제를 찾아 인라인 6건을 남겼고, 작성자가 6건 모두 답글과 커밋으로 반영한 뒤 승인했습니다.
  - [#11](https://github.com/wasw2123/cds-b2-2/pull/11): GitHub `suggestion` 블록으로 수정안을 제시 → 작성자가 커밋 [`fbd96c3`](https://github.com/wasw2123/cds-b2-2/commit/fbd96c3760c01bec8e3dabc23c5fe49229ac66b9)으로 반영.
  - 바로 승인하지 않고 Comment로 지적 → 수정 확인 후 Approve하는 순서로, 작성자와 리뷰어의 상호작용이 기록에 남도록 했습니다.

### 2-4. 충돌 발생 시 대응 흐름(공유 → 해결 → 기록)

- **흐름**([CONTRIBUTING > 충돌 대응 흐름](https://github.com/wasw2123/cds-b2-2/blob/main/docs/CONTRIBUTING.md#충돌-대응-흐름)): 충돌이 난 PR의 작성자가 주도 → 충돌 상대에게 공유하고 해결 방향 합의 → `docs/conflict-resolution.md`에 기록.
- **예방과 사전 공유**
  - 여러 명이 같은 문서를 고칠 때는 섹션 뼈대를 먼저 만들고 담당 섹션만 채우게 했습니다(CONTRIBUTING [#14](https://github.com/wasw2123/cds-b2-2/pull/14), troubleshooting-log [#22](https://github.com/wasw2123/cds-b2-2/pull/22)).
  - PR을 올리기 전에 `git merge-tree`로 열린 PR들과의 충돌 여부를 확인했습니다(#14는 #11과 다른 위치에 추가해 충돌 없음).
  - 예상되는 충돌은 리뷰로 미리 공유했습니다([#24 리뷰 3번](https://github.com/wasw2123/cds-b2-2/pull/24#pullrequestreview-5527207503)).
- 실제 충돌 해결 기록은 1-6과 같이 작성 예정입니다.

### 2-5. 트러블슈팅 로그를 "재현 가능"하게 만든 고정 항목

- 시나리오마다 **참여자 / 상황 / 시도한 명령·절차 / 결과(주의할 점) / 왜 이 방법을 선택했는가** 5개 항목을 고정했습니다([troubleshooting-log.md](https://github.com/wasw2123/cds-b2-2/blob/main/docs/troubleshooting-log.md)).
- revert 기록은 다른 사람이 그대로 따라 할 수 있도록:
  - 실제 명령과 **실제 출력**(테스트 실패 메시지, `git log`, push 결과)을 그대로 붙였습니다.
  - 실수 커밋 [`33001af`](https://github.com/wasw2123/cds-b2-2/commit/33001afa0e9d37cef9d27ac5d2d4c4f5029c9c71)과 되돌리기 커밋 [`c43e8c9`](https://github.com/wasw2123/cds-b2-2/commit/c43e8c9742da565ed46bc1107670845020dabd20)을 링크했습니다.
  - "실습을 위해 의도적으로 재현"했다는 전제를 명시했습니다.
  - Squash 병합 시 기록이 사라지므로 Merge commit으로 병합해 두 커밋을 `main` 히스토리에 남겼습니다.

---

## 항목 3. 이유 설명

### 3-1. GitHub Flow에서 main을 "항상 배포 가능 상태"로 유지하는 이유

- 모든 작업 브랜치가 `main`에서 출발합니다. `main`이 깨지면 그 뒤에 브랜치를 딴 모든 팀원이 깨진 코드 위에서 작업하게 되고, 문제가 내 변경 때문인지 원래 있던 것인지 구분할 수 없습니다.
- 그래서 검증은 브랜치에서 끝내고 `main`에는 통과한 것만 들어오게 합니다. revert 실습에서도 잘못된 변경(`int(a / b)`)이 브랜치의 단위 테스트에서 먼저 잡혀 `main`에는 영향이 없었습니다.

### 3-2. main 직접 push 대신 PR + 승인으로 병합하는 이유

- **품질**: 작성자 혼자서는 놓치는 문제를 리뷰어가 잡습니다. #16에서 "테스트가 실패해도 성공으로 끝나는" 문제가 리뷰로 발견됐습니다.
- **책임**: 누가 작성하고 누가 승인했는지가 PR에 남아, 변경의 근거와 확인자가 분명해집니다.
- **추적성**: `main`의 모든 변경이 `Merge pull request #n` 커밋으로 남아, 커밋 → PR(논의·리뷰) → 이슈(배경)로 거슬러 올라갈 수 있습니다.
- 이를 사람의 약속이 아니라 ruleset으로 강제했습니다(1-2).

### 3-3. 이슈-PR을 연동하는 이유

- **추적성**: 이슈(왜 필요한가) ↔ PR(어떻게 바꿨나) ↔ 커밋(무엇을 바꿨나)이 서로 링크됩니다.
- **커뮤니케이션**: 이슈의 담당자(assignee)로 작업을 나눠 중복 작업을 막았습니다(연산 #2·#4·#5·#6·#7).
- **자동화**: `Closes #n`이 있으면 PR 병합과 동시에 이슈가 자동으로 닫힙니다(#15 병합 → #7 닫힘, #22 병합 → #21 닫힘). 반대로 잘못 연결하면 일이 끝나기 전에 이슈가 닫히므로(#24) 연결 대상도 리뷰 대상입니다.

### 3-4. 원격에 push된 커밋을 되돌릴 때 reset 대신 revert를 쓰는 이유

- `reset`은 커밋을 히스토리에서 지웁니다. 이미 원격에 있는 커밋을 지우면 로컬과 원격이 갈라져 일반 push가 거부되고, 강제 push가 필요합니다. 강제 push는 그 커밋을 이미 받아간 팀원의 히스토리를 깨뜨리고, `main`에서는 ruleset으로 차단됩니다.
- `revert`는 지우지 않고 "반대로 되돌리는 커밋"을 새로 추가하므로 일반 push로 끝나고, 무엇을 왜 되돌렸는지 기록도 남습니다.
- 실제 확인 결과: reset한 상태를 push하면 `! [rejected] (non-fast-forward)`로 거부됐습니다([revert 기록 > Why](https://github.com/wasw2123/cds-b2-2/blob/main/docs/troubleshooting-log.md#시나리오-revert)).

| | `reset` | `revert` |
| --- | --- | --- |
| 동작 | 커밋을 히스토리에서 지움 | 반대 변경을 담은 커밋 추가 |
| 이미 push된 커밋 | 강제 push 필요, 팀원 히스토리와 어긋남 | 일반 push로 해결 |
| 적합한 상황 | 아직 push하지 않은 로컬 커밋 | 이미 공유된 커밋 |

### 3-5. 충돌 마커의 의미와 비자명 충돌 해결 기준

```text
<<<<<<< HEAD
(현재 내 브랜치의 내용)
=======
(병합하려는 상대 브랜치의 내용)
>>>>>>> feat/...
```

- `<<<<<<< HEAD`부터 `=======`까지는 현재 체크아웃한 브랜치의 내용, `=======`부터 `>>>>>>>`까지는 병합해 들어오는 브랜치의 내용입니다. 해결이란 이 구간을 최종 내용으로 직접 고치고 마커 3줄을 모두 지운 뒤 커밋하는 것입니다.
- 비자명 충돌의 의사결정 기준
  - **양쪽 의도를 먼저 확인**: 어느 쪽이 맞는지보다 두 변경이 각각 무엇을 하려 했는지를 상대와 공유합니다.
  - **전략 선택**: 둘 다 필요하면 keep both, 한쪽이 다른 쪽을 대체하면 choose one, 둘을 합쳐 새 구조가 필요하면 refactor.
  - **이름 변경/삭제 vs 내용 수정**: 이동·이름 변경을 기준으로 삼고, 상대의 내용 수정을 새 위치의 파일에 옮겨 적용합니다(수정이 사라지지 않게).
  - **검증**: 해결 후 테스트(`python -m unittest discover -s tests`)와 문서 렌더링을 확인하고, 과정을 `conflict-resolution.md`에 기록합니다.
- 우리 팀의 실제 비자명 충돌 사례는 troubleshooting-log의 같은 영역 충돌(1-6)로 기록할 예정입니다.

---

## 항목 4. 상황 대응

### 4-1. main에 긴급 핫픽스가 필요할 때

1. **이슈 생성**: 증상과 재현 방법을 적고 담당자를 지정합니다.
2. **브랜치**: 최신 `main`에서 바로 핫픽스 브랜치를 땁니다(예: `feat/hotfix-quotient-zero`). 다른 작업 브랜치에 섞지 않습니다.
3. **최소 수정 + 테스트**: 원인만 고치고, 재발을 잡는 테스트를 함께 추가합니다.
4. **PR**: 제목 `fix: ...`, 본문 What/Why/How + `Closes #n`. 긴급하다고 알리고 리뷰어를 직접 지정합니다.
5. **리뷰/승인**: 승인 1명 규칙은 핫픽스에도 그대로 적용합니다(ruleset에 우회자 없음). 범위가 작으니 빠르게 볼 수 있습니다.
6. **병합(배포)**: `main`이 곧 배포 기준이므로 병합이 반영입니다. 다른 팀원들은 각자 브랜치에 `main`을 다시 받아옵니다.
7. **더 급하면**: 원인 커밋을 고치기보다 먼저 되돌리는 것이 빠르면, 원인 PR의 머지 커밋을 `git revert -m 1 <merge커밋>`으로 되돌리는 PR을 올립니다.

### 4-2. 팀원이 의미 없는 커밋 메시지를 여러 개 push했을 때

- **원칙**: 공유된 히스토리는 합의 없이 다시 쓰지 않습니다(팀 규칙 + 미션 제약).
- **아직 리뷰 전인 본인 feature 브랜치**: 팀에 알리고 `git rebase -i`로 reword/squash한 뒤 `git push --force-with-lease`로 올립니다. `--force-with-lease`는 그사이 다른 사람이 push한 내용이 있으면 덮어쓰지 않고 멈춥니다.
- **이미 리뷰 중이거나 다른 사람이 받아간 경우**: 히스토리는 그대로 두고, PR 본문에 커밋별 실제 내용을 정리합니다. 필요하면 병합할 때 Squash merge로 의미 있는 메시지 하나로 합칩니다(GitHub 병합 화면에서 메시지 수정 가능).
- **가장 최근 1개이고 아직 push 전**: `git commit --amend`로 고치면 됩니다.
- **재발 방지**: [CONTRIBUTING > 커밋 메시지](https://github.com/wasw2123/cds-b2-2/blob/main/docs/CONTRIBUTING.md#커밋-메시지)에 금지 예시를 두고, 리뷰 때 커밋 메시지도 함께 봅니다.

### 4-3. 같은 파일/같은 영역에서 충돌이 반복될 때

- **원인 분석**: `git log --format="%h %an %s" -- <파일>`로 그 파일을 누가 얼마나 자주 고치는지 봅니다. 우리 팀에서는 `CONTRIBUTING.md`와 `troubleshooting-log.md`처럼 모두가 함께 쓰는 문서가 핫스팟이었습니다. 원인은 대부분 ① 여러 명이 같은 위치(파일 끝 등)에 추가, ② 파일 전체를 새로 쓰기, ③ 오래 열려 있는 브랜치였습니다.
- **예방 방안**
  - 섹션 뼈대를 먼저 병합하고 각자 담당 섹션만 수정합니다(우리가 #14, #22에서 적용).
  - PR을 작게 만들고 빨리 병합합니다. 오래 걸리는 브랜치는 수시로 `main`을 받아옵니다(PR의 `Update branch`).
  - PR 전에 `git merge-tree --write-tree origin/main <내 브랜치>`로 충돌을 미리 확인합니다.
  - 핫스팟 파일은 `.github/CODEOWNERS`로 담당 리뷰어를 지정해 변경을 한 사람이 조율하게 합니다.
  - 정말 자주 부딪히는 문서는 시나리오별 파일처럼 여러 파일로 나눕니다.

### 4-4. (보너스) 리베이스가 히스토리를 깨끗하게 하지만 협업에서 위험한 이유

- 보너스 과제(rebase -i)는 아직 수행하지 않았습니다. 아래는 설명입니다.
- **장점**: 커밋을 최신 `main` 위로 다시 쌓아 merge 커밋 없는 일직선 히스토리를 만들고, `-i`로 자잘한 커밋을 합치거나 메시지를 다듬을 수 있습니다.
- **위험**: 리베이스는 기존 커밋을 해시가 다른 새 커밋으로 바꿉니다. 이미 공유한 브랜치를 리베이스하면 다른 사람이 가진 히스토리와 어긋나 강제 push가 필요해지고, 그 브랜치를 받아 작업하던 팀원의 커밋이 꼬이거나 사라질 수 있습니다.
- **안전 수칙**
  - 아무도 받아가지 않은 본인 브랜치에서만 합니다.
  - `main`과 공유 브랜치에서는 하지 않습니다(우리 `main`은 ruleset의 `non_fast_forward`로 강제 push 자체가 차단됨).
  - push가 필요하면 `--force` 대신 `--force-with-lease`를 쓰고, 팀에 미리 알립니다.
  - 리베이스 전 백업 브랜치를 만들어 둡니다(`git branch backup/<브랜치>`). 꼬이면 `git reflog`로 되돌릴 수 있습니다.
