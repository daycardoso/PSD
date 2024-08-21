import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift

# Parâmetros do sinal
sampling_rate = 1000  # Taxa de amostragem em Hz
T = 1.0  # Duração do sinal em segundos
t = np.linspace(0, T, int(sampling_rate * T), endpoint=False)  # Vetor de tempo

# Sinal: combinação de duas senoides de frequências diferentes
f1 = 50  # Frequência da primeira senoide
f2 = 150  # Frequência da segunda senoide
x = np.cos(2 * np.pi * f1 * t) + 0.5 * np.cos(2 * np.pi * f2 * t)

# Função para aplicar e plotar o espectro com e sem janelamento
def plot_spectrum(signal, window, title):
    # Aplicando a janela ao sinal
    windowed_signal = signal * window
    
    # Calcula a Transformada de Fourier
    X_f = fft(windowed_signal)
    
    # Frequências correspondentes
    f = fftfreq(len(signal), 1/sampling_rate)
    
    # Desloca o zero da frequência para o centro
    X_f_shifted = fftshift(X_f)
    f_shifted = fftshift(f)
    
    # Plotando o espectro no domínio da frequência
    plt.figure(figsize=(12, 6))
    plt.plot(f_shifted, np.abs(X_f_shifted))
    plt.title(f'{title} - Espectro de Fourier com {window.__ne__} Window')
    plt.xlabel('Frequência [Hz]')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()

# Janelas
rectangular_window = np.ones_like(x)
hanning_window = np.hanning(len(x))
hamming_window = np.hamming(len(x))
blackman_window = np.blackman(len(x))

# Plotando espectros com diferentes janelas
plot_spectrum(x, rectangular_window, 'Janela Retangular')
plot_spectrum(x, hanning_window, 'Janela de Hanning')
plot_spectrum(x, hamming_window, 'Janela de Hamming')
plot_spectrum(x, blackman_window, 'Janela de Blackman')
