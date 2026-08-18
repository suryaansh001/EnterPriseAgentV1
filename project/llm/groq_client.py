import os
import json

from dotenv import load_dotenv
from groq import Groq
from llm.prompts import planner_prompt


load_dotenv()  # Load environment variables from .env file

class GroqClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key)
        self.model = "llama-3.3-70b-versatile"

    def invoke(self, prompt):
        """
        Sends prompt to Groq.
        Returns JSON.
        """
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=self.model,
        )

        return chat_completion.choices[0].message.content

    def generate_plan(self, user_prompt, agents):
        """
        Generate a plan for the user_prompt given the available agents.
        Returns a list of steps in JSON format.
        """
        # Build tools description from agents dict (agent name -> agent object)
        tools_desc = "\n".join([f"- {name}: {agent.description}" for name, agent in agents.items()])
        prompt = planner_prompt().format(tools=tools_desc, task=user_prompt)
        response = self.invoke(prompt)
        # The response should be a JSON list of steps
        return response

