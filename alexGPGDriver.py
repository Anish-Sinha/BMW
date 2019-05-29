### Code Generated for CSE145/CSE237D
### Alex's Best Implementation of BCI Driver
### 5.28.19

#required libraries
import easygopigo3
import time
import numpy as np
import csv

time_topline = time.clock() # returns current processor clock time in seconds

#################### INITIALIZE GOPIGO AND NEUROSKY ################################

from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
mindwaveDataPointReader = MindwaveDataPointReader()
# connect to the mindwave mobile headset
mindwaveDataPointReader.start()
#mindwave example code:
# print dataPoint.__class__.__name__
# classes: AttentionDataPoint, MeditationDataPoint, RawDataPoint
#   EEGPowersDataPoint: delta, theta, lowAlpha, highAlpha,
#      lowBeta, highBeta, lowGamma, midGamma
#if dataPoint.__class__.__name__ == 'AttentionDataPoint':
#      if (dataPoint > 75):
#            print('***'),

#Instantiate GoPiGo Object
GPG = easygopigo3.EasyGoPiGo3()


#################### GLOBAL VARIABLES & FUNCTIONS ##############################################

#Get width of moving average window:
windowLength = input("How many datapoints for the moving window? ")
#make sudo queue for simple moving average
sma = []
for i in range(0, int(windowLength)):
	sma.append(0)

#keep track of how long the test lasted
time_beforeTry = time.clock()
print "preparation time: " + str(time_beforeTry - time_topline)
#control loop for pi


#initialize array for output to csv
results = []
def ProcessDataForCSV():
	#append what we want for final results
	#results.append("***")

	#format of results row entry:
	#[]

	return
def OutputToCSV():
	with open('testingData.csv', 'w', newline='') as file:
		writer.csvwriter(file)
		if results != []:
			writer.writerow(results)
	return

################### BEGIN CONTROL CODE #############################################
try:
	while(True):
		
		#grab a datapoint from Neurosky
    	dataPoint = mindwaveDataPointReader.readNextDataPoint()
    	if dataPoint.__class__.__name__ == 'AttentionDataPoint':
			print dataPoint
			dataPoint = int(str(dataPoint))
			threshold = 0
			#update sliding window


			#update threshold
			if np.var(sW) > 10:
				threshold = 1

			#Tell it to start or stop
			if threshold:
				GPG.forward()
			else: GPG.stop()

except: KeyboardInterrupt()

GPG.stop()
#output results to csv:
try: 
	OutputToCSV():
	print "Trial ended, data successfully recorded..."
except: print "Error writing to csv, ending program..."







