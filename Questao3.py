import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import librosa

def h_n(n):
    h = np.zeros(n)
    for i in range(n):
        if i == 0:
            h[i] = 1
        elif i == 1:
            h[i] = 0.5
        elif i == 3:
            h[i] = -0.25
        else:
            h[i] = 0
    return h

def convolucao(x, h):
    N1 = len(x)
    N2 = len(h)
    N = N1 + N2 - 1
    y = np.zeros(N)
    for n in range(N):
        for k in range(N1):
            if n - k >= 0 and n - k < N2:
                y[n] += x[k] * h[n - k]
    return y

x, Fs = librosa.load('fala_sino.wav', sr=None)

n = len(x)
h = h_n(n)

y = convolucao(x, h)
y = y[:len(x)]
plt.figure()
plt.plot(x)
plt.plot(y)
plt.legend(['Áudio Original', 'Áudio Filtrado'])
plt.show()

sd.play(x, Fs)
sd.wait()
sd.play(y, Fs)
sd.wait()
