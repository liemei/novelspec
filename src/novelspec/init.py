"""`novelspec init` — scaffold a new novel project in the current directory.

Works like OpenSpec:
    pip install novelspec          # global install (once)
    cd my-project                  # go to any directory
    novelspec init                 # creates NovelSpec files here
    novelspec init my-novel        # creates a new directory
"""

from pathlib import Path

import novelspec.templates as tpl

# Mapping of relative path → content function
SKELETON: dict[str, callable] = {
    "novel.yaml": tpl.novel_yaml,
    "world/background.md": tpl.world_background,
    "world/timeline.md": tpl.world_timeline,
    "world/glossary.md": tpl.world_glossary,
    "characters/profiles/.gitkeep": lambda: "",
    "characters/relationships.md": tpl.characters_relationships,
    "characters/speech-patterns.md": tpl.characters_speech_patterns,
    "plot/overview.md": tpl.plot_overview,
    "plot/parts/.gitkeep": lambda: "",
    "plot/outlines/.gitkeep": lambda: "",
    "plot/foreshadowing.md": tpl.plot_foreshadowing,
    "plot/sub-arcs/.gitkeep": lambda: "",
    "style/narrative-samples.md": tpl.style_narrative_samples,
    "style/forbidden.md": tpl.style_forbidden,
    "style/conventions.md": tpl.style_conventions,
    "rules/quality-standards.md": tpl.rules_quality_standards,
    "prompts/daily-write.md": tpl.prompt_daily_write,
    "prompts/revise-chapter.md": tpl.prompt_revise_chapter,
    "prompts/audit-consistency.md": tpl.prompt_audit_consistency,
    "prompts/worldbuild.md": tpl.prompt_worldbuild,
    "prompts/outline.md": tpl.prompt_outline,
    "prompts/reader-review.md": tpl.prompt_reader_review,
    "prompts/propose-framework.md": tpl.prompt_propose_framework,
    "state/current-status.md": tpl.state_current_status,
    "state/chapter-log.md": tpl.state_chapter_log,
    "state/unresolved-threads.md": tpl.state_unresolved_threads,
    "framework/archive/.gitkeep": lambda: "",
    "meta/changelog.md": tpl.meta_changelog,
}


def run_init(target: Path, force: bool = False) -> None:
    root = target.resolve()

    # --- Create the target directory if needed ---
    root.mkdir(parents=True, exist_ok=True)

    # --- Safety check: refuse if novel.yaml already exists ---
    novel_yaml_path = root / "novel.yaml"
    if novel_yaml_path.exists() and not force:
        print(
            f"⚠️  {root}/novel.yaml 已存在。\n"
            f"   如要重新初始化，请使用 novelspec init --force"
        )
        return

    # --- Scaffold all files ---
    print(f"📁  NovelSpec 项目已创建: {root}\n")

    for rel_path, content_fn in SKELETON.items():
        full = root / rel_path
        full.parent.mkdir(parents=True, exist_ok=True)
        content = content_fn()
        content = content.replace("{{PROJECT_PATH}}", str(root))
        full.write_text(content, encoding="utf-8")
        print(f"  ✓  {rel_path}")

    # --- Agent instructions for Claude Code ---
    agents_dir = root / ".claude" / "skills"
    agents_dir.mkdir(parents=True, exist_ok=True)
    (agents_dir / "novelspec.md").write_text(
        tpl.agent_claude_code(), encoding="utf-8"
    )
    print("  ✓  .claude/skills/novelspec.md")

    print(
        """
✅ NovelSpec 项目初始化完成！

接下来：
  1. 编辑 novel.yaml 填写小说元信息
  2. 提供你的素材 → 和 AI 说 /novel:worldbuild
  3. AI 会引导你完成框架搭建

参考命令:
  /novel:status       查看进度
  /novel:review       读者视角审阅（章节/大纲/框架）
  /novel:help         所有可用命令
"""
    )
