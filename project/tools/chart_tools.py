import plotly.graph_objects as go
from pathlib import Path
import time

CHARTS_DIR = Path(__file__).parent.parent / "charts"
CHARTS_DIR.mkdir(exist_ok=True)

def _save(fig, name):
    ts = int(time.time())
    path = str(CHARTS_DIR / f"{name}_{ts}.png")
    fig.write_image(path)
    fig._saved_path = path
    return fig

def generate_line_chart(x, y, title="Line Chart", x_label="X-axis", y_label="Y-axis", **kwargs):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines'))
    fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
    return _save(fig, "line_chart")

def generate_bar_chart(x, y, title="Bar Chart", x_label="X-axis", y_label="Y-axis", **kwargs):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y))
    fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
    return _save(fig, "bar_chart")

def generate_pie_chart(labels, values, title="Pie Chart", **kwargs):
    fig = go.Figure()
    fig.add_trace(go.Pie(labels=labels, values=values))
    fig.update_layout(title=title)
    return _save(fig, "pie_chart")

def generate_scatter_plot(x, y, title="Scatter Plot", x_label="X-axis", y_label="Y-axis", **kwargs):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers'))
    fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
    return _save(fig, "scatter_plot")

def generate_histogram(data=None, title="Histogram", x_label="X-axis", y_label="Y-axis", x=None, dataframe=None, df=None, column=None, **kwargs):
    src = dataframe if dataframe is not None else df
    d = data if data is not None else x
    if column is not None and src is not None:
        d = src[column]
    elif src is not None and isinstance(d, str):
        if d in src.columns:
            d = src[d]
        else:
            d = src
    elif src is not None and d is None:
        d = src
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=d))
    fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
    return _save(fig, "histogram")
