import os

import matplotlib.pyplot as plt
import pandas as pd
import math

cwd = os.getcwd()

file_path_highpass_bode = cwd + "\\assets\\highpass_bode.csv"
file_path_lowpass_bode = cwd + "\\assets\\lowpass_bode.csv"
file_path_add_bode = cwd + "\\assets\\add_bode.csv"

def get_plot_data(file_path):
    data = pd.read_csv(file_path, sep=";")
    frequencies = data.iloc[:,0]
    magnitude = data.iloc[:, 1]
    phase = list(data.iloc[:, 2]*180/math.pi)
    phase[0] = phase[1]
    for i,value in enumerate(phase):
        if i == 0 or i == 1: continue
        if abs(phase[i] - phase[i-1])>60:
            phase[i] = phase[i-1]

    return frequencies, magnitude, phase

def plot_bode(file_path):
    frequencies, magnitude, phase = get_plot_data(file_path)
    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()

    ax1.plot(frequencies, magnitude, color="g")
    ax2.plot(frequencies, phase, color="b", linestyle="--")

    ax1.set_xscale("log")

    ax1.set_xlabel("Frequenz in Hz")
    ax1.set_ylabel("Amplitudengang [dB]")
    ax2.set_ylabel("Phasengang [°]")

    plt.savefig(file_path.replace("assets", "plots").replace("csv", "png"))

plot_bode(file_path_add_bode)