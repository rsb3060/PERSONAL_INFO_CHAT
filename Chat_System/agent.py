"""Root agent entrypoint for Chat_System."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from a .env file (if using one)
load_dotenv()





from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.function_tool import FunctionTool
from google.adk.models.lite_llm import LiteLlm

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

current_model= 'gemini'
if current_model== 'gemini':
    MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")
else:
    MODEL_NAME = LiteLlm(
    model="groq/llama-3.3-70b-versatile")

def initialize_session_state(
    callback_context: CallbackContext, **_: object
) -> None:
    for key, value in default_state.items():
        if key not in callback_context.state:
            callback_context.state[key] = value




# Initialize the LiteLlm model with the specific Groq model name
# The format is "groq/<groq-model-name>", e.g., "groq/llama-3.3-70b-versatile"




root_agent = LlmAgent(
    name="root_agent",
    description="Root assistant that greets the caller and routes requests.",
    model=MODEL_NAME,
    instruction=orchestrator_prompt,
    tools=[FunctionTool(log_caller_name)],
    before_agent_callback=initialize_session_state,
    sub_agents=[personal_information_subagent, professional_information_subagent],
)
