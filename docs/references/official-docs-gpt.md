# 우리집 냉장고 개발에 필요한 공식 문서

2026년 11월 23일 확인 · HTML·CSS·JavaScript 단일 파일 / Claude Artifacts / 2인 가구

먼저 확인할 항목은 **두 계정의 저장 권한, 영수증 인식 실패 시 입력 경로, 평가자가 열 수 있는 제출본**이다. 테스트용 사본은 비로그인 상태에서도 네 개 탭이 열렸고, 저장된 데이터를 보려면 로그인하라는 안내가 표시됐다. 앱 소스, 두 계정의 동기화, 영수증 인식 실동작은 확인하지 못했다. 아래의 적용 사항은 제공된 개발 일정표와 공개 화면, 공식 문서를 기준으로 정리했다.

## 1. Claude Artifacts 실행, 저장, 공유

| 구분 | 확인할 내용 | 공식 문서 |
| --- | --- | --- |
| 아티팩트 유형 | 현재 앱의 메뉴에서 `Share` 또는 `Publish`를 확인한다. 테스트용 사본에는 `Share`가 표시됐다. Anthropic은 새 아티팩트와 레거시 아티팩트의 저장 및 게시 동작을 구분한다. 새 유형은 게시 전에도 저장할 수 있다. 레거시 유형은 저장을 쓰려면 게시해야 하며 게시 취소 시 저장 데이터가 영구 삭제된다. | [Anthropic · 아티팩트 사용, AI, 저장소](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) · [아티팩트 공유](https://support.claude.com/en/articles/9547008-share-artifacts) |
| 개인 저장과 공유 저장 | 개인 저장은 사용자별로 분리되고 공유 저장은 접근 가능한 사용자가 같은 데이터를 본다. 두 사람이 하나의 냉장고를 쓴다면 계정 A와 B에서 같은 가상 재료가 보이는지, 양쪽에서 수정해도 반영되는지, 본 앱과 테스트 사본이 서로 영향을 주지 않는지 확인한다. 아티팩트 링크 접근 권한과 앱 데이터 쓰기 권한은 각각 확인한다. | [Anthropic · Store data in an artifact](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) · [공유 대상과 권한](https://support.claude.com/en/articles/9547008-share-artifacts) |
| 외부 평가자 접근 | 새 아티팩트에서 링크만 가진 비로그인 방문자는 저장 데이터와 Claude 기능에 제한이 있다. 링크를 받은 조직 외부 사용자 역시 문서에 설명된 범위에서 저장 변경과 AI 사용이 제한될 수 있다. `평가자 링크 열기 → 네 탭 확인 → 샘플 확인 → 쓰기·인식 가능 여부 확인` 순으로 본다. | [Anthropic · What others can see and do](https://support.claude.com/en/articles/9547008-share-artifacts) |
| 아티팩트 내장 AI | 내장 Claude 기능의 로그인, 최초 사용 권한, 각 사용자의 사용량 한도를 확인한다. 파일 선택으로 사진을 모델에 전달하는 흐름, 아티팩트 저장소에 원본 파일을 보존하는 흐름, 별도 API로 보내는 흐름은 코드에서 각각 확인한다. Help Center의 사용 안내만으로 현재 앱이 호출하는 함수명과 인자까지 확정할 수 없다. | [Anthropic · Build AI-powered apps / Store data](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) |
| 실제 기록 백업 | 재고·식단·가계부를 앱에서 JSON으로 내보내고 테스트 사본으로 복원할 수 있는지 확인한다. Claude 계정의 데이터 내보내기 안내는 대화와 계정 데이터를 중심으로 설명한다. 그 내보내기로 앱 레코드가 복원되는지는 별도 확인이 필요하다. | [Anthropic · 계정 데이터 내보내기](https://support.claude.com/en/articles/9450526-export-your-claude-data) · [MDN · JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON) |

공식 문서의 기본 저장 한도는 새 아티팩트에서 **100 MB 또는 레코드 25,000개 중 먼저 도달하는 쪽**이다. 문서에 소개된 업로드 파일 한도는 별개다. 레거시 저장소는 아티팩트당 **20 MB의 텍스트 데이터**로 제한된다. 앱에서 실제로 쓰는 저장 경로를 확인한 뒤 해당 한도를 적용한다. [Anthropic · 아티팩트의 저장 한도](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)

## 2. 냉장고 탭

| 구현 지점 | 적용 기준 | 공식 문서 |
| --- | --- | --- |
| 꾹 눌러 칸 옮기기 | Pointer Events로 눌림·이동·해제를 처리하고, 스크롤 전환 등으로 `pointercancel`이 발생하면 드래그 상태를 초기화한다. 제스처 제어는 필요한 요소 범위에서 하고, 카드를 열어 목적 칸을 탭하는 방법도 제공한다. | [MDN · Pointer Events](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events/Using_Pointer_Events) · [MDN · touch-action](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/touch-action) · [W3C · 드래그의 대체 조작](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements) |
| 소비기한·먼저 먹기 | 기존 '유통기한' 필드가 실제로 무엇을 담는지 확인한다. 제품에 표시된 소비기한, 제품에 표시된 유통기한, 사용자가 지정한 '먼저 먹기' 날짜는 의미가 다르다. 소비기한은 표시된 보관방법 준수를 전제로 하므로, 냉동 표시만으로 앱이 날짜를 일괄 연장하지 않도록 한다. 색상에 '오늘', '임박', '지남', '미정' 같은 글자를 함께 표시한다. | [식약처 · 소비기한 자료](https://www.foodsafetykorea.go.kr/portal/board/board.do?menu_grp=MENU_NEW01&menu_no=4612) · [대한민국 정책브리핑·식약처 · 소비기한 Q&A](https://www.korea.kr/news/policyNewsView.do?newsId=148911130) · [W3C · 색상 사용](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) |
| 날짜 입력과 표시 | 포장 날짜와 식단 날짜는 시간 없는 `YYYY-MM-DD` 값으로 다룬다. 기록 생성 시각은 별도 값으로 구분한다. `Date.parse`는 날짜만 있는 표준 문자열을 UTC로 해석하므로, 브라우저의 현지 날짜로 변환하는 과정에서 날짜가 바뀌는지 확인한다. 이 앱의 일자 경계는 한국 기준으로 잡는다. | [MDN · 날짜 입력](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date) · [MDN · Date.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse) · [MDN · 날짜와 숫자 현지화](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Internationalization) |
| 솥 요리와 재고 차감 | 요리를 만들 때 사용량 차감과 완성 요리 추가가 한 작업으로 반영되는지 확인한다. 먼저 '요리 만들기'에서 차감한 재료가 '먹음' 처리에서 다시 빠지지 않게 한다. 중복 탭, 저장 실패, 두 계정의 동시 수정 시에도 기록이 맞아야 한다. 저장 방식의 실제 동시 쓰기 지원은 구현에서 확인한다. | [Anthropic · 아티팩트 저장](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) · [MDN · IndexedDB 트랜잭션, 독립 데모에서 선택 시](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB) |

## 3. 식단표와 지난 식단

| 구현 지점 | 적용 기준 | 공식 문서 |
| --- | --- | --- |
| 어제·오늘·내일, 주간·월간 달력 | 한국 자정과 월말·연말 경계, 한 주의 시작 요일, '먹음'·'건너뜀'·계획 기록의 집계 기준을 정한다. 날짜 선택값과 화면에 표시하는 날짜를 구분한다. | [MDN · 날짜 입력](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date) · [MDN · 날짜와 숫자 현지화](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Internationalization) |
| 1인 단가와 외식 비교 | 집밥 1인 단가는 `해당 끼니에 사용한 재료 원가 합 ÷ 실제 식사 인원`으로 정의하는 안을 권장한다. 여러 끼니에 나눠 먹는 솥 요리는 해당 끼니에 먹은 분량만 배분한다. 외식도 같은 1인 단위로 비교하고, 인원 0명이나 가격 미입력은 별도 상태로 표시한다. 모아 둔 비용을 합계할 때와 화면에서 반올림할 때의 기준을 정한다. | [MDN · Intl.NumberFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat) · [MDN · 안전한 정수](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger) |
| 영양 비율 | 식약처 DB의 식품코드, 생것·조리품 구분, 함량 기준량, 단위, 실제 사용량을 연결한다. DB에 100 g당 20 g으로 기록된 성분은 50 g을 먹었을 때 10 g으로 환산한다. 화면의 비율이 탄단지 중량 비율인지 열량 비율인지 표시한다. 정보가 없는 재료는 미확인으로 남기고 집계 범위를 알린다. | [식약처 · K-FIND 식품영양성분 DB](https://various.foodsafetykorea.go.kr/nutrient/) · [공공데이터포털 · 식품영양성분 DB Open API](https://www.data.go.kr/data/15127578/openapi.do) |
| 자주 먹은 메뉴·식비·술 기록 | 메뉴 빈도와 식비는 같은 날짜 범위와 기록 상태를 적용한다. 술 기록은 횟수, 금액, 양 중 무엇을 표시하는지 밝힌다. 장을 본 날의 **실제 지출**과 먹은 날의 **배분된 식사 원가**는 각 화면에서 이름을 분명히 붙인다. | [MDN · 숫자와 통화 표시](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat) |

1인 단가, 요리 분량 배분, 술 집계 방식은 앱이 정하는 계산 규칙이다. MDN은 날짜와 숫자의 처리 및 표시 동작을 확인하는 데 사용한다. 외식 절약액을 표시한다면 어떤 외식 단가를 비교 기준으로 사용했는지도 화면이나 README에 적는다.

## 4. 가계부와 영수증 인식

| 구현 지점 | 적용 기준 | 공식 문서 |
| --- | --- | --- |
| 사진 촬영·앨범 선택 | 파일 입력에서 카메라와 앨범 경로를 실기기로 확인한다. `capture="environment"`는 기기에 후면 카메라 사용을 요청하는 힌트다. `accept` 역시 선택기의 힌트이므로 선택 후 유형과 크기를 검사한다. JPG·PNG와 실제 휴대폰이 돌려주는 형식을 확인하고, 처리할 수 없는 형식에는 재선택 안내를 둔다. | [MDN · 파일 입력](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file) · [MDN · capture](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/capture) · [MDN · File API](https://developer.mozilla.org/en-US/docs/Web/API/File_API) |
| 업로드 전 사진 처리 | 큰 사진을 줄일 때는 가는 글자와 합계가 읽히는지 확인한다. 테스트에는 흐린 사진, 기울어진 사진, 긴 영수증, 영수증이 아닌 이미지를 포함한다. | [MDN · Canvas toBlob](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toBlob) · [Anthropic · Vision, 외부 API 사용 시 입력 사양](https://platform.claude.com/docs/en/build-with-claude/vision) |
| AI 결과 저장 | 인식 결과는 초안으로 보여준다. 상호·날짜·품목·수량·금액·할인·합계를 수정할 수 있게 하고, 불명확한 값은 빈칸으로 남긴다. 할인과 환불, 합계 불일치, 같은 영수증 재등록, AI 미지원이나 실패 후 수동 저장을 점검한다. OCR로 읽은 품목명이나 사용자 입력은 화면에 일반 텍스트로 렌더링한다. | [Anthropic · 아티팩트 내장 AI](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) · [MDN · textContent](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent) |
| 영수증과 개인정보 | 앱이 영수증 사진을 어디에 보내고 원본을 보존하는지 확인한다. 공개 저장소, 시연 화면, 예시 이미지에는 합성 영수증이나 개인정보를 가린 샘플을 사용한다. Claude 기능을 쓰는 경우 해당 서비스의 개인정보 설정과 보존 안내를 확인한다. | [Anthropic Privacy Center · 데이터 보존](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data) · [모델 개선 설정](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings) |
| 월 지출과 오토바이 연비 | 식재료·생활용품·기타 항목과 '숨쉬기 비용' 집계 범위를 정한다. 연비는 만땅에서 다음 만땅까지의 주행거리(km) ÷ 같은 구간에 보충한 연료량(L)으로 계산하는 안을 권장한다. 중간에 부분 주유를 했으면 그 양도 포함하고, 완료되지 않은 구간은 계산 대기로 표시한다. | [MDN · 숫자, 통화, 단위 표시](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat) |

**Claude API를 앱 밖에서 직접 호출하는 구조일 때**는 아래 문서를 추가로 본다. 내장 아티팩트에서 이미 AI를 호출한다면 현재 경로와 권한을 먼저 확인한다.

- 이미지 형식·크기·해상도와 요청 형식. [Anthropic · Vision](https://platform.claude.com/docs/en/build-with-claude/vision) · [Messages API](https://platform.claude.com/docs/en/api/messages/create)
- 기계가 읽는 응답 형식. JSON Schema로 구조를 제한하고, 품목과 합계가 실제 영수증과 맞는지는 앱에서 검증한다. [Anthropic · Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- 호출 인증, 오류, 사용량 한도. 직접 호출하는 API 키는 서버에 두고, 정적 HTML이나 공개 저장소에 포함하지 않는다. [Anthropic · 인증](https://platform.claude.com/docs/en/manage-claude/authentication) · [오류](https://platform.claude.com/docs/en/api/errors) · [사용량 제한](https://platform.claude.com/docs/en/api/rate-limits)

## 5. 모바일 화면과 실기기 확인

| 확인할 화면 | 적용 기준 | 공식 문서 |
| --- | --- | --- |
| 네 탭과 하단 바 | 뷰포트와 하단 안전 영역을 처리한다. 탭의 선택 상태와 패널 레이블, 키보드 초점을 확인한다. 글자 크기를 늘리고 브라우저 하단 바가 나타났을 때도 저장 버튼이 보여야 한다. | [MDN · viewport](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport) · [MDN · CSS env()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env) · [W3C · Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) |
| 작은 추가·삭제 버튼과 처리 상태 | 작은 아이콘의 터치 영역을 확인한다. WCAG 2.2의 최소 대상 크기 기준은 24×24 CSS px이며 간격 등 예외 조건을 문서에서 확인할 수 있다. 저장 완료와 인식 실패는 보이는 메시지로 표시하고 보조기기에도 전달한다. | [W3C · 최소 대상 크기](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum) · [W3C · 상태 메시지](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) |
| 실기기 테스트 | Android Chrome과 상대방이 쓰는 iPhone Safari에서 각각 파일 선택, 길게 누르기와 스크롤, 한국 자정 전후 날짜, 새로고침 후 저장 복구를 검증한다. iOS Web Inspector를 컴퓨터에서 연결하는 공식 절차는 Mac을 전제로 한다. | [Chrome DevTools · Android 원격 디버깅](https://developer.chrome.com/docs/devtools/remote-debugging/) · [WebKit · Web Inspector](https://webkit.org/web-inspector/enabling-web-inspector/) |

## 6. 공개 저장소와 과제 제출

| 해야 할 일 | 확인 기준 | 공식 문서 |
| --- | --- | --- |
| GitHub 공개 저장소 | 평가자가 로그아웃 상태에서 저장소와 소스코드를 열 수 있게 한다. 공개 전 샘플 데이터와 스크린샷, 저장소 이력에 실생활 기록이나 API 키가 포함돼 있는지 확인한다. | [GitHub · 저장소 빠른 시작](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories) · [민감한 데이터가 들어간 이력 처리](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) |
| README | 앱이 해결하는 문제, 4개 탭, 실행 방법, Claude 계정 및 권한 요구사항, 평가용 데모·스크린샷, 저장과 AI 의존성, 계산 기준, 외부 코드·이미지·폰트·데이터 출처를 기록한다. 과제 공지상 타인의 코드를 사용했다면 참고자료에 출처를 적는다. | [GitHub · README](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) |
| 라이선스 | 직접 작성한 코드에 적용할 `LICENSE`를 저장소에 두고, 외부 코드와 에셋의 라이선스·저작권 표시 조건을 확인한다. 디자인 에셋의 공개 범위도 확인한다. | [GitHub · 저장소 라이선스](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) · [Open Source Initiative · 승인 라이선스](https://opensource.org/licenses) |
| 제출 소스 ZIP | 제출 시점 커밋에서 소스 ZIP을 내려받아 풀고, 실행 파일과 참조 에셋, README, LICENSE가 있는지 확인한다. 저장소 URL과 ZIP은 같은 제출 버전을 가리키게 한다. | [GitHub · 브랜치·태그·커밋 소스 ZIP](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives) · [GitHub · Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) |
| 독립 실행 데모가 필요할 때 | GitHub Pages로 HTML·CSS·JavaScript를 제공할 수 있다. 아티팩트에서 제공되던 저장·AI 인터페이스는 독립 페이지용 실행 경로가 있어야 한다. 예를 들어 샘플 JSON, 브라우저 저장, 가상 영수증의 인식 결과 샘플로 주요 흐름을 시연할 수 있다. 평가자가 실제 AI를 사용할 수 있는지 확인된 범위를 README에 적는다. | [GitHub · Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) · [MDN · localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) · [MDN · IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) · [MDN · 브라우저 저장 한도와 삭제 조건](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria) |

브라우저 저장소를 쓰는 독립 데모는 해당 브라우저와 출처 기준으로 저장된다. 두 사람의 실시간 공유 기능까지 독립 환경에서 제공하려면 두 계정이 접근하는 공용 저장 경로가 필요하다. 이번 제출에서 어느 수준까지 시연할지는 평가자 접근 테스트 결과로 결정한다.

## 7. 12월 6일 제출까지 확인 순서

아래는 2026년 11월 23일 기준 제안 일정이다. 제출 마감은 **12월 6일 일요일 23:59, 한국 시간**이며, e-Class의 Term Project Submission에 Repository URL과 제출 시점 소스 ZIP을 낸다.

| 날짜 | 확인 작업 | 끝난 기준 |
| --- | --- | --- |
| 11/23–11/25 | 현재 아티팩트 유형·저장·공유 권한 확인 | 두 계정과 로그아웃 상태에서 읽기·쓰기·영수증 인식 가능 여부를 각각 기록한다. 테스트 사본과 본 앱의 분리도 확인한다. |
| 11/26–11/29 | 네 탭의 핵심 흐름 점검 | 가상 영수증 → 확인·저장 → 재료 등록 → 요리·식단 → 1인 단가 확인을 한 번 끝까지 실행한다. 사진 실패, 중복 처리, 월말 날짜를 별도로 확인한다. |
| 11/30–12/03 | 평가용 데모와 공개 저장소 준비 | 비로그인으로 열 수 있는 데모 또는 재현 절차를 마련한다. README, 스크린샷, 외부 자료 출처, LICENSE를 추가한다. |
| 12/04–12/05 | 제출 ZIP 작성과 제3자 환경 확인 | 고정한 커밋에서 받은 ZIP을 풀어 재실행하고, 로그아웃 상태에서 저장소와 시연 자료를 연다. |
| 12/06 | e-Class 제출 | 23:59 전에 저장소 URL과 같은 버전의 소스 ZIP을 제출하고 제출 상태를 확인한다. |
