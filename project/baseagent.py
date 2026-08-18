import json
import re

DF_ALIASES = {'dataframe', 'df', 'data', 'dataset'}

def _snake(s):
    return re.sub(r'([A-Z])', r'_\1', s).lower().lstrip('_')

class BaseAgent:

    def __init__(self, name, description, tools, llm):
        self.name = name
        self.description = description
        self.tools = tools
        self.llm = llm

    def execute(self, task, state):
        llm_response = self.ask_llm(task, state)
        tool_name = llm_response["tool"]
        arguments = llm_response.get("arguments", {}) or {}
        arguments = {_snake(k): v for k, v in arguments.items()}
        results = state.get("results") or {}
        if tool_name != "load_csv":
            for agent_name, agent_result in results.items():
                if hasattr(agent_result, 'head'):
                    arguments['dataframe'] = agent_result
                    break
        tool = self.tools[tool_name]
        result = tool(**arguments)
        return result

    def ask_llm(self, task, state):
        results = state.get("results") or {}
        context = ""
        for agent_name, agent_result in results.items():
            if hasattr(agent_result, 'head'):
                context += f"Previous result from {agent_name}: a DataFrame with {len(agent_result)} rows and columns {list(agent_result.columns)}\n"
            else:
                context += f"Previous result from {agent_name}: {str(agent_result)[:200]}\n"
        tools_list = list(self.tools.keys())
        prompt = f"""You are an agent. Based on the task and previous results, choose a tool and arguments.
Available tools: {tools_list}

Previous context:
{context}

Task: {task}

Return ONLY valid JSON (no markdown, no code fences) with format:
{{"tool": "<tool_name>", "arguments": {{"key": "value"}}}}
"""
        response = self.llm.invoke(prompt)
        match = re.search(r'\{.*\}', response, re.DOTALL)
        if match:
            response = match.group()
        return json.loads(response)
