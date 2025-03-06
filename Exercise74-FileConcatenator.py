import pandas as pd

data1 = pd.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data2 = pd.read_csv("https://pythonhow.com/media/data/sampledata_x_2.txt")

data3 = pd.concat([data1,data2])
data3.to_csv("concData.txt",index=None)