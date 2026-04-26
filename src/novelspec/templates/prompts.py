"""Prompt / agent instruction template files."""


def prompt_daily_write() -> str:
    return """# Daily Write — 每日创作指令

> Agent 在运行 /novel:write 时执行的指令。

## 输入读取（按顺序）

1. 读取 novel.yaml（元信息）
2. 读取 world/（世界观框架）
3. 读取 characters/（人物框架）
4. 读取 style/（风格框架）
5. 读取 plot/overview.md 和对应部/outline（剧情大纲）
6. 读取 state/current-status.md（找到下一章）
7. 读取 state/chapter-log.md（了解当前状态）
8. 读取 state/unresolved-threads.md（未解决线索）
9. 读取最近 5 章的 summary.md（章节概要，不要读完整 content.md）

## 创作步骤

1. **理解上下文**：综合以上输入，理解当前故事进展
2. **检查埋点**：查看 foreshadowing.md，判断是否有需要在本章回收的埋点
3. **生成章节正文**：
   - 严格按照 plot/outline 中该章的大纲写作
   - 匹配 style/conventions.md 中的写作约定
   - 参考 style/narrative-samples.md 模仿文风
   - 人物对话符合 speech-patterns.md 中的说话方式
   - 遵守 style/forbidden.md 中的禁忌清单
   - 遵循 rules/quality-standards.md 中的创作质量准则
4. **更新 summary.md**：写完内容后，生成 300-500 字的章节概要
5. **检查新埋点**：如果本章引入了新的伏笔，更新 foreshadowing.md
6. **更新状态**：更新 state/ 下的所有文件

## 产出物

```
chapters/part-XX/ch-NNN/
├── summary.md        # 章节概要（含 front matter）
└── content.md        # 章节正文（含 front matter）
```

### content.md 的 front matter 格式

```markdown
---
chapter: NNN
title: 章节标题
part: XX
word_count: 字数
pov: 视角人物
written_at: YYYY-MM-DD
status: draft
key_events:
  - 事件1
new_foreshadowing:
  - FS-XXX: 描述
character_appearances:
  - 人物1
---
```

## 注意

- 不要读旧的 content.md 全文，只读 summary.md
- 如果发现框架层文件有矛盾，暂停并通知用户
- 保持每章字数在 novel.yaml 中每日目标字数的 ±20% 范围内
"""


def prompt_revise_chapter() -> str:
    return """# Revise Chapter — 修改章节指令

> Agent 在运行 /novel:revise 时的指令。

## 输入读取

1. 读取用户指定的章节 content.md 和 summary.md
2. 读取所有框架层文件（world/ + characters/ + plot/ + style/）

## 修改流程

**Step 1 — 分析影响范围**：

判断用户修改请求属于哪一类：

| 类别 | 处理方式 |
|------|---------|
| 🔤 仅润色（措辞、错别字、语句通顺） | 直接修改 content.md，不动其他文件 |
| 📖 调整情节（事件顺序、细节增删） | 修改 content.md + 同步更新 summary.md |
| 👤 影响人物设定 | 修改 content.md + 建议更新 characters/ 中对应文件 |
| 🌍 影响世界观/剧情走向 | 提示用户创建 framework/ 提案（/novel:propose） |

**Step 2 — 执行修改**：

- 修改 content.md 前，将当前版本保存到 revisions/ 目录
- 命名格式：`revisions/v{N}-YYYY-MM-DD.md`
- 修改后同步更新 summary.md（如需要）

**Step 3 — 输出影响报告**：

```
✓ 已修改 ch-NNN/content.md
✓ 旧版本已保存至 revisions/v{N}-YYYY-MM-DD.md
✓ 已更新 summary.md

【影响分析】
✅ 未影响框架层
⚠️ 注意：这个修改可能影响 ch-NNN+1 的剧情走向
```
"""


def prompt_audit_consistency() -> str:
    return """# Audit Consistency — 一致性审计指令

> Agent 在运行 /novel:audit 时的指令。

## 检查项

### 1. 人物一致性
- 扫描所有已写章节的 summary.md
- 检查人物性格、背景、能力是否前后一致
- 检查人物名字拼写是否统一

### 2. 时间线一致性
- 检查所有章节中的时间引用是否矛盾
- 检查 world/timeline.md 中的事件是否与故事内容冲突

### 3. 专有名词一致性
- 检查所有已写章节中的专有名词使用是否与 glossary.md 一致

### 4. 埋点回收检查
- 检查 foreshadowing.md 中状态为"待回收"的埋点
- 如果某埋点的"计划回收章节" ≤ 当前已写章节数，标记为 ⏰ 已过期

### 5. 未登记埋点检测
- 扫描已写章节 summary.md
- 发现可能构成伏笔的内容但未在 foreshadowing.md 中登记 → 建议补充

## 输出格式

```
📋 NovelSpec 一致性审计报告

✅ [领域] — 状态摘要

⚠️ 埋点检查
┌──────┬──────────┬──────────┬────────┐
│ ID   │ 描述     │ 计划回收 │ 状态   │
├──────┼──────────┼──────────┼────────┤
│      │          │          │        │
└──────┴──────────┴──────────┴────────┘

⚡ 建议事项
- 
```
"""


def prompt_worldbuild() -> str:
    return """# Worldbuild — 世界观框架生成指令

> Agent 在运行 /novel:worldbuild 时的指令。

## 工作流

### 用户提供素材后

按依赖关系逐项生成：

```
world/background.md
  → world/timeline.md
  → world/glossary.md
  → characters/profiles/（主要人物）
  → characters/relationships.md
  → characters/speech-patterns.md
  → plot/overview.md（总纲）
  → plot/parts/（各部梗概）
  → plot/foreshadowing.md（初始埋点设计）
  → style/（文风、禁忌、约定）
```

### 生成原则

1. 每次生成一个文件，展示给用户确认后再继续下一个
2. 依赖尚未确认的文件时，基于当前最佳理解先行生成
3. 用户确认后标记该文件为 ✅ 已确认
4. 如果用户想修改已确认的文件，使用 /novel:propose

### 二次调用（已有框架后再次运行）

- 读取现有框架文件
- 展示当前框架结构
- 询问用户想修改哪部分
- 生成修改影响分析
- 用户确认后更新

## 输出风格

- 纯简体中文
- 文件内容使用 Markdown
- 人物卡应包含：外貌、性格、背景故事、动机、成长弧
- 世界观应包含足够的可扩展空间
"""


def prompt_outline() -> str:
    return """# Outline — 章节大纲创作指令

> Agent 在运行 /novel:outline 时的指令。

## 输入

1. 读取 novel.yaml（总章数规划）
2. 读取 plot/overview.md（总纲）
3. 读取 plot/parts/ 中对应部的概梗
4. 读取 characters/（了解出场人物范围）

## 产出

创建 `plot/outlines/part-XX-outline.md`

### 大纲条目格式

```markdown
## 第 N 章（ch-NNN）
**暂定标题**: 
**视角**: 
**核心事件**:
- 
**埋点**: 
- 
**目标字数**: 2000-2500
**出场人物**: 
- 
```

## 注意

- 严格遵循 plot/parts/ 中的故事梗概
- 每章埋下 0-2 个新埋点，定期回收旧埋点
- 各章之间要有节奏感：张弛交替
- 确保人物出场合理
"""


def prompt_propose_framework() -> str:
    return """# Propose Framework Change — 框架变更提案指令

> Agent 在运行 /novel:propose 时的指令。

## 工作流

1. 读取当前框架文件（world/ + characters/ + plot/ + style/）
2. 读取已写章节的 summary.md（评估影响范围）
3. 在 framework/ 下创建提案目录
4. 生成 proposal.md

### proposal.md 模板

```markdown
# 提案：〈标题〉

## 为什么改
（为什么需要这个变更）

## 改什么
- （列出要修改的具体文件）

## 影响范围
- 框架文件：（哪些框架文件受影响）
- 已写章节：（哪些章节可能需要调整）
- 后续大纲：（哪些后续章节大纲需要调整）

## 备选方案
A. （方案 A）
B. （方案 B）
```

## 原则

- 只生成提案，不执行修改
- 清晰地标注影响范围，让用户判断是否值得改
- 提供至少 2 个备选方案（如果有余地的线）
"""
