# Please concatenate this file with this one to a single text file. The content of the output file should look like in the expected output.

import pandas as pd

data1 = pd.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data2 = pd.read_csv("https://pythonhow.com/media/data/sampledata_x_2.txt")

data3 = pd.concat([data1,data2])
data3.to_csv("concData.txt",index=None)