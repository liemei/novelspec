"""Style template files."""


def style_narrative_samples() -> str:
    return """# 叙事风格样本

> 放置你认可的叙事风格参考样本（3-5 段），用于 AI 模仿文风。

## 样本 1

```

```

## 样本 2

```

```

## 样本 3

```

```
"""


def style_forbidden() -> str:
    return """# 禁忌清单

> 明确告诉 AI 不要写什么：禁止的情节、描写、用词、走向等。

- 
- 
- 
"""


def style_conventions() -> str:
    return """# 写作约定

> 统一的写作风格约定。

- 视角：
- 时态：
- 段落长度：
- 对话格式：
- 章节篇幅：
- 其他约定：
"""
