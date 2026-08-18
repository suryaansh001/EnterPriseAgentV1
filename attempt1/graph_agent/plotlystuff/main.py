import plotly.express as px
import pandas as pd

# Load sample dataset
df = px.data.iris()

# Create scatter plot
fig = px.scatter(
    df, 
    x="sepal_width", 
    y="sepal_length", 
    color="species",               # Color points by categorical group
    size="petal_length",           # Change dot size based on numerical column
    title="Flower Sepal Width vs. Length"
)

fig.show()

df_tips = px.data.tips()

# Bar chart showing total bills split by day and gender
fig = px.bar(
    df_tips, 
    x="day", 
    y="total_bill", 
    color="sex", 
    barmode="group",               # Options: 'group', 'stack', 'overlay'
    title="Total Bill Amounts by Day"
)

fig.show()


df_stocks = px.data.stocks()       # Stock market data over time

fig = px.line(
    df_stocks, 
    x="date", 
    y="GOOG",                      # Google stock price
    title="Google Stock Performance"
)

fig.show()