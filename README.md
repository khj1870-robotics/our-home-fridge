<div align="center">

<img src="docs/images/banner.svg" alt="우리집 냉장고 - 냉장고 관리부터 끼니 해결까지" width="100%">

<p>
  <img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/Built_with-Claude-D97757?logo=anthropic&logoColor=white" alt="Built with Claude">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License"></a>
</p>

**냉장고 재료를 한눈에 관리하고, 그 재료로 요리 계획을 세워 끼니를 해결하도록 돕는 2인 가구용 모바일 웹앱**

[주요 기능](#-주요-기능) · [실행 방법](#-실행-방법) · [계산 규칙](#-계산-규칙) · [개발 일정](#-개발-일정) · [개발 과정](#-개발-과정) · [참고 자료](#-참고-자료)

</div>

---

## 💡 왜 만들었나

룸메이트와 동거를 시작하면서 식비를 줄이기 위해 요리를 자주 하게 되었습니다. 하지만 매번 메뉴를 정하고 재료를 준비하는 과정이 번거로웠고, 둘 다 바쁜 시간이 반복되면 냉장고 현황을 자주 체크하지 못했습니다. 그러다보니 점점 외식이 늘었지요.

이 앱을 만든 취지는 집밥을 자주, 귀찮지 않게, 게으르게 할 수 있게 도와주는 냉장고 비서를 만드는 것이었습니다. 재료를 썩히지 않고 현명하게 소진하는 것부터 시작해서, 외식을 하지 않아서 아낀 비용을 보며 뿌듯함까지 챙기는 서비스입니다.

우리 생활에서 AI가 크게 도와줄 수 있는 부분이 이런 것이라고 생각했습니다. 인간은 밥을 먹어야 하고, 밥을 먹기 위해 돈을 벌어야 합니다. 밥과 돈을 모두 관리해주면 인간의 생존 조건을 근본적으로 도와주는 것인 셈이죠. 즉, 삶의 질을 높이고 싶었습니다.

모든 1인 가구, 2인 가구들이 굶지 말고 잘 살았으면 좋겠습니다. 물론, 3인 이상 가구도요.

이 앱은 다음과 같은 과정을 하나로 이어줍니다. 여기서 사람이 할 일은 영수증을 찍고, 남은 재료에 따라 메뉴를 결정하고, 그날 끼니를 먹었는지 체크하는 것입니다.

<p align="center">
🛒 <b>장보기</b> (영수증 찍기)
&nbsp;➡️&nbsp; 🥬 <b>냉장고 재고</b>
&nbsp;➡️&nbsp; 📝 <b>식단 계획</b>
&nbsp;➡️&nbsp; 🍽️ <b>먹음 처리</b>
&nbsp;➡️&nbsp; 💰 <b>재고·식비 반영</b>
&nbsp;➡️&nbsp; 🛒 <b>다음 장보기</b>
</p>

| 단계 | 앱이 하는 일 |
| --- | --- |
| 재고 확인 | 재료 종류별로 재고를 확인하고, 유통기한 임박 재료를 표시해줍니다. |
| 요리 계획 | 현재 재고에서 만들 수 있는 요리를 추천해주고, 식단표 화면에서 오늘, 내일 메뉴를 유동적으로 결정 |
| 먹음과 동시에 재고 반영 및 식비 계산 | 먹음 처리 한 번에 재고 차감, 1인 단가 계산, 지난 식단 기록 |
| 덜 귀찮게, 간편한 기록 | 사람은 대강 입력하고, AI가 알아서 기록해줍니다. 정확한 양과 단가로 맞춤 |
| 구체적인 절약 경험 | 해먹은 끼니를 외식 기준가와 비교해 아낀 돈을 보여줌 |

## ✨ 주요 기능

| 탭 | 기능 |
| --- | --- |
| 🧊 냉장고 | 칸별 재고, 유통기한 신호등, 먼저 먹기 표시, 냉동 표시, 꾹 눌러 옮기기, 재료를 솥에 넣어 요리 만들기 |
| 🍱 식단표 | 어제·오늘·내일 끼니, 재료 넣기, 먹음·건너뜀 처리, 도시락·외식 표시, 1인 단가 자동 계산 |
| 📅 지난 식단 | 주간·월간 달력, 자주 먹은 메뉴·재료, 식비, 영양 비율, 술 기록 |
| 🧾 가계부 | 영수증 사진 인식, 식재료·생활용품 분리, 이번달 숨쉬기 비용, 오토바이 연비 |

<!-- 스크린샷·데모 GIF: docs/images/ 에 추가 예정 -->
> 📸 탭별 스크린샷과 사용 흐름 데모 GIF는 예시 데이터로 촬영해 추가할 예정입니다.

## 🚀 실행 방법

| 버전 | 상태 | 저장 | 영수증 인식 |
| --- | --- | --- | --- |
| 본 앱 (Claude 아티팩트) | 사용 중 | Claude 아티팩트 저장소 | Claude 내장 AI |
| 독립 실행 버전 (`app/`) | 만드는 중 | 브라우저 저장소(IndexedDB) | 직접 입력 또는 예시 결과 |

- 본 앱은 Claude 계정으로 로그인해야 저장된 데이터와 영수증 인식을 쓸 수 있습니다.
- 평가자와 누구나 로그인 없이 열어 볼 수 있도록 **독립 실행 버전**을 만들고 있습니다. 완성되면 `app/index.html`을 브라우저로 여는 방법과 GitHub Pages 주소를 이곳에 적습니다.
- 실제 영수증·식단·이름은 저장소에 올리지 않고, `data/sample/`의 예시 데이터로 시연합니다.

## 🧮 계산 규칙

| 항목 | 규칙 |
| --- | --- |
| 금액 단위 | 저장과 계산 모두 1원 단위. 나누고 남는 원은 마지막 항목에 붙여 합계를 맞춤 |
| 원본 금액 | 금액은 영수증 항목 한 곳에만 두고, 재고·끼니 금액은 모두 거기서 계산 |
| 배송비 | 같이 산 상품 개수로 똑같이 나눔 (같은 상품 3개면 3개로 셈) |
| 할인 | 영수증에 찍힌 행사 할인·쿠폰만, 가격에 비례해 나눔 (카드 할인·적립금 제외) |
| 재고 | 같은 재료를 또 사면 산 날·가격별 묶음으로 두고, 먼저 산 것부터 씀 |
| 1인 단가 | 그 끼니에 쓴 재료 금액 ÷ 먹은 사람 수. 여러 끼니에 나눠 먹는 요리는 다 먹은 시점에 실제 먹은 인분으로 나눔 |
| 외식 비교 | 외식 1끼 기준가 기본값 10,000원과 1인 단가를 비교 |
| 오토바이 연비 | 가득 주유 사이 주행거리(km) ÷ 그 사이 넣은 연료량(L) |

전체 규칙과 결정 기록은 기획서에 정리했습니다.

## 📅 개발 일정

일정은 [구글 시트](https://docs.google.com/spreadsheets/d/1r8RBJvEdbfDC4w6hNwSiXqFveHQJivf6P9-myf62BhA)에서 관리하고, 매일 GitHub Actions가 아래 배지와 차트를 자동으로 갱신합니다 ([`scripts/sync_schedule.py`](scripts/sync_schedule.py)).

<!-- schedule:start -->
![진행률](https://img.shields.io/badge/progress-41%25-blue) ![완료](https://img.shields.io/badge/done-13-4CAF7D) ![진행 중](https://img.shields.io/badge/doing-1-3B7DDD) ![예정](https://img.shields.io/badge/todo-18-B7CDEB)

전체 진행률 **41%** · 완료 13 · 진행 중 1 · 예정 18 (작업 32개) · 자세한 일정: [구글 시트](https://docs.google.com/spreadsheets/d/1r8RBJvEdbfDC4w6hNwSiXqFveHQJivf6P9-myf62BhA)

```mermaid
gantt
    dateFormat YYYY-MM-DD
    axisFormat %m/%d
    todayMarker stroke-width:3px,stroke:#D93025
    section 기획
    가계 분석·요구사항 정리 :done, 2026-10-09, 2d
    엑셀 가계부 :done, 2026-10-11, 1d
    기획서 작성 :done, 2026-10-23, 3d
    section 디자인
    식단표 화면 개선 :done, 2026-10-12, 2d
    화면 시안 :done, 2026-10-22, 1d
    재디자인 ver2 :done, 2026-10-24, 3d
    새 디자인으로 다시 만들기 :2026-12-07, 25d
    section 개발
    첫 웹앱 :done, 2026-10-11, 2d
    레시피·솥 요리 :done, 2026-10-15, 3d
    등분·정산 :done, 2026-10-19, 4d
    식단표 기능 :done, 2026-10-23, 1d
    돈 계산 개편 0~5단계 :done, 2026-10-26, 2d
    독립 실행 버전 :2026-11-25, 4d
    돈 계산 개편 6단계 :2026-11-29, 3d
    돈 계산 개편 7단계 :2026-12-07, 14d
    웹앱을 앱으로 포장 :2027-01-01, 31d
    로그인·클라우드 저장 :2027-01-01, 31d
    영수증 인식 비용 줄이기 :2027-01-10, 22d
    section 테스트
    카메라 첨부 버그 수정 :done, 2026-10-25, 1d
    실사용· 연비 기록 :done, 2026-10-31, 1d
    테스트·버그 수정 :2026-12-02, 2d
    두 사람 실사용 점검 :2026-12-21, 11d
    section 제출
    범위 확정·저장소 만들기 :active, 2026-11-23, 2d
    README 작성 :2026-12-04, 1d
    실행 확인·제출 :2026-12-05, 1d
    과제 마감 :2026-12-06, 1d
    section 출시
    테스터 모집 :2027-01-15, 17d
    Google Play 비공개 테스트 :2027-02-01, 20d
    iOS TestFlight 테스트 :2027-02-01, 28d
    스토어 등록 정보 :2027-02-15, 14d
    프로덕션 검토·심사 :2027-03-01, 15d
    스토어 출시 :2027-03-31, 1d
    section 마감
    과제 제출 마감 :milestone, crit, 2026-12-06, 0d
```
<!-- schedule:end -->

## 🛠 개발 과정

날짜별로 한 일과 그때 부딪힌 문제·결정은 [`docs/devlog/`](docs/devlog/)에 있습니다.

> 저장소는 2026-11-23에 만들었습니다. 그 전(2026-10-09 ~ 10-31) 작업은 개발 기록을 바탕으로 해당 날짜에 복원한 커밋이며, 커밋 메시지 앞에 `[기록 복원]`이 붙어 있습니다. 그 뒤로는 실제 작업한 날짜로 커밋합니다.

<details>
<summary><b>폴더 구조</b></summary>

```
app/              앱 코드 (독립 실행 버전)
data/sample/      예시 데이터 (실제 생활 데이터는 올리지 않음)
docs/devlog/      날짜별 개발 기록
docs/images/      배너·스크린샷·데모 GIF
docs/references/  개발에 참고한 공식 문서 정리
scripts/          일정 동기화 스크립트 (Python)
.github/          GitHub Actions 설정
```

</details>

## 📚 참고 자료

- [개발에 필요한 공식 문서 정리](docs/references/official-docs-gpt.md): Claude 아티팩트 저장·공유, MDN(날짜·파일 입력·IndexedDB), 식약처 소비기한·영양 DB, W3C 접근성, GitHub 문서
- 외부 코드·이미지·폰트를 쓰면 출처와 라이선스를 이곳에 적습니다. 배너 이미지는 직접 만든 SVG입니다.

## 🤖 AI 도구 사용

| 도구 | 쓴 곳 |
| --- | --- |
| Claude (Anthropic) | 기획, 계산 규칙 설계, 코드 작성, 문서 작성. 해당 커밋에 `Co-Authored-By: Claude` 표시 |
| ChatGPT (OpenAI) | 공식 문서 조사 정리 ([`docs/references/`](docs/references/)) |
| GitHub Copilot | PR 코드 리뷰 (예정) |

## 📄 라이선스

[MIT License](LICENSE) © 2026 khj1870-robotics
