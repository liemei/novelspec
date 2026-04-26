"""`novelspec status` — show writing progress."""

from pathlib import Path

import yaml


def run_status(root: Path) -> None:
    meta = _load_novel_yaml(root / "novel.yaml")
    chapters = _scan_chapters(root)
    foreshadowing = _count_foreshadowing(root)

    print(f"\n📖  {meta.get('书名', '未命名')}")
    print(f"{'=' * 40}")
    print(f"  类型:       {meta.get('类型', '—')}")
    print(f"  规划:       {meta.get('总部数', '?')} 部 / {meta.get('总章数规划', '?')} 章")
    print(f"  已写:       {chapters['written']} 章 ({chapters['total_words']:,} 字)")
    if meta.get('目标总字数'):
        pct = (chapters['total_words'] / meta['目标总字数']) * 100
        print(f"  字数进度:   {chapters['total_words']:,} / {meta['目标总字数']:,} ({pct:.1f}%)")
    print(f"  埋点:       {foreshadowing['total']} 个（待回收 {foreshadowing['pending']}，已回收 {foreshadowing['resolved']}）")
    print(f"  创作天数:   {chapters.get('days', '?')} 天")
    print(f"  下一章:     {chapters.get('next_chapter', '—')}")
    print()


def _load_novel_yaml(path: Path) -> dict:
    if path.exists():
        try:
            return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception:
            return {}
    return {}


def _scan_chapters(root: Path) -> dict:
    parts_dir = root / "chapters"
    written = 0
    total_words = 0
    all_chs = []
    days = set()

    if parts_dir.exists():
        for part_dir in sorted(parts_dir.iterdir()):
            if not part_dir.is_dir():
                continue
            for ch_dir in sorted(part_dir.iterdir()):
                if not ch_dir.is_dir() or not ch_dir.name.startswith("ch-"):
                    continue
                content_file = ch_dir / "content.md"
                if content_file.exists():
                    written += 1
                    all_chs.append(ch_dir.name)
                    # Rough word count
                    text = content_file.read_text(encoding="utf-8")
                    total_words += len(text.replace("\n", " ").split())

    next_ch = f"ch-{len(all_chs) + 1:03d}" if all_chs else "ch-001"

    return {
        "written": written,
        "total_words": total_words,
        "next_chapter": next_ch,
        "days": len(days) or "?",
    }


def _count_foreshadowing(root: Path) -> dict:
    foreshadow_file = root / "plot" / "foreshadowing.md"
    total = 0
    pending = 0
    resolved = 0

    if foreshadow_file.exists():
        for line in foreshadow_file.read_text(encoding="utf-8").splitlines():
            if "待回收" in line:
                pending += 1
                total += 1
            elif "已回收" in line:
                resolved += 1
                total += 1

    return {"total": total, "pending": pending, "resolved": resolved}
