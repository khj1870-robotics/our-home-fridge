"""
구글 시트 '일정 입력'을 읽어 README.md 안의 간트 차트(Mermaid)를 다시 쓰는 스크립트.

- GitHub Actions(.github/workflows/sync-schedule.yml)가 매일 자동으로 실행합니다.
- 직접 실행: python scripts/sync_schedule.py            (구글 시트에서 내려받기)
            python scripts/sync_schedule.py 파일.csv   (내려받은 CSV로 테스트)

README.md 안의 아래 두 줄 사이만 바꿉니다.
    <!-- schedule:start -->
    <!-- schedule:end -->
"""
import csv
from datetime import date
import io
import re
import sys
import urllib.request
from pathlib import Path

SHEET_ID = "1r8RBJvEdbfDC4w6hNwSiXqFveHQJivf6P9-myf62BhA"
INPUT_GID = "1501570673"  # '일정 입력' 시트
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={INPUT_GID}"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}"
DEADLINE = ("과제 제출 마감", "2026-12-06")

README = Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!-- schedule:start -->", "<!-- schedule:end -->"
ORDER = ["기획", "디자인", "개발", "테스트", "제출", "출시"]


def load_rows(src=None):
    if src:
        text = Path(src).read_text(encoding="utf-8-sig")
    else:
        with urllib.request.urlopen(CSV_URL, timeout=30) as r:
            text = r.read().decode("utf-8-sig")
    rows = list(csv.reader(io.StringIO(text)))
    # 제목·안내 줄을 건너뛰고 '구분'으로 시작하는 머리글을 찾음
    head = next(i for i, r in enumerate(rows) if r and r[0].strip() == "구분")
    cols = [c.strip() for c in rows[head]]
    out = []
    for r in rows[head + 1:]:
        d = dict(zip(cols, (c.strip() for c in r)))
        if d.get("구분") and d.get("작업") and re.match(r"\d{4}-\d{2}-\d{2}", d.get("시작일", "")):
            out.append(d)
    return out


def clean(name):
    # Mermaid 간트에서 ':' '#' ';'는 문법 기호라 바꿔 씀
    return name.replace(":", "·").replace("#", "").replace(";", ",")


def mermaid(rows):
    lines = ["```mermaid", "gantt", "    dateFormat YYYY-MM-DD", "    axisFormat %m/%d",
             "    todayMarker stroke-width:3px,stroke:#D93025"]
    cats = sorted({r["구분"] for r in rows}, key=lambda c: ORDER.index(c) if c in ORDER else 99)
    for cat in cats:
        lines.append(f"    section {cat}")
        for r in sorted((r for r in rows if r["구분"] == cat), key=lambda r: r["시작일"]):
            tag = {"완료": "done, ", "진행 중": "active, "}.get(r["상태"], "")
            end = r.get("완료일") or r["시작일"]
            # Mermaid의 끝 날짜는 그날을 포함하지 않으므로 기간(일)로 적음
            days = (date.fromisoformat(end) - date.fromisoformat(r["시작일"])).days + 1
            lines.append(f"    {clean(r['작업'])} :{tag}{r['시작일']}, {days}d")
    lines.append("    section 마감")
    lines.append(f"    {DEADLINE[0]} :milestone, crit, {DEADLINE[1]}, 0d")
    lines.append("```")
    return "\n".join(lines)


def summary(rows):
    n = len(rows)
    cnt = {s: sum(r["상태"] == s for r in rows) for s in ("완료", "진행 중", "예정")}
    pct = [float(r["진행률"].rstrip("%")) / 100 for r in rows if r.get("진행률", "").rstrip("%").replace(".", "").isdigit()]
    avg = round(sum(pct) / len(pct) * 100) if pct else 0
    return (f"전체 진행률 **{avg}%** · 완료 {cnt['완료']} · 진행 중 {cnt['진행 중']} · 예정 {cnt['예정']} "
            f"(작업 {n}개) · 자세한 일정: [구글 시트]({SHEET_URL})")


def main():
    rows = load_rows(sys.argv[1] if len(sys.argv) > 1 else None)
    block = f"{START}\n{summary(rows)}\n\n{mermaid(rows)}\n{END}"
    text = README.read_text(encoding="utf-8") if README.exists() else f"# 우리집 냉장고\n\n## 개발 일정\n\n{START}\n{END}\n"
    if START not in text:
        text += f"\n## 개발 일정\n\n{START}\n{END}\n"
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    if new != text:
        README.write_text(new, encoding="utf-8")
        print("README 일정 갱신")
    else:
        print("바뀐 내용 없음")


if __name__ == "__main__":
    main()
