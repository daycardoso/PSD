import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift

# Parâmetros do sinal
sampling_rate = 1000  # Taxa de amostragem em Hz
T = 1.0  # Duração do sinal em segundos
t = np.linspace(0, T, int(sampling_rate * T), endpoint=False)  # Vetor de tempo

# Sinal: Pulso Retangular
x = np.zeros_like(t)
x[int(sampling_rate * T/4):int(sampling_rate * T/4 + sampling_rate * T/10)] = 1

# Aplicando a Transformada de Fourier
X_f = fft(x)
f = fftfreq(len(x), 1/sampling_rate)

# Deslocamento do espectro para centrar em f=0
X_f_shifted = fftshift(X_f)
f_shifted = fftshift(f)

# Plotando o sinal no tempo e seu espectro
plt.figure(figsize=(12, 6))

# Sinal no domínio do tempo
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Pulso Retangular - Domínio do Tempo')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

# Espectro no domínio da frequência
plt.subplot(2, 1, 2)
plt.plot(f_shifted, np.abs(X_f_shifted))
plt.title('Pulso Retangular - Espectro de Fourier (Função sinc)')
plt.xlabel('Frequência [Hz]')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()
