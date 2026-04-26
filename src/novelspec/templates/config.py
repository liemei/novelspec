"""novel.yaml and metadata templates."""


def novel_yaml() -> str:
    return """# NovelSpec 小说元信息
书名: 未命名
类型:           # 玄幻 / 科幻 / 历史 / 言情 / 悬疑 / ...
基调:           # 热血、成长、黑暗、治愈、幽默 ...
目标总字数: 300000
每日目标字数: 2000
默认语言: zh-CN

# 创作参数
模型:           # 推荐使用 deepseek-v4-flash / claude-sonnet-4 等
写作时间: "08:00"
交付平台:       # weixin / telegram / local ...
总章数规划: 60
总部数规划: 3

# 框架版本
novelspec_version: 1.0
"""


def meta_changelog() -> str:
    return """# 框架变更日志

| 日期 | 变更内容 | 提案路径 |
|------|---------|---------|
|      |         |         |

格式：
| YYYY-MM-DD | 修改了什么（如：调整世界观时间线） | framework/<提案名>/ |
"""
