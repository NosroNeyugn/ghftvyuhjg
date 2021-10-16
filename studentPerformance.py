from os import stat
import plotly.figure_factory as px
import pandas as  pd
import random
import csv
import statistics
import plotly.graph_objects as go

df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()
mean=statistics.mean(data)
standard_deviation=statistics.stdev(data)
median=statistics.median(data)
mode=statistics.mode(data)
fig=px.create_distplot([data],["reading score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17 ], mode="lines", name="MEAN"))
first_std_dev_start,first_std_dev_end=mean-standard_deviation,mean+standard_deviation
second_std_dev_start,second_std_dev_end=mean-(2*standard_deviation),mean+(2*standard_deviation)
third_std_dev_start,third_std_dev_end=mean-(3*standard_deviation),mean+(3*standard_deviation)
fig.add_trace(go.Scatter(x=[first_std_dev_start,first_std_dev_start],y=[0,0.17],mode="lines", name="standarddeviation1start"))
fig.add_trace(go.Scatter(x=[first_std_dev_end,first_std_dev_end],y=[0,0.17],mode="lines", name="standarddeviation1end"))
fig.add_trace(go.Scatter(x=[second_std_dev_start,second_std_dev_start],y=[0,0.17],mode="lines", name="standarddeviation2start"))
fig.add_trace(go.Scatter(x=[second_std_dev_end,second_std_dev_end],y=[0,0.17],mode="lines", name="standarddeviation2end"))
fig.show()
print("Mean: ",mean)
print("Standard Deviation: ",standard_deviation)
print("Mean of Data: ",mean_data)
print("Standard Deviation of Data:",standard_deviation_data)
