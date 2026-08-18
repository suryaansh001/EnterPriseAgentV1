class DatabaseAgent:
    def __init__(self):
        self.name = "DatabaseAgent"
        self.description = "Handles database queries and data retrieval."

    def execute(self, task):

        if task == "fetch_pending_invoices":

            query = """
            SELECT *
            FROM invoices
            WHERE status='pending'
            """

            return execute_sql(query)

        elif task == "fetch_all_clients":

            query = """
            SELECT *
            FROM clients
            """

        return execute_sql(query)


class AnalyticsAgent:
    def __init__(self):
        self.name = "AnalyticsAgent"
        self.description = "Performs data analysis and generates analytics ."
    def execute(self,task,dataframe):
        if task == "analyze_data":
            run_code="""import pandas as pd ....."""
            analytics  = analyze_data(dataframe)
            return analytics 
        elif task == "gcalculate_average_delay":
            analytics = (dataframe)
            return analytics
        
class ChartAgent:
    def __init__(self):
        self.name = "ChartAgent"
        self.description = "Creates visualizations such as graphs and charts."

    def execute(self, task, dataframe):
        if task == "create_bar_chart":
            chart = create_bar_chart(dataframe)
            return chart
        elif task == "create_line_chart":
            chart = create_line_chart(dataframe)
            return chart
class WriterAgent:
    def __init__(self):
        self.name = "WriterAgent"
        self.description = "Generates written content based on data and analysis."
        

AGENTS = {

    "database":DatabaseAgent(),

    "analytics":AnalyticsAgent(),

    "chart":ChartAgent(),

    "writer":WriterAgent()

}



#step 1  : 
user_prompt = input("Please enter your request: ")
def planner(AGENTS : dict, user_prompt : str)->list:
    execution_plan = []
    if "database" in user_prompt.lower():
        execution_plan.append(AGENTS["database"])
    if "analytics" in user_prompt.lower():
        execution_plan.append(AGENTS["analytics"])
    if "chart" in user_prompt.lower():
        execution_plan.append(AGENTS["chart"])
    if "writer" in user_prompt.lower():
        execution_plan.append(AGENTS["writer"])
    return execution_plan

state = {

    "user_prompt":"",

    "execution_plan":[],

    "results":{

        "database":None,

        "analytics":None,

        "charts":None,

        "report":None

    },

    "logs":[]

}
def orchestrator(execution_plan : list,AGENTS : dict):
    #this will execute the agents in the order they were added to the execution plan and save things in state 
    for agent in execution_plan:
        if isinstance(agent, DatabaseAgent):
            print(f"Executing {agent.name}: {agent.description}")
            state["results"]["database"] = agent.execute(DatabaseAgent)
            # Call the database agent's function here
        elif isinstance(agent, AnalyticsAgent):
            print(f"Executing {agent.name}: {agent.description}")
            state["results"]["analytics"] = agent.execute(AnalyticsAgent)
            # Call the analytics agent's function here
        elif isinstance(agent, ChartAgent):
            print(f"Executing {agent.name}: {agent.description}")
            state["results"]["charts"] = agent.execute(ChartAgent)
            # Call the chart agent's function here
        elif isinstance(agent, WriterAgent):
            print(f"Executing {agent.name}: {agent.description}")
            state["results"]["report"] = agent.execute(WriterAgent)
            # Call the writer agent's function here

   