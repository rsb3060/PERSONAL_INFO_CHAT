"""Professional information subagent."""

from __future__ import annotations

import os

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.function_tool import FunctionTool

from tools.professional_info_tools import get_professional_detail
from prompts.professional_information_subagent import professional_information_prompt
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")


professional_information_subagent = LlmAgent(
    name="professional_information_subagent",
    description="Handles professional information requests for the caller.",
    model=MODEL_NAME,
    instruction=professional_information_prompt,
    tools=[FunctionTool(get_professional_detail)],
)
