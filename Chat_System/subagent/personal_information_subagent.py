"""Personal information subagent."""

from __future__ import annotations

import os

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.function_tool import FunctionTool

from tools.personal_info_tools import get_personal_detail
from prompts.personal_information_subagent import personal_information_prompt
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")


personal_information_subagent = LlmAgent(
    name="personal_information_subagent",
    description="Handles personal information requests for the caller.",
    model=MODEL_NAME,
    instruction=personal_information_prompt,
    tools=[FunctionTool(get_personal_detail)],
)
