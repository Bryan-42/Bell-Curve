import pandas as pd
import plotly.figure_factory as px

df = pd.read_csv("data.csv")

fig = px.create_distplot([df["Avg Rating"]],["result"], show_hist = True)
fig.show()

