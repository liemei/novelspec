# NovelSpec

**Spec-driven long-form novel creation for AI coding assistants.**

Inspired by [OpenSpec](https://github.com/Fission-AI/OpenSpec) (spec-driven development for AI coding), NovelSpec brings the same philosophy to storytelling:

> **Agree on the world before you write a single word.**

[简体中文版](README.zh-CN.md)

## Philosophy

```text
→ spec-first not improv-first
→ iterative not waterfall
→ structured enough to keep AI consistent
→ flexible enough to change your mind
→ scalable from short stories to epic sagas
```

## How It Works

```
                        NovelSpec Workflow

╔══════════════════════════════════════════════════════╗
║               SETUP PHASE                            ║
║                                                       ║
║   /novel:init → /novel:worldbuild → /novel:outline    ║
║        │               │                  │           ║
║        │        (iterate)          (batch per part)   ║
╚════════╪═══════════════╪══════════════════╪═══════════╝
         │               │                  │
         ▼               ▼                  ▼
╔══════════════════════════════════════════════════════╗
║              WRITING PHASE                           ║
║                                                       ║
║   /novel:write → /novel:review → /novel:revise       ║
║        │              │                │             ║
║        │         (reader review)   (fix issues)       ║
║        │              └── re-review after fix ───────╡
║        │                                            │
║        └──────────→ continue to next chapter ───────╡
╚══════════════════════════════════════════════════════╝
         │               │                  │
         ▼               ▼                  ▼
╔══════════════════════════════════════════════════════╗
║              EVOLUTION PHASE                         ║
║                                                       ║
║   /novel:propose → discuss → /novel:accept → archive  ║
║                                                       ║
║   /novel:audit (weekly or on demand)                  ║
║                                                       ║
╚══════════════════════════════════════════════════════╝
```

## Quick Start

```bash
# Install
pip install novelspec

# Create a new novel project
novelspec init my-novel
cd my-novel

# In your AI assistant (Claude Code, Cursor, Windsurf...):
# /novel:worldbuild  →  describe your story materials
# /novel:outline part-01  →  create chapter outlines
# /novel:write       →  start writing chapters
```

## Reader Review System (v1.2.0+)

After writing a chapter or creating an outline, NovelSpec can review your work from a **reader's perspective** — catching logical flaws, character IQ issues, pacing problems, and emotional disconnects before you move on.

### Six-Dimension Review

| Dimension | What It Checks |
|-----------|---------------|
| 🧠 Reasonableness | Does the character act according to their personality and situation? Are cause-and-effect chains logical? |
| 🎯 Character IQ | Any "plot-induced stupidity"? Do decisions match the character's intelligence level? |
| 📖 Storyline Consistency | Does this chapter align with the plot direction? Is the pacing right for the current story phase? |
| 💔 Emotional Resonance | Will the reader actually feel something? Or is it forced drama? |
| 📄 Reading Experience | Does the chapter have a hook at the end? Any skippable passages? Info density right? |
| 🗣️ Dialogue & Behavior | Would this person really say/do this in this situation? |

### Review Commands

| Command | What It Does |
|---------|-------------|
| `/novel:review ch-NNN` | Review a single chapter |
| `/novel:review recent N` | Batch review last N chapters |
| `/novel:review outline part-XX` | Review a part's outline before writing |
| `/novel:review plot` | Review the overall plot framework |
| `/novel:review all` | Comprehensive review of everything |

### Review → Revise → Re-review Loop

```
/novel:review ch-003   →  Report: 2 critical issues found
/novel:revise ch-003   →  Fix: adjust character decision
/novel:review ch-003   →  Confirm: both issues resolved ✓
```

Review reports are saved to `chapters/part-XX/ch-NNN/reviews/` for future reference.

## Project Structure

```
my-novel/
├── novel.yaml                      # Metadata
├── world/                          # World-building
├── characters/                     # Character profiles
├── plot/                           # Plot, outlines, foreshadowing
├── style/                          # Narrative style guide
├── rules/                          # Quality standards
├── prompts/                        # Agent working instructions
│   └── reader-review.md            # Reader review instructions
├── state/                          # Writing progress tracker
├── chapters/                       # Chapter drafts
│   └── part-XX/ch-NNN/
│       ├── summary.md              # Chapter summary
│       ├── content.md              # Full chapter text
│       ├── revisions/              # Version history
│       └── reviews/                # Reader review reports
├── framework/                      # Framework change proposals
└── meta/                           # Changelog
```

## Slash Commands

| Command | Purpose | Auto-Review |
|---------|---------|-------------|
| `/novel:init` | Initialize a new novel project | — |
| `/novel:worldbuild` | Generate world framework from your materials | — |
| `/novel:outline` | Create chapter outlines per part | ✅ suggests review |
| `/novel:write` | Write the next chapter | ✅ suggests review |
| `/novel:show` | Read written content | — |
| `/novel:revise` | Revise a chapter (auto-saves history) | — |
| `/novel:review` | Review from reader's perspective (5 modes) | ★ core feature |
| `/novel:propose` | Propose a framework change | — |
| `/novel:accept` | Accept and apply a framework change | — |
| `/novel:archive` | Archive completed proposals | — |
| `/novel:audit` | Consistency audit (foreshadowing, timeline) | — |
| `/novel:status` | Show writing progress | — |

## Three-Level Storage

- **L1 - Framework layer** (world/ + characters/ + plot/ + style/): Stable, rarely changes
- **L2 - State layer** (state/): Updates daily, compact
- **L3 - Output layer** (chapters/): Full drafts, only `summary.md` referenced for context

This prevents context window explosion in long novels.

## License

MIT
