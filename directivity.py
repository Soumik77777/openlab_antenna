import matplotlib.pyplot as plt
import numpy as np
import os
import csv
import open_csv



#### Taking inputs
loc = os.getcwd()+"/data/"
filename = 'yagi7.csv'
delim = None

#### Loading Data
x,y=[],[]
data = open_csv.read_csv(filename, location=loc, delimiter=delim)
for i in range(len(data[0])):
    x.append(data[0][i])
    y.append(data[1][i])


area = 0
for i in range(len(x)-1):
    area += (y[i] + y[i+1]) * (abs(x[i] - x[i+1])) /2

isotropic_length = area / abs(x[-1] - x[0])

directivity = max(y) / isotropic_length
print(directivity)


plt.plot(x, y, label='Directivity (2D)= '+str(round(directivity, 4)))
plt.xlabel("Angle (Deg)")
plt.ylabel("Output Current ($\mu A$)")
plt.grid()
plt.axhspan(0, ymax=isotropic_length, color='cyan')
plt.legend()
plt.show()