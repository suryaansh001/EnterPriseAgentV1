class Orchestrator:

    def __init__(self, planner, agents, state):

        self.planner = planner
        self.agents = agents
        self.state = state

    def run(self, user_prompt):

        # Save user prompt
        self.state.set(
            "user_prompt",
            user_prompt
        )

        # Ask planner for execution plan
        plan = self.planner.plan(
            user_prompt,
            self.agents
        )

        # Store execution plan
        self.state.set(
            "execution_plan",
            plan
        )

        # Execute each step
        for step in plan:

            agent_name = step["agent"]

            task = step["task"]

            agent = self.agents[agent_name]

            result = agent.execute(
                task=task,
                state=self.state
            )

            self.state.add_result(
                agent_name,
                result
            )

        return self.state.data