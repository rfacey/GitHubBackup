import os
import matplotlib.pyplot as plt
import numpy as np

#Check to see if the data file exists in the current directory

filecheck = 0
data = []

for r, d, f in os.walk(os.getcwd()):
    for file in f:
        if file == 'MPCORB.DAT':
            filecheck = 1
        else:
            ''

#If the file exists, do nothing. If does not exist, download it.

if filecheck == 0:
    os.system(f"wget https://minorplanetcenter.net//iau/MPCORB/MPCORB.DAT")
else:
    ''

#Write the dataset into an array

dataFile = open("MPCORB.DAT", "r")

for line in dataFile:
    if line.strip() != '':
        data.append(line.strip())
    else:
        ''
#Get the header, used in testing

dataHeader = data[30].split()
        
        
#Delete the header and comments

del data[0:32]

#Split the actual data into a list of lists

dataMatrix = [line[1:-1].split() for line in data]

#Remove the raw data

del data

#Set up attribute arrays

peri = []
incl = []
e = []
a = []

for line in dataMatrix:
    peri.append(float(line[5]))                       #Perihelion Distance (Peri)
    incl.append(float(line[7]))                       #Inclination (Incl)
    e.append(float(line[8]))                        #Orbital Eccentricity (e)
    a.append(float(line[5])/(1 - float(line[8])))     #Semi-major axis (a)

#line graph histogram

class histFunc():
    
    def __init__(self, array, title, xlabel, boxes, lowerlimit, upperlimit):
        bins_avg = []
        bin_amounts = []
        bin_label = []
        counter = 0

        for i in np.arange(lowerlimit, upperlimit, (upperlimit - lowerlimit)/ boxes):
            for value in array:
                if value >= i and value < (i+(upperlimit - lowerlimit)/ boxes):
                    counter = counter + 1
                else:
                    ""
            bins_avg.append((i + (i+(upperlimit - lowerlimit)/ boxes))/2)
            bin_label.append(i)
            bin_amounts.append(counter)
            counter = 0

        plt.title(title)
        plt.ylabel('Occurances')
        plt.xlabel(xlabel)
        plt.plot(bins_avg, bin_amounts)
        plt.xticks(bin_label)
        plt.savefig(f'{title}.png')
        plt.show()

#actual histogram

class histAll():
    def __init__(self):
        fig, axs = plt.subplots(4, 1, figsize=(5, 15),sharey=False, tight_layout=True)

        axs[0].hist(peri, np.linspace(0, 50))
        axs[0].set_title('Perihelion')
        axs[0].set_ylabel('Occurances')
        axs[0].set_xlabel('Perihelion Distance (Peri)')

        axs[1].hist(incl, np.linspace(-30, 30))
        axs[1].set_title('Inclination')
        axs[1].set_ylabel('Occurances')
        axs[1].set_xlabel('Inclination (Incl)')

        axs[2].hist(e, np.linspace(0, 1.1))
        axs[2].set_title('Eccentricity')
        axs[2].set_ylabel('Occurances')
        axs[2].set_xlabel('Orbital Eccentricity (e)')

        axs[3].hist(a, np.linspace(0, 50))
        axs[3].set_title('Semi-major')
        axs[3].set_ylabel('Occurances')
        axs[3].set_xlabel('Semi-major axis (a)')

        plt.savefig('plots.jpg')
        plt.show()
