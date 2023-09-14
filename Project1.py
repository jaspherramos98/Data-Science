import sys
import urllib.request
import numpy as np
#import panda as pd
import pylab
import scipy.stats as stats


#read data from uci data repository
target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv")
data = urllib.request.urlopen(target_url)
#arrange data into list for labels and list of lists for attributes
xList = []
labels = []
for line in data:
    #split on smicolon
    row = line.strip().split(b';')
    xList.append(row)
print("\n--------------------------------------------\n")
sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(len(xList[1]))) 

print("\n\n---------------------------------------------\nNumeric Summary of Wine Data\n")
target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv")
data = urllib.request.urlopen(target_url)
xList2 = []
labels2 = []
for line in data:
    #split on smicolon
    row2 = line.strip().split(b';')
    xList2.append(row2)
nrow = len(xList2)
ncol = len(xList2[0])

col2Counts = []
for col2 in range(ncol):
    type = [0]*3
    for row2 in xList2:
        try:
            float(row2[col2])
            type[0] += 1
        except ValueError:
            type[1] += 1
    col2Counts.append(type)
  
sys.stdout.write("Col#" + '\t' + "Number" + '\t' + "Strings" + '\t ' + "Other\n")
iCol = 0
for types in col2Counts:
    sys.stdout.write(str(iCol) + '\t' + str(types[0]) +'\t' + str(types[1]) + '\t' + str(types[2]) + "\n")
    iCol += 1

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv")
data = urllib.request.urlopen(target_url)
#arrange data into list for labels and list of lists for attributes
xList4 = []
labels4 = []
for line in data:
    #split on comma
    row4 = line.strip().split(b';')
    xList4.append(row4)
nrow4 = len(xList)
ncol4 = len(xList[1])
type4 = [0]*3
colCounts4 = []
#generate summary statistics for column 3 (e.g.)
col4 = 3
colData4 = []
for row in xList:
    colData4.append(float(row4[col4]))
colArray4 = np.array(colData4)
colMean4 = np.mean(colArray4)
colsd4 = np.std(colArray4)
sys.stdout.write("\n\nMean = " + '\t' + str(colMean4) + '\t\t' + "Standard Deviation = " + '\t ' + str(colsd4) + "\n")
#calculate quantile boundaries
ntiles = 4
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray4, i*(100)/ntiles))
sys.stdout.write("\nBoundaries for 4 Equal Percentiles \n")
print(percentBdry)
sys.stdout.write(" \n")
#run again with 10 equal intervals
ntiles = 10
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray4, i*(100)/ntiles))
sys.stdout.write("Boundaries for 10 Equal Percentiles \n")
print(percentBdry)
sys.stdout.write(" \n")
#The last column contains categorical variables
col = 60
colData = []
for row in xList:
    colData.append(row4[col4])
unique = set(colData)
sys.stdout.write("Unique Label Values \n")
print(unique)
#count up the number of elements having each value
catDict = dict(zip(list(unique),range(len(unique))))
catCount = [0]*2
for elt in colData:
    catCount[catDict[elt]] += 1
sys.stdout.write("\nCounts for Each Value of Categorical Label \n")
print(list(unique))
print(catCount)




print("\n\n---------------------------------------------\nBox plot of Wine Data\n")
target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv")
data = urllib.request.urlopen(target_url)
#arrange data into list for labels and list of lists for attributes
xList3 = []
labels3 = []
next(data)
for line in data:
    #split on comma
    row3 = line.strip().split(b';')
    xList3.append(row3)
nrow3 = len(xList3)
ncol3 = len(xList3[0])
type3 = [0]*3
col3Counts = []
#generate summary statistics for column 3 (e.g.)
col3 = 11
col3Data = []
for row3 in xList3:
    col3Data.append(float(row3[col3]))
stats.probplot(col3Data, dist="norm", plot=pylab)
pylab.show()
