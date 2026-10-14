# 친구 3~5명과 함께 프로그램 만드는 법 연습하기

5명의 팀원이 연산 함수를 분담하여 작성하고 Git·GitHub 협업을 실습하는 프로젝트입니다.
구현할 연산은 **더하기, 빼기, 몫, 나머지, 곱하기**의 5가지이며, 팀원별로 하나씩 담당합니다.
복잡한 기능 구현보다 이슈 기반 작업, PR과 코드 리뷰, 충돌 해결 및 트러블슈팅 기록에 집중합니다.

## 개발 환경

- Python 3.10 이상
- Git 및 GitHub
- 테스트: Python 내장 `unittest` 사용

Python은 특정 버전으로 고정하지 않습니다. 작업 전에 설치된 버전을 확인합니다.

```bash
python3 --version
```

## 디렉터리 구성

```text
cds-b2-2/
├── README.md                      # 프로젝트 안내
├── .gitignore                     # 팀 공통 Git 제외 규칙
├── .github/
│   └── pull_request_template.md    # PR 작성 양식
├── src/                           # 서비스 코드
├── tests/                         # 테스트 파일
└── docs/                          # 협업 규칙 및 실습 기록
    ├── CONTRIBUTING.md
    ├── conflict-resolution.md
    └── troubleshooting-log.md
```

## 연산 구성
<!-- TODO 자신이 제작한 함수와 파일, 상태를 업데이트 해주세요 -->
| 연산 | 함수 | 파일 | 현재 로컬 상태 |
| --- | --- | --- | --- |
| 더하기 | `add(a, b)` | [src/addition.py](src/addition.py) | 구현됨 |
| 빼기 | 추가 예정 | 추가 예정 | 미반영 |
| 몫 | 추가 예정 | 추가 예정 | 미반영 |
| 나머지 | 추가 예정 | 추가 예정 | 미반영 |
| 곱하기 | `multiplier(a, b)` | [src/multiplier.py](src/multiplier.py) | 구현됨 |

팀원별 담당 함수를 추가하면서 함수 목록과 사용 예시를 갱신합니다.

## 사용 방법

저장소를 내려받고 프로젝트 루트로 이동합니다.

```bash
git clone https://github.com/wasw2123/cds-b2-2.git
cd cds-b2-2
python3
```

Python에서 다음과 같이 사용합니다.

```python
from src.addition import add
from src.multiplier import multiplier

add(1, 2)         # 3
add(-1, -2)       # -3
multiplier(2, 3)  # 6
multiplier(-2, 3) # -6
```

## 테스트 실행

프로젝트 루트에서 전체 테스트를 실행합니다.

```bash
python3 -m unittest discover -s tests -v
```

덧셈 테스트만 실행하려면 다음 명령을 사용합니다.

```bash
python3 -m unittest discover -s tests -p 'test_add.py' -v
```

## 협업 방식

GitHub Flow를 사용하며, 팀 컨벤션에 따라 작업 브랜치는 `feat/작업명`으로 작성합니다.
각 작업을 Issue로 만들고, PR에서 리뷰·검증·승인을 거친 뒤 `main`에 병합합니다.

GitHub Flow 선택 이유:

- 간단한 연산 함수 모음으로, 별도 개발 서버나 여러 릴리스 버전을 관리할 필요가 없어 `main`과 작업 브랜치만으로 충분합니다.
- PR·리뷰·검증 후 병합하여 `main`을 정상 동작하는 상태로 유지합니다.
- 이슈 기반 작업, 코드 리뷰, 충돌 해결 등 이번 미션의 협업 과정에 집중할 수 있습니다.

## 협업 문서 및 제출

- [기여 가이드](docs/CONTRIBUTING.md): 브랜치 및 커밋 메시지 규칙
- [충돌 해결 기록](docs/conflict-resolution.md): 실제 충돌의 상황·해결 과정·결과 기록
- [트러블슈팅 기록](docs/troubleshooting-log.md): Git 실습의 명령·결과·주의점 기록
- [제출물 인덱스](SUBMISSION.md): 팀원별 Issue·PR·문서·증빙 링크
