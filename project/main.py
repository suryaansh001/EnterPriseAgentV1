from llm.groq_client import GroqClient

from planner import Planner
from orchestrator import Orchestrator
from state import State

from registry import get_agents


def main():

    llm = GroqClient()

    state = State()

    planner = Planner(llm)

    agents = get_agents(llm)

    orchestrator = Orchestrator(
        planner=planner,
        agents=agents,
        state=state
    )

    user_prompt = input("Enter your prompt: ")

    result = orchestrator.run(user_prompt)

    print("\nFinal State\n")

    print(result)


if __name__ == "__main__":
    main()