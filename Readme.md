# Personal Info Chat (Google ADK)

This repo contains two ADK agents:
- `Chat_System`: A multi-agent assistant that greets callers, logs caller name, initializes session state, and routes requests to personal/professional subagents.
- `sample_agent/my_agent`: A simple example agent that uses a `get_current_time` tool.

**Agents**

`Chat_System`
- Root agent greets the caller, asks for name if missing, logs it, and routes requests.
- Subagent `personal_information_subagent` uses `get_personal_detail`.
- Subagent `professional_information_subagent` uses `get_professional_detail`.
- Prompts live in `Chat_System/prompts/*.py`.
- Tools live in `Chat_System/tools/*.py`.
- Session defaults live in `Chat_System/helper/state.py` and are initialized on new sessions.

`sample_agent/my_agent`
- Single root agent that answers “current time in a city” using a mock tool.

**Run Locally**

1. Activate the venv: `source adk_env/bin/activate`
2. Set environment variables (or edit `.env` in each agent folder): `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION`, optional `GEMINI_MODEL` (defaults to `gemini-2.5-flash-lite`).
3. Start ADK Web UI for `Chat_System`: `adk web /home/rajat/GIT_PROJECTS/PERSONAL_INFO_CHAT` and select `Chat_System` in the UI.
4. Start ADK Web UI for the sample agent: `adk web /home/rajat/GIT_PROJECTS/PERSONAL_INFO_CHAT/sample_agent` and select `my_agent` in the UI.

**Notes**
- If you rename folders, update the `adk web` path accordingly.
- The tools currently return static data; update them to integrate with your data sources.
