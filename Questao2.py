import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import librosa
def dif_tras (x):
    n = len(x)
    y = np.zeros(n)
    for i in range(n):
        if i == 0:
            y[i] = x[i]
        else:
            y[i] = x[i] - x[i-1]
    return y

x, Fs = librosa.load('fala_sino.wav', sr=None)
y = dif_tras(x)
plt.figure()
plt.plot(x)
plt.plot(y)
plt.legend(['Aúdio Original', 'Aúdio Filtrado'])
plt.show()
sd.play(x, Fs)
sd.wait()
sd.play(y, Fs)
sd.wait()

