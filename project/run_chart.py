from llm.groq_client import GroqClient
from agents.chart import ChartAgent
from tools.database_tools import load_csv
df = load_csv(file_path="data/titanic.csv")
