"""Root agent entrypoint for Chat_System."""

from __future__ import annotations

import os
import sys
from pathlib import Path

from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.function_tool import FunctionTool

AGENT_DIR = Path(__file__).resolve().parent
if str(AGENT_DIR) not in sys.path:
    sys.path.insert(0, str(AGENT_DIR))

from subagent.personal_information_subagent import personal_information_subagent
from subagent.professional_information_subagent import (
    professional_information_subagent,
)
from tools.logging_tools import log_caller_name
from Chat_System.prompts.orchestrator_agent import orchestrator_prompt
from helper.state import default_state
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

def initialize_session_state(
    callback_context: CallbackContext, **_: object
) -> None:
    for key, value in default_state.items():
        if key not in callback_context.state:
            callback_context.state[key] = value


root_agent = LlmAgent(
    name="root_agent",
    description="Root assistant that greets the caller and routes requests.",
    model=MODEL_NAME,
    instruction=orchestrator_prompt,
    tools=[FunctionTool(log_caller_name)],
    before_agent_callback=initialize_session_state,
    sub_agents=[personal_information_subagent, professional_information_subagent],
)
