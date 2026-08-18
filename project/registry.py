from agents.database import DatabaseAgent
from agents.analytics import AnalyticsAgent
from agents.chart import ChartAgent

# Agent information: class and description
AGENT_INFO = {
    "database": {"class": DatabaseAgent, "description": "Handles data loading and manipulation."},
    "analytics": {"class": AnalyticsAgent, "description": "Performs statistical analysis."},
    "chart": {"class": ChartAgent, "description": "Generates charts and visualizations."}
}

def get_agents(llm):
    """
    Instantiate agent objects with the given LLM.
    Returns a dict mapping agent name to agent instance.
    """
    agents = {}
    for name, info in AGENT_INFO.items():
        agents[name] = info["class"](llm)
    return agents

# Tool definitions (kept for reference if needed elsewhere)
ANALYTICS_TOOLS = {
    "mean": {"function": "calculate_mean","description": "Calculate the mean of a dataset."},
    "sum": {"function": "calculate_sum","description": "Calculate the sum of a dataset."},
    "correlation": {"function": "correlation_matrix","description": "Calculate the correlation matrix of a dataset."},
    "t_test": {"function": "t_test","description": "Perform a t-test on two datasets."},
    "z_score": {"function": "z_score","description": "Calculate the z-scores of a dataset."}
}

CHART_TOOLS = {
    "line_chart": {"function": "generate_line_chart","description": "Generate a line chart."},
    "bar_chart": {"function": "generate_bar_chart","description": "Generate a bar chart."},
    "pie_chart": {"function": "generate_pie_chart","description": "Generate a pie chart."}
}

DATABASE_TOOLS = {
    "load_csv": {
        "function": "load_csv",
        "description": "Load the sales CSV into a pandas DataFrame."
    },
    "select_columns": {
        "function": "select_columns",
        "description": "Select specific columns from a DataFrame."
    },
    "filter_rows": {
        "function": "filter_rows",
        "description": "Filter rows based on conditionstakes condition as input."
    }
}