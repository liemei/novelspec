# NovelSpec

**Spec-driven long-form novel creation for AI coding assistants.**

Inspired by [OpenSpec](https://github.com/Fission-AI/OpenSpec) (spec-driven development for AI coding), NovelSpec brings the same philosophy to storytelling:

> **Agree on the world before you write a single word.**

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
║   /novel:write → review → /novel:revise → continue    ║
║                                                       ║
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

## Project Structure

```
my-novel/
├── novel.yaml                      # Metadata
├── world/                          # World-building
├── characters/                     # Character profiles
├── plot/                           # Plot, outlines, foreshadowing
├── style/                          # Narrative style guide
├── prompts/                        # Agent working instructions
├── state/                          # Writing progress tracker
├── chapters/                       # Chapter drafts
├── framework/                      # Framework change proposals
└── meta/                           # Changelog
```

## Slash Commands

| Command | Purpose |
|---------|---------|
| `/novel:init` | Initialize a new novel project |
| `/novel:worldbuild` | Generate world framework from your materials |
| `/novel:outline` | Create chapter outlines per part |
| `/novel:write` | Write the next chapter |
| `/novel:show` | Read written content |
| `/novel:revise` | Revise a chapter (auto-saves history) |
| `/novel:propose` | Propose a framework change |
| `/novel:accept` | Accept and apply a framework change |
| `/novel:archive` | Archive completed proposals |
| `/novel:audit` | Consistency audit |
| `/novel:status` | Show writing progress |

## Three-Level Storage

- **L1 - Framework layer** (world/ + characters/ + plot/ + style/): Stable, rarely changes
- **L2 - State layer** (state/): Updates daily, compact
- **L3 - Output layer** (chapters/): Full drafts, only `summary.md` referenced for context

This prevents context window explosion in long novels.

## License

MIT
