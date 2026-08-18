
from baseagent import BaseAgent
from tools.chart_tools import generate_line_chart, generate_bar_chart, generate_pie_chart, generate_scatter_plot, generate_histogram



class ChartAgent(BaseAgent):

    def __init__(self, llm):

        tools = {

            "line_chart": generate_line_chart,

            "bar_chart": generate_bar_chart,

            "pie_chart": generate_pie_chart,

            "scatter_plot": generate_scatter_plot,

            "histogram": generate_histogram

        }

        super().__init__(

            name="Chart Agent",

            description="Generates charts and visualizations.",

            tools=tools,

            llm=llm

        )
