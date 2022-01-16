import csv
from email import message_from_string
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random
import pandas as pd
import statistics

df=pd.read_csv("data.csv")
data=df["average"].tolist()

fig=ff.create_distplot([data],["Average"], show_hist=False)
fig.show()

list=[]
for i in range(0,100):
    randomindex=random.randint(1,len(data))
    value=data[randomindex]
    list.append(value)

mean=statistics.mean(list)
std_dev=statistics.stdev(list)

print("The Mean =", mean)
print("The std_deviation =", std_dev)

def random_set_of_mean(counter):
    list1=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        list1.append(value)
    mean_of_sample_data=statistics.mean(list1)
    #std_dev_of_sample_data=statistics.stdev(list1)
    return mean_of_sample_data

def show_graph(list2):
    file=list2
    mean_of_file=statistics.mean(file)
    fig=ff.create_distplot([file],["Avg"], show_hist=False)
    fig.show()

def setup():
    list=[]
    for i in range(0,1000):
        randomdata=random_set_of_mean(100)
        list.append(randomdata)
    show_graph(list)
    mean=statistics.mean(list)
    std_dev=statistics.stdev(list)
    print("The Mean of Sampling Distribution =", mean)
    print("The Standard Deviation =", std_dev)

setup()