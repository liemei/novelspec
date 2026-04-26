"""
Template content functions for NovelSpec project scaffolding.
Each function returns the markdown content for a specific file.
"""
# flake8: noqa: E501

from novelspec.templates.config import novel_yaml, meta_changelog
from novelspec.templates.world import world_background, world_timeline, world_glossary
from novelspec.templates.characters import (
    characters_relationships,
    characters_speech_patterns,
)
from novelspec.templates.plot import plot_overview, plot_foreshadowing
from novelspec.templates.style import (
    style_narrative_samples,
    style_forbidden,
    style_conventions,
)
from novelspec.templates.state import (
    state_current_status,
    state_chapter_log,
    state_unresolved_threads,
)
from novelspec.templates.prompts import (
    prompt_daily_write,
    prompt_revise_chapter,
    prompt_audit_consistency,
    prompt_worldbuild,
    prompt_outline,
    prompt_propose_framework,
)
from novelspec.templates.agents import agent_claude_code

__all__ = [
    "novel_yaml",
    "meta_changelog",
    "world_background",
    "world_timeline",
    "world_glossary",
    "characters_relationships",
    "characters_speech_patterns",
    "plot_overview",
    "plot_foreshadowing",
    "style_narrative_samples",
    "style_forbidden",
    "style_conventions",
    "state_current_status",
    "state_chapter_log",
    "state_unresolved_threads",
    "prompt_daily_write",
    "prompt_revise_chapter",
    "prompt_audit_consistency",
    "prompt_worldbuild",
    "prompt_outline",
    "prompt_propose_framework",
    "agent_claude_code",
]
