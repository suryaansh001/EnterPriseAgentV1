#!/usr/bin/env python3
"""
Script to download the Titanic dataset and use the orchestrator to analyze it.
"""

import os
import requests
import pandas as pd
from pathlib import Path

# Ensure data directory exists
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

TITANIC_URL = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
TITANIC_PATH = DATA_DIR / "titanic.csv"

def download_titanic():
    if TITANIC_PATH.exists():
        print(f"Titanic dataset already exists at {TITANIC_PATH}")
        return
    print(f"Downloading Titanic dataset from {TITANIC_URL}...")
    try:
        response = requests.get(TITANIC_URL, timeout=10)
        response.raise_for_status()
        with open(TITANIC_PATH, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded and saved to {TITANIC_PATH}")
    except Exception as e:
        print(f"Failed to download: {e}")
        # Fallback to a local copy if exists? Not needed.
        raise

def main():
    # Download dataset
    download_titanic()

    # Import orchestrator components
    from llm.groq_client import GroqClient
    from planner import Planner
    from orchestrator import Orchestrator
    from state import State
    from registry import get_agents

    # Initialize LLM
    llm = GroqClient()
    state = State()
    planner = Planner(llm)
    agents = get_agents(llm)
    orchestrator = Orchestrator(planner=planner, agents=agents, state=state)

    # Example prompt: load the CSV and show first few rows
    user_prompt = f"""
    Load the CSV file located at '{TITANIC_PATH}' into a DataFrame.
    Then show the first 5 rows
    """
    print("\n--- Running orchestrator with prompt ---")
    print(user_prompt)
    result = orchestrator.run(user_prompt)

    print("\n--- Result ---")
    print(result)

    # Additional example: calculate average age
    user_prompt2 = f"""
    Load the CSV file located at '{TITANIC_PATH}' into a DataFrame.
    Then calculate the average age of passengers.
    """
    print("\n--- Running second prompt ---")
    print(user_prompt2)
    result2 = orchestrator.run(user_prompt2)
    print("\n--- Result ---")
    print(result2)

    # Chart example: histogram of ages
    user_prompt3 = f"""
    Load the CSV file located at '{TITANIC_PATH}' into a DataFrame.
    Then create a histogram of passenger ages.
    """
    print("\n--- Running chart prompt ---")
    print(user_prompt3)
    result3 = orchestrator.run(user_prompt3)
    print("--- Chart Result ---")
    print(result3)

if __name__ == "__main__":
    main()
