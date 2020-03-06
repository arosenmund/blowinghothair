from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
import os

os.getcwd()

# read audio samples
samplerate, sampledata = read("..\\audiosamples\\waves\\Hello-2-20-T2.wav")
totalsamples = len(sampledata)
totaltime_s = totalsamples/samplerate

#take the mean of the data covert from stereo to mono

#plotting initial samples
plt.plot(sampledata[0:totalsamples])
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("Raw Mono Audio")
plt.show()


#change values to postive values

sampledata = np.absolute(sampledata)

##abs value plot
plt.plot(sampledata[0:totalsamples-1])
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("Absolute Raw Audio")
plt.show()

#grab mena of data for later use

average_amplitude = np.mean(sampledata)

#Transform data to a mean across a specific period (non moving mean)

#seconds used for data transmit in bits per second in transmit file
seconds = 5

#seconds converted to a value of total samples
window = seconds * samplerate

#calculate number of windows in dataset
total_windows = totalsamples/window

#run through data set and set values in each window equal to the mean of the window
i = 0
s = 0
f = window
while i < total_windows:
    average = np.mean(sampledata[s:f])
    sampledata[s:f] = average
    s+=window
    f+=window
    i+=1

# Make equal to the period of listening need to find a way to get close to the begining like a start signal.....
##abs value plot
plt.plot(sampledata[0:totalsamples-1])
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("Averaged Audio Across Period")
plt.show()

#then set all equal to specific averages.


sampledata[(sampledata < average_amplitude)] = 0
sampledata[(sampledata > average_amplitude)] = 1



##abs value plot
plt.plot(sampledata[0:totalsamples-1])
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("Absolute Raw Audio")
plt.show()

#now need to turn that into 1 & 0
i = 0
halfp = int(window/2)
while i < total_windows:
    print(binaryAudio[halfp-1])
    halfp+=window
    i+=1

#Translate into bytes and back into ascii for demo



### Extra stuff

#channel1 = sampledata[:,0] 
#channel2 = sampledata[:,1]

#list audio files
#i = 0
#while i < (totalsamples-1):
#    print(sampledata[i])
#    i+=1
#list audio files in absolute value.
#i = 0
#while i < (totalsamples-1):
#    print(absolutesampledata[i])
#    i+=1