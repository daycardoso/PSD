import numpy as np
import matplotlib.pyplot as plt

# Definindo o sinal contínuo: Pulso Gaussiano
def gaussian_pulse(t):
    return np.exp(-t**2)

# Parâmetros do sinal e amostragem
T = 3.0  # Duração total em segundos
sampling_rate = 50  # Taxa de amostragem em Hz (adequada para evitar aliasing)
t_continuous = np.linspace(-T, T, 1000)  # Vetor de tempo contínuo
x_continuous = gaussian_pulse(t_continuous)  # Sinal contínuo

# Amostragem
T_s = 1 / sampling_rate
n_samples = np.arange(-T, T, T_s)
x_sampled = gaussian_pulse(n_samples)

# Reconstrução do sinal contínuo a partir das amostras usando interpolação sinc
t_reconstructed = np.linspace(-T, T, 1000)
x_reconstructed = np.zeros_like(t_reconstructed)

for n in range(len(n_samples)):
    x_reconstructed += x_sampled[n] * np.sinc((t_reconstructed - n_samples[n]) / T_s)

# Plotando os sinais
plt.figure(figsize=(12, 8))

# Sinal contínuo original
plt.subplot(3, 1, 1)
plt.plot(t_continuous, x_continuous, label='Sinal Contínuo (Pulso Gaussiano)')
plt.title('Sinal Contínuo')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Sinal amostrado
plt.subplot(3, 1, 2)
plt.stem(n_samples, x_sampled, 'r', basefmt=" ", label='Amostras')
plt.title('Sinal Amostrado')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Sinal reconstruído
plt.subplot(3, 1, 3)
plt.plot(t_reconstructed, x_reconstructed, 'g-', label='Sinal Reconstruído')
plt.plot(t_continuous, x_continuous, 'b--', label='Sinal Contínuo Original')
plt.title('Reconstrução do Sinal')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
