import os
import csv


class Reader:

    def __init__(self):
        self.id = 0

    def buildFilenames(self,names,concentrations):

        electrodes = []
        for i in range(len(names)):
            electrode = []
            for j in range(len(concentrations)):
                filename = names[i] + "_creatinine_" + str(concentrations[j])
                electrode.append(filename)
            electrodes.append(electrode)
        
        return electrodes

    def buildPath(self,current_electrode):
        path_files = []
        for j in range(len(current_electrode)):
            path = os.path.join(os.getcwd(),'Desktop','ETE',current_electrode[j] + '.csv')
            path_files.append(path)
        return path_files

    def readFile(self,file_path):

        # read in file

        with open(file_path,newline = '',encoding="utf16") as file:
            csv_reader = csv.reader(file, delimiter=',')
                
            # find header
            for row in csv_reader:
                if str(row) == "['V', 'µA']":
            
                    break
                else:
                    continue
                
            # read in everthing after the header
            data = []
                    
            voltage = []
            current = []
            for row in csv_reader:
                if '\ufeff' in str(row[0]):
                    continue
                elif '\ufeff' in str(row[1]):
                    continue
                elif len(row) == 0:
                    continue
                else:
                    voltage.append(float(row[0]))
                    current.append(float(row[1]))

            data.append(voltage)
            data.append(current)

        return data