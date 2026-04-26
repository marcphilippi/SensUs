import numpy as np
import os
import csv
from modelReader import Reader
from dataProcessor import Processor
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# files out of which the model shall be generated
names = ["A","B","D","E","L","M","P"]
concentrations = [25,50,75,125,150,200,250,300]

################################################################################################################################################
def func(x, A, B,C):
    return A * np.log(B * np.asarray(x)) + C

reader = Reader()
processor = Processor()

electrodes = reader.buildFilenames(names,concentrations)

# read model_data
voltage_peak_electrodes = []
current_peak_electrodes = []
for i in range(len(electrodes)):
    electrode_i = electrodes[i]
    data_paths = reader.buildPath(electrode_i)
    
    peak_voltage = []
    peak_current = []
    for j in range(len(data_paths)):

        #extract data from file
        data_read = reader.readFile(data_paths[j])

        # find peak
        peak = processor.findPeak(data_read)
        peak_voltage.append(peak[0])
        peak_current.append(peak[1])
    voltage_peak_electrodes.append(peak_voltage)
    current_peak_electrodes.append(peak_current)
print("current_peak_electrodes: " + str(current_peak_electrodes))


# average current peaks
current_peak_mean = np.mean(current_peak_electrodes,axis=0)
print("current_peak_mean: "+ str(current_peak_mean))


legend = names
legend.append("fit")
colors = ['blue','green','orange','black','purple','pink','gray','olive','cyan','brown','gold','lime']
for idx in range(len(current_peak_electrodes)):
    plt.scatter(concentrations,current_peak_electrodes[idx],color=colors[idx])
plt.plot(concentrations,current_peak_mean, 'o', label='original data',color='red')

parameters, covariance = curve_fit(func,np.asarray(concentrations,dtype=np.float64),np.asarray(current_peak_mean,dtype=np.float64))
fit_A = parameters[0]
print("fit_A: " + str(fit_A))
fit_B = parameters[1]
print("fit_B: " + str(fit_B))
fit_C = parameters[2]
print("fit_C: " + str(fit_C))
fit = func(concentrations, fit_A, fit_B, fit_C)
plt.plot(concentrations,fit, '-',color='red')
plt.legend(legend)

#plt.plot(concentrations, regression.intercept + np.multiply(regression.slope,concentrations), 'r', label='fitted line')
plt.grid()
plt.title("DTE Model")
plt.xlabel("concentrations in µM")
plt.ylabel("current in µA")
plt.show()

   
    



