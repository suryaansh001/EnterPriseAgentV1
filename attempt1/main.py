def decide_next_agent(user_prompt:str,agent_lists:dict)->json : 
    # system_prompt="Based on the user prompt, determine which agent from the provided list is best suited to handle the request. Consider the expertise and capabilities of each agent in relation to the user's needs.The list and functions of the aggents are as follows: " + str(agent_lists) + ". Please provide your recommendation in JSON format, specifying the selected agent and a brief justification for your choice."
    # responseOfLLM=llm_response(system_prompt + " User prompt: " + user_prompt)
    # return responseOfLLM
    sequneceOfAgents = []
    if "graphs" in user_prompt.lower() or "charts" in user_prompt.lower():
        sequneceOfAgents.append({"selected_agent": "DataVisualizationAgent", "justification": "The user prompt mentions graphs or charts, indicating a need for data visualization expertise."})
        return {"selected_agent": "DataVisualizationAgent", "justification": "The user prompt mentions graphs or charts, indicating a need for data visualization expertise."}
    #creating graphs and charts based on the data provided by the user or fetched from database

    
    if "find" in user_prompt.lower() or "data" in user_prompt.lower() or "invoice" in user_prompt.lower() or "pending" in user_prompt.lower() or "database" in user_prompt.lower():
        sequneceOfAgents.append({"selected_agent": "DataRetrievalAgent", "justification": "The user prompt suggests a need for data retrieval or database access, which aligns with the capabilities of the DataRetrievalAgent."})
        return {"selected_agent": "DataRetrievalAgent", "justification": "The user prompt suggests a need for data retrieval or database access, which aligns with the capabilities of the DataRetrievalAgent."}
        #for fetching sql queries and data from database



    if "analyze" in user_prompt.lower() or "insights" in user_prompt.lower() or "trends" in user_prompt.lower():
        sequneceOfAgents.append({"selected_agent": "DataAnalysisAgent", "justification": "The user prompt indicates a need for data analysis or insights, which is best handled by the DataAnalysisAgent."})
        return {"selected_agent": "DataAnalysisAgent", "justification": "The user prompt indicates a need for data analysis or insights, which is best handled by the DataAnalysisAgent."}
    #for calculating things like average percentage, correlation   etc .and then providing insights and trends based on the data
    




#defining the state of the session in which the memory of this sesion will be stored and the user prompt will be processed and the next agent will be decided based on the user prompt and the state of the session

state = {}
def  data_analysis_agent(user_prompt:str, state:dict):
    # This function will handle data analysis tasks based on the user prompt and provided data.
    # Implement the logic for analyzing the data and generating insights.
    pass
def dataRetrievalAgent(user_prompt:str, database_connection, sql_tables:list)->dict:
    dataframe = await sql ('SELECT * FROM invoices WHERE status = 'pending';')
    state["pending_invoice_data"] = dataframe
    return dataframe
    #something like that only the tables will be given to llm andit will run the query and fetch the data from the database and return it to the user in json format
def dataVisualizationAgent(user_prompt:str, dataframe:dict),state:dict ->json:
    #here dome running pf python code 
    


