"""Logging utilities for the root agent."""

from __future__ import annotations

import logging
from typing import Optional

from google.adk.tools.tool_context import ToolContext

logger = logging.getLogger(__name__)


def log_caller_name(name: str, tool_context: Optional[ToolContext] = None) -> str:
    """Record the caller name in session state and server logs."""
    cleaned = name.strip()
    if tool_context is not None:
        tool_context.state["caller_name"] = cleaned
    logger.info("Caller name logged: %s", cleaned)
    return f"Logged caller name: {cleaned}"
