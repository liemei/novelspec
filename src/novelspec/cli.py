"""NovelSpec CLI — the entry point.

Usage:
    novelspec init [目录]        # 在指定目录（或当前目录）创建小说项目
    novelspec init --force       # 强制重新初始化
    novelspec status             # 查看写作进度
    novelspec help               # 显示帮助
"""

import argparse
import sys
from pathlib import Path

from novelspec.init import run_init
from novelspec.status import run_status

PROJECT_FILE = "novel.yaml"


def find_project_root(start: Path | None = None) -> Path | None:
    """Walk up from start (or cwd) looking for novel.yaml."""
    cwd = start or Path.cwd()
    for parent in [cwd] + list(cwd.parents):
        if (parent / PROJECT_FILE).exists():
            return parent
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="novelspec",
        description="Spec-driven long-form novel creation.",
        epilog="Run `novelspec help` for available commands.",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- init ---
    init_parser = subparsers.add_parser(
        "init", help="初始化小说项目（在已有目录或新目录中）"
    )
    init_parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="目标目录（默认当前目录）",
    )
    init_parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="强制重新初始化（覆盖现有 novel.yaml）",
    )

    # --- status ---
    status_parser = subparsers.add_parser("status", help="查看写作进度")

    # --- help ---
    subparsers.add_parser("help", help="显示帮助信息")

    ns = parser.parse_args(argv or sys.argv[1:])

    if ns.command is None or ns.command == "help":
        print_help()
        return 0

    if ns.command == "init":
        run_init(Path(ns.target), force=ns.force)
        return 0

    if ns.command == "status":
        root = find_project_root()
        if not root:
            print(
                "❌ 找不到 novel.yaml — 请先运行 novelspec init，或进入小说项目目录后重试。"
            )
            return 1
        run_status(root)
        return 0

    return 0


def print_help() -> None:
    print(
        r"""
╔══════════════════════════════════════════╗
║           NovelSpec  v1.0.0              ║
║   Spec-driven long-form novel creation   ║
╚══════════════════════════════════════════╝

Inspired by OpenSpec — write novels with AI the
same way you build software: spec first.

GLOBAL INSTALL
    pip install novelspec          # 装一次，到处用

USAGE
    cd my-project
    novelspec init                 # 在当前目录创建小说项目
    novelspec init my-novel        # 创建新目录并初始化
    novelspec init --force         # 强制重新初始化
    novelspec status               # 查看写作进度
    novelspec help                 # 显示本帮助

SLASH COMMANDS (in AI chat)
    /novel:init         初始化小说项目
    /novel:worldbuild   根据素材生成世界观框架
    /novel:outline      创建章节大纲
    /novel:write        创作章节
    /novel:show         阅读已写内容
    /novel:revise       修改章节
    /novel:propose      提出框架变更
    /novel:accept       确认并应用框架变更
    /novel:archive      归档已完成变更
    /novel:audit        一致性审计
    /novel:status       查看写作进度
"""
    )


if __name__ == "__main__":
    sys.exit(main())
