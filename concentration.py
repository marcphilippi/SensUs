import numpy as np
import os
from modelReader import Reader
from dataProcessor import Processor
import matplotlib.pyplot as plt

filename = "D_creatinine_150"
file_path = os.path.join(os.getcwd(),'Desktop','ETE',filename + '.csv' )
fit_A = 554.8316785598106
fit_B = 1.294356863246618
fit_C = -1272.5231509085318
x = np.arange(10,305,5)
#################################################################################################################################################

def func(x, A, B,C):
    return A * np.log(B * np.asarray(x)) + C

reader = Reader()
processor = Processor()

data = reader.readFile(file_path)

peak = processor.findPeak(data)
print("peak: " + str(peak))

measurement = peak[1]
print("measurement: " + str(measurement))

ref_func = func(x,fit_A,fit_B,fit_C)

min_distance = float('inf')
min_idx = 0
for idx in range(len(ref_func)):
    if np.linalg.norm(ref_func[idx] - measurement) <= min_distance:
        min_distance = np.linalg.norm(ref_func[idx] - measurement)
        min_idx = idx


concentration = x[min_idx]
print("concentration: " + str(concentration) + " μM")