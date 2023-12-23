import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq

# Part a
pianowave = np.loadtxt('piano.txt')
trumpetwave = np.loadtxt('trumpet.txt')

piano_fft = np.fft.fft(pianowave)[:10000]
trumpet_fft = np.fft.fft(trumpetwave)[:10000]

pianoA = np.abs(piano_fft)
trumpetA = np.abs(trumpet_fft)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

axes[0, 0].plot(pianowave)
axes[0, 0].set_title('Piano Waveform')
axes[0, 0].set_xlabel('Sample Number')
axes[0, 0].set_ylabel('Amplitude')

axes[0, 1].plot(trumpetwave)
axes[0, 1].set_title('Trumpet Waveform')
axes[0, 1].set_xlabel('Sample Number')
axes[0, 1].set_ylabel('Amplitude')

axes[1, 0].plot(pianoA)
axes[1, 0].set_title('Fourier Transform of Piano Waveform')
axes[1, 0].set_xlabel('Frequency(Hz)')
axes[1, 0].set_ylabel('Magnitude')

axes[1, 1].plot(trumpetA)
axes[1, 1].set_title('Fourier Transform of Trumpet Waveform')
axes[1, 1].set_xlabel('Frequency(Hz)')
axes[1, 1].set_ylabel('Magnitude')

plt.tight_layout()
plt.show()

# Part b
def find_freq(coef, freq):
    index = np.argmax(np.abs(coef))
    fund_freq = freq[index]
    return fund_freq
sample_rate = 44100
piano_coef = rfft(pianowave)
piano_freq = rfftfreq(len(pianowave), 1/sample_rate)

trumpet_coef = rfft(trumpetwave)
trumpet_freq = rfftfreq(len(trumpetwave), 1/sample_rate)

piano_fund_freq = find_freq(piano_coef, piano_freq)
trumpet_fund_freq = find_freq(trumpet_coef, trumpet_freq)

print("The fundamental frequency for piano is: ", piano_fund_freq)
print("The fundamental frequency for trumpet is: ", trumpet_fund_freq)
