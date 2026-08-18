# Orchestration Project

This project contains a small multi-agent orchestration workflow for data analysis and chart generation.

## Overview

The codebase includes:

- agent orchestration and planning logic
- tool integrations for analytics and charting
- database and LLM client support
- example runs for datasets such as Titanic

## Project Structure

```text
project/
├── agents/
├── charts/
├── data/
├── llm/
├── tools/
├── utils/
├── baseagent.py
├── main.py
├── orchestrator.py
├── planner.py
├── registry.py
├── state.py
├── run_chart.py
├── run_titanic.py
├── runtit2.py
├── fix.py
└── .env
```

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

If a requirements file is not present yet, install the packages needed for the project manually.

3. Configure environment variables:

Create a `.env` file with the required API keys and settings used by the project.

## Running the Project

From the project directory:

```bash
python main.py
```

You can also run the example scripts:

```bash
python run_titanic.py
python run_chart.py
```

## Notes

- Keep secrets out of version control.
- Use `.env` for local configuration.
- Prefer virtual environments for dependency isolation.

## License

This project is provided as-is for learning and experimentation.
