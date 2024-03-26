import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import librosa
def med_mov (x, M1, M2):
    n = len(x)
    y = np.zeros(n)
    for i in range(n):
        sum_x = 0
        for k in range(-M1, M2+1):
            if i+k >= 0 and i+k < n:
                sum_x += x[i+k]
        y[i] = sum_x/(M1+M2+1)
    return y

x, Fs = librosa.load('fala_sino.wav', sr=None)
M1, M2 = 5, 10
y = med_mov(x, M1, M2)
plt.figure()
plt.plot(x)
plt.plot(y)
plt.legend(['Aúdio Original', 'Aúdio Filtrado'])
plt.show()
sd.play(x, Fs)
sd.wait()
sd.play(y, Fs)
sd.wait()

