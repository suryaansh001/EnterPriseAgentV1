from baseagent import BaseAgent
from tools.analytics_tools import calculate_mean, calculate_sum, correlation_matrix, t_test, z_score
class AnalyticsAgent(BaseAgent):

    def __init__(self, llm):

        tools = {

            "mean": calculate_mean,

            "sum": calculate_sum,

            "correlation": correlation_matrix,

            "t_test": t_test,

            "z_score": z_score

        }

        super().__init__(

            name="Analytics Agent",

            description="Performs statistical analysis.",

            tools=tools,

            llm=llm

        )