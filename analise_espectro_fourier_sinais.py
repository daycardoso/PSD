import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift

# Parâmetros do sinal
sampling_rate = 1000  # Taxa de amostragem em Hz
Ts = 1/sampling_rate  # Período de amostragem
T = 0.7  # Duração do sinal em segundos
t = np.linspace(0, T-Ts, int(sampling_rate * T), endpoint=False)  # Vetor de tempo

# Sinal 1: Senoide pura de frequência f0
f0 = 50  # Frequência da senoide em Hz
f1 = 2*f0  # Frequência da segunda componente senoidal
x1 = np.cos(2 * np.pi * f0 * t) + 0.5 * np.sin(2 * np.pi * 2*f1 * t)

# Sinal 2: Pulso retangular de duração T/10
x2 = np.zeros_like(t)
x2[int(sampling_rate * T/4):int(sampling_rate * T/4 + sampling_rate * T/10)] = 1

# Função para calcular e plotar o espectro de Fourier
def plot_spectrum(signal, title):
    # Calcula a Transformada de Fourier
    X_f = fft(signal)
    
    # Frequências correspondentes
    f = fftfreq(len(signal), 1/sampling_rate)
    
    # Desloca o zero da frequência para o centro
    X_f_shifted = fftshift(X_f)
    f_shifted = fftshift(f)
    
    # Plotando o sinal no tempo
    plt.figure(figsize=(15, 10))
    
    plt.subplot(2, 1, 1)
    plt.plot(t, signal)
    plt.title(f'{title} - Domínio do Tempo')
    plt.xlabel('Tempo [s]')
    plt.ylabel('Amplitude')
    
    # Plotando o espectro no domínio da frequência
    plt.subplot(2, 1, 2)
    plt.plot(f_shifted, np.abs(X_f_shifted))
    plt.title(f'{title} - Espectro de Fourier')
    plt.xlabel('Frequência [Hz]')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()

# Aplicando e visualizando o espectro de Fourier para cada sinal
plot_spectrum(x1, 'Senoide Pura (50 Hz)')
plot_spectrum(x2, 'Pulso Retangular')

