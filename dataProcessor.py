import numpy

class Processor:

    def __init__(self):
        self.id = 0

    def findPeak(self,data):
        voltage = data[0]
        current = data[1]

        initial = 0.0
        for idx in range(len(current)):
            if(abs(current[idx]) >= initial and voltage[idx] < 0):
                initial = abs(current[idx])
                max_idx = idx
        
        peak = [voltage[max_idx],abs(current[max_idx])]
        return peak