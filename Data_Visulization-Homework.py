import pandas as pd
import plotly.express as px
from google.colab import files
data_to_load=files.upload()

df=pd.read_csv("data.csv")
fig = px.scatter(df, x="date",y="cases",color="country")
fig.show()
