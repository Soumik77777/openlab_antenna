import matplotlib.pyplot as plt
import numpy as np
import os
import csv

angle1 = 35
angle2 = 315

hpbw = abs(angle2-angle1)
if hpbw>180:
    hpbw = 360-hpbw

print(hpbw)








