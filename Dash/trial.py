import pandas as pd
import re

df = pd.read_csv("D:\Dash\Data\Daily Sales report 01-03-2019 to 06-06-2019.csv")

series = pd.Series(df)
# dsc = df.describe()

print(series)
