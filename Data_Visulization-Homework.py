import pandas as pd
import plotly.express as px
from google.colab import files
data_to_load=files.upload()

df=pd.read_csv("data.csv")
fig=px.bar(df,x='Country',y='InternetUsers')
fig.show()
