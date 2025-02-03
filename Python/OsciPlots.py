import os

import matplotlib.pyplot as plt
import pandas as pd
import math

cwd = os.getcwd()

file_path_highpass_200 = cwd + "\\assets\\highpass_osc_200.csv"
file_path_highpass_1000 = cwd + "\\assets\\highpass_osc_1000.csv"
file_path_highpass_4500 = cwd + "\\assets\\highpass_osc_4500.csv"
file_path_lowpass_200 = cwd + "\\assets\\lowpass_osc_200.csv"
file_path_lowpass_1000 = cwd + "\\assets\\lowpass_osc_1000.csv"
file_path_lowpass_4500 = cwd + "\\assets\\lowpass_osc_4500.csv"

def get_plot_data(file_path):
    data = pd.read_csv(file_path, sep=";")
    positive_time_index = 0
    for index, time_value in enumerate(data.iloc[:,0]):
        if time_value >= 0:
            positive_time_index = index
            break

    time = data.iloc[:,0][positive_time_index:]
    u_e = data.iloc[:,1][positive_time_index:]
    u_a = data.iloc[:,2][positive_time_index:]

    return time, u_e, u_a

def plot_bode(file_path):
    time, u_e, u_a = get_plot_data(file_path)
    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()

    ax1.plot(time, u_e, color="g")
    ax2.plot(time, u_a, color="b")

    ax1.set_xlabel("Zeit [ms]")
    ax1.set_ylabel("U_e [V]")
    ax2.set_ylabel("U_a [V]")

    ax1.set_ylim(-1.5, 1.5)
    ax2.set_ylim(-1.5, 1.5)

    plt.savefig(file_path.replace("assets", "plots").replace("csv", "png"))

plot_bode(file_path_lowpass_200)
plot_bode(file_path_lowpass_1000)
plot_bode(file_path_lowpass_4500)
plot_bode(file_path_highpass_4500)
plot_bode(file_path_highpass_4500)
plot_bode(file_path_highpass_4500)