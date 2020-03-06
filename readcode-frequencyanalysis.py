from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
import scipy

# read audio samples
samplerate, sampledata = read("samplefans1.wav")
totalsamples = len(sampledata)
totaltime_s = totalsamples/samplerate
totalsamples = len(sampledata)
totaltime_s = totalsamples/samplerate

channel1 = sampledata[:,0] 
channel2 = sampledata[:,1]

rawAudio = np.mean(sampledata, axis=1)

#fft_out = scipy.fft.fft(rawAudio[0:44100])

#plt.plot(rawAudio, np.abs(fft_out))

#plt.show()


#freqs = scipy.fft.fftfreq(len(fft_out)) * samplerate

#plt.stem(freqs, np.abs(fft_out), use_line_collection=True)
#plt.xlabel('Frequency in Hertz [Hz]')
#plt.ylabel('Frequency Domain (Spectrum) Magnitude')
#plt.xlim(-samplerate/2, samplerate/2)
#plt.ylim(-5, 110)

#plt.show()


#scipy.fft




frequencies, times, spectrogram = sig.spectrogram(rawAudio, samplerate)

plt.pcolormesh(times,frequencies,spectrogram)
plt.imshow(spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
