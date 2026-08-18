import json
import re

class Planner:

    def __init__(self, llm):
        self.llm = llm

    def plan(self, user_prompt, agents):
        plan = self.llm.generate_plan(user_prompt, agents)
        match = re.search(r"\{.*\}", plan, re.DOTALL)
        if match:
            plan = match.group()
        parsed = json.loads(plan)
        if "subtasks" in parsed:
            parsed = parsed["subtasks"]
        steps = []
        for item in parsed:
            agent = item.get("agent") or item.get("tool", "database")
            task = item.get("task", "")
            params = item.get("parameters", {})
            if params:
                task = task + " with parameters: " + json.dumps(params)
            steps.append({"agent": agent, "task": task})
        return steps
