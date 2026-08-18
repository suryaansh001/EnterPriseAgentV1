from baseagent import BaseAgent
from tools.database_tools import load_csv, select_columns, filter_rows, show_head

class DatabaseAgent(BaseAgent):

    def __init__(self, llm):

        tools = {

            "load_csv": load_csv,

            "select_columns": select_columns,

            "filter_rows": filter_rows,

            "show_head": show_head

        }

        super().__init__(

            name="Database Agent",

            description="Handles data loading and manipulation.",

            tools=tools,

            llm=llm

        )