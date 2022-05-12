import matplotlib.pyplot as plt
import numpy as np
import os
import csv
import open_csv

#### Taking inputs
loc = os.getcwd()+"/data/"
filename = 'simple_half.txt'
delim = '\t'
shift = 'yes'
cartesian = 0
polar = 0
dB_polar = 1



#### Loading Data
x,y=[],[]
data = open_csv.read_csv(filename, location=loc, delimiter=delim)
for i in range(len(data[0])):
    x.append(data[0][i])
    y.append(data[1][i])


#### Shifting Axis
if shift == 'yes':
    maxi, max_sl = 0, 0
    for i in range(len(y)):
        if y[i]>maxi:
            maxi = y[i]
            max_sl = i
    new_zero = x[max_sl]
    for i in range(len(x)):
        x[i] = x[i]-new_zero


#### Cartesian Graph
if cartesian==1:
    plt.plot(x,y)
    plt.xlabel("Angle (in Deg)")
    plt.ylabel("Output Current ($\mu A$)")
    plt.grid()
    plt.fill_between(x, 0, y, color='cyan')
    plt.show()


#### Polar Graph
if polar==1:
    r = y
    theta = np.deg2rad(x)

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, label='Output current in $\mu A$ in polar plot')
    ax.set_rmax(2)
    ax.set_rticks(np.linspace(0, max(r)+20, 5))  # Less radial ticks
    ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    ax.grid(True)
    plt.legend()

    #ax.set_title("Field Pattern of folded dipole antenna in Polar Axis", va='bottom')
    plt.show()


#### Polar Graph in dB
if dB_polar==1:
    y_dB = [20 * np.log10(y[i]) for i in range(len(y))]
    r = y_dB
    theta = np.deg2rad(x)

    # -3dB line
    dB_max = [max(y_dB)-3 for i in range(len(y_dB))]

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, label='Output current in dB in polar plot')
    ax.plot(theta, dB_max, label='-3dB gain line')
    ax.set_rmax(2)
    ax.set_rticks(np.linspace(0, max(r)+20, 5))
    ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    ax.grid(True)
    plt.legend()
    #ax.set_title("Field Pattern of folded dipole antenna in Polar Axis", va='bottom')
    plt.show()


