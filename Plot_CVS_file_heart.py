import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tutorial.csv")
df = df.to_numpy()
#convert the csv into an array

dates = df[:,0]

row = len(dates)

time = []
for i in range(row):
    num = dates[i][11:25]
    num = num.replace(':','')
    num = float(num)
    time.append(num)
    
time = np.transpose(time)
y = df[:,1]
plt.plot(time,y)
plt.ylabel('ylabel')
plt.xlabel('Time')
plt.show()

print(time)
print(y)
