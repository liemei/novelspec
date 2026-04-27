"""AI agent instruction files for different coding assistants."""


def agent_claude_code() -> str:
    return """---
name: novelspec
description: Spec-driven long-form novel creation — slash commands for AI-assisted storytelling
---

# NovelSpec — 小说创作工作流

NovelSpec 是一个 spec-driven 的长篇小说创作方法，受到 OpenSpec 启发。
本技能文件让 AI 了解 NovelSpec 的目录结构和命令体系。

## 目录结构（novel/）

```
novel/
├── novel.yaml                    # 小说元信息
├── world/                        # 世界观
│   ├── background.md             # 地理/历史/社会/魔法体系
│   ├── timeline.md               # 时间线
│   └── glossary.md               # 专有名词词典
├── characters/                   # 人物
│   ├── profiles/                 # 人物卡
│   ├── relationships.md          # 关系网
│   └── speech-patterns.md       # 说话方式
├── plot/                         # 剧情
│   ├── overview.md               # 总纲
│   ├── parts/                    # 各部梗概
│   ├── outlines/                 # 章节大纲
│   ├── foreshadowing.md          # 埋点追踪
│   └── sub-arcs/                 # 支线
├── style/                        # 风格
│   ├── narrative-samples.md      # 文风样本
│   ├── forbidden.md              # 禁忌清单
│   └── conventions.md            # 写作约定
├── rules/                        # 创作质量准则
│   └── quality-standards.md      # AI 必须遵循的九大创作规则
├── prompts/                      # Agent 工作指令
│   ├── daily-write.md            # 每日创作
│   ├── revise-chapter.md         # 修改章节
│   ├── audit-consistency.md      # 一致性审计
│   ├── worldbuild.md             # 框架构建
│   ├── outline.md                # 大纲创作
│   ├── propose-framework.md      # 框架变更
│   └── reader-review.md          # 读者视角审阅
├── state/                        # 状态追踪
│   ├── current-status.md         # 进度
│   ├── chapter-log.md            # 章节索引
│   └── unresolved-threads.md     # 未解决线索
├── chapters/                     # 产出
│   └── part-XX/
│       └── ch-NNN/
│           ├── summary.md        # 概要（供上下文）
│           ├── content.md        # 正文
│           ├── revisions/        # 历史版本
│           └── reviews/          # 读者视角审阅报告
├── framework/                    # 框架迭代
│   ├── <提案名>/                 # 当前提案
│   │   ├── proposal.md
│   │   └── specs/
│   └── archive/
└── meta/
    └── changelog.md
```

## 核心设计

### 三级存储
- **L1 框架层**: world/ + characters/ + plot/ + style/（几乎不变）
- **L2 状态层**: state/（每日更新，体积小）
- **L3 产出层**: chapters/（按需引用，只读 summary.md）

### 埋点追踪
foreshadowing.md 跟踪所有伏笔：ID、描述、埋入章节、计划回收、状态

### 框架迭代
framework/ 管理框架变更，含 proposal.md 和 archive/

## Slash 命令

### 初始搭建
- `/novel:init` — 初始化小说项目
- `/novel:worldbuild` — 根据素材生成世界观框架（交互式，逐件确认）
- `/novel:outline [part-XX]` — 创建章节大纲

### 日常创作
- `/novel:write` — 创作下一章（根据 prompts/daily-write.md 的指令）
- `/novel:write --count N` — 批量创作 N 章

### 审阅修改
- `/novel:show ch-NNN` — 阅读章节
- `/novel:show ch-NNN summary` — 只看概要
- `/novel:show --recent N` — 看最近 N 章概要
- `/novel:revise ch-NNN 修改内容` — 修改章节（自动保存旧版本）
- `/novel:review ch-NNN` — 读者视角审阅单章（根据 prompts/reader-review.md 的指令）
- `/novel:review recent N` — 批量审阅最近 N 章
- `/novel:review outline part-XX` — 大纲审阅
- `/novel:review plot` — 剧情框架审阅
- `/novel:review all` — 综合审阅

### 框架迭代
- `/novel:propose 提案内容` — 提出框架变更
- `/novel:accept 提案名 方案` — 确认并应用变更
- `/novel:archive 提案名` — 归档已完成变更

### 维护
- `/novel:audit` — 一致性审计
- `/novel:status` — 查看写作进度

## 核心原则

1. AI 每日创作时**只读旧章节的 summary.md**，不读完整 content.md，避免上下文爆炸
2. 框架变更使用 **propose → accept → archive** 工作流
3. 修改章节时自动分析影响范围，必要时提示创建框架提案
4. 埋点追踪表和一致性审计确保长篇逻辑自洽
"""


def agent_cursor() -> str:
    """Cursor .cursorrules format."""
    return agent_claude_code()  # Same content, different location


def agent_windsurf() -> str:
    """Windsurf .windsurfrules format."""
    return agent_claude_code()  # Same content, different location
