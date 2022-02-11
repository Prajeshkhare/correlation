import csv
import plotly.express as px
import numpy as np
from tenacity import retry

# with open ("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv")as csv_file:
#     df = csv.DictReader(csv_file)
#     fig = px.scatter(df,x="Temperature", y= "Ice-cream Sales")
#     fig.show()

def getdatasource(data_path):
    Temperature = []
    cold_drink_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Temperature.append(float(row["Temperature"]))
            cold_drink_sales.append(float(row["Cold drink sales"]))

    return{"x" :Temperature,"y" :cold_drink_sales}

def findCorrelation(datasoucre):
    correlation = np.corrcoef(datasoucre["x"],datasoucre["y"])
    print("correlation between Temperature vs cold drink sales :\n--->",correlation[0,1])

def setup():
    data_path = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    datasource = getdatasource(data_path)
    findCorrelation(datasource)

setup()