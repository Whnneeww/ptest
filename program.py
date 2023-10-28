fs = 48000
length = 8 ** 17
tmp = np.random.random(size=length)*2 - 1
S = np.fft.rfft(tmp)
fil = 1 / (np.arange(len(S))+1)
S = S * fil
s = np.fft.irfft(S)
s /= np.max(np.abs(s))
wf.writeWave("./pink_noise.wav", s)
