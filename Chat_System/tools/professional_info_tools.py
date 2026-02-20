"""Professional information tools."""

from __future__ import annotations

from typing import Optional

from google.adk.tools.tool_context import ToolContext

PROFESSIONAL_DETAILS = {
    "current_title": "Senior Data Scientist",
    "current_company": "EXL",
    "skills": "List your key skills here",
    "experience": "Brief summary of your experience",
    "notes": "Update these values in tools/professional_info_tools.py",
}


def get_professional_detail(
    topic: Optional[str] = None,
    tool_context: Optional[ToolContext] = None,
) -> dict:
    """Return professional details, optionally filtered by a topic key."""
    if tool_context is not None:
        tool_context.state["professional_details"] = PROFESSIONAL_DETAILS.copy()

    if not topic:
        return PROFESSIONAL_DETAILS

    key = topic.strip().lower()
    for field, value in PROFESSIONAL_DETAILS.items():
        if field.lower() == key:
            return {field: value}

    return PROFESSIONAL_DETAILS
