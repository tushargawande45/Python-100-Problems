# plot the data in the file provided through the URL https://pythonhow.com/media/data/sampledata.txt

import pandas as pd
import matplotlib.pyplot as plt

url = "https://pythonhow.com/media/data/sampledata.txt"
data = pd.read_csv(url)

# Scatter plot
data.plot(x='x', y='y', kind='scatter', color='blue', title="Scatter Plot of Sample Data")

# Save the plot as an image
plt.savefig("plot.png")  

# Show the plot
plt.show()
