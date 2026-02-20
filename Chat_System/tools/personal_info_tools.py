"""Personal information tools."""

from __future__ import annotations

from typing import Optional

from google.adk.tools.tool_context import ToolContext

PERSONAL_DETAILS = {
    "full_name": "Rajat Subhra Bhowmick",
    "email": "sendrajat3060@gmail.com",
    "phone": "7908547953",
    "location": "Kolkata, India",
    "notes": "Update these values in tools/personal_info_tools.py",
}


def get_personal_detail(
    topic: Optional[str] = None,
    tool_context: Optional[ToolContext] = None,
) -> dict:
    """Return personal details, optionally filtered by a topic key."""
    if tool_context is not None:
        tool_context.state["personal_details"] = PERSONAL_DETAILS.copy()

    if not topic:
        return PERSONAL_DETAILS

    key = topic.strip().lower()
    for field, value in PERSONAL_DETAILS.items():
        if field.lower() == key:
            return {field: value}

    return PERSONAL_DETAILS
