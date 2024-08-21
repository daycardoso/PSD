import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal contínuo
f_signal = 5  # Frequência do sinal original em Hz
t_continuous = np.linspace(0, 1, 1000, endpoint=False)  # Tempo contínuo
x_continuous = np.sin(2 * np.pi * f_signal * t_continuous)  # Sinal contínuo (senoide)

# Amostragem com diferentes taxas
f_s1 = 20  # Taxa de amostragem 1 em Hz (adequada)
f_s2 = 8   # Taxa de amostragem 2 em Hz (abaixo da Nyquist, causará aliasing)
n1 = np.arange(0, 1, 1/f_s1)  # Pontos de amostragem para f_s1
n2 = np.arange(0, 1, 1/f_s2)  # Pontos de amostragem para f_s2

x_sampled1 = np.sin(2 * np.pi * f_signal * n1)  # Sinal amostrado com f_s1
x_sampled2 = np.sin(2 * np.pi * f_signal * n2)  # Sinal amostrado com f_s2

# Plotando os sinais contínuos e amostrados
plt.figure(figsize=(12, 8))

# Sinal contínuo
plt.subplot(3, 1, 1)
plt.plot(t_continuous, x_continuous, label='Sinal Contínuo (5 Hz)')
plt.title('Sinal Contínuo')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Sinal amostrado adequadamente
plt.subplot(3, 1, 2)
plt.plot(t_continuous, x_continuous, 'b-', label='Sinal Contínuo (5 Hz)')
plt.stem(n1, x_sampled1, 'r', basefmt=" ", label='Amostras (f_s = 20 Hz)')
plt.title('Sinal Amostrado - Taxa Adequada')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Sinal com aliasing
plt.subplot(3, 1, 3)
plt.plot(t_continuous, x_continuous, 'b-', label='Sinal Contínuo (5 Hz)')
plt.stem(n2, x_sampled2, 'r', basefmt=" ", label='Amostras (f_s = 8 Hz)')
plt.title('Sinal Amostrado - Taxa Inadequada (Aliasing)')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
