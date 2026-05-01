import numpy as np
import os
from modelReader import Reader
from dataProcessor import Processor

#need test 

filename = ""
file_path =

fit_A = 554.8316785598106
fit_B = 1.294356863246618
fit_C = -1272.5231509085318

true_concentration = 150 

#load data and find the peak
reader = Reader()
processor = Processor()

data = reader.readFile(file_path)
peak = processor.findPeak(data)
measurement = peak[1]
print("measurement: " + str(measurement))

# Konzentration berechnen
concentration = np.exp((measurement - fit_C) / fit_A) / fit_B
print("concentration: " + str(round(concentration, 2)) + " µM")

# Scoring
rel_error = abs(concentration - true_concentration) / true_concentration * 100

if rel_error <= 10:
    zone, points = "BLUE", 2
elif rel_error <= 25:
    zone, points = "GREEN", 1
else:
    zone, points = "GREY", 0

print("rel. error: " + str(round(rel_error, 1)) + "%")
print("zone: " + zone + " → " + str(points) + " Punkte")
