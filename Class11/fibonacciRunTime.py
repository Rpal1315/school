import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("fibonacciRunTime.csv")
plt.plot(data.counter, data.time_diff)
plt.show()
