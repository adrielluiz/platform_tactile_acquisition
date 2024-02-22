# Read an excel column and process the data using a butterworth filter
# Plot the data and the filtered data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

# Read the excel file
def read_excel(file):
    df = pd.read_excel(file)
    return df

# Process the data using a butterworth filter
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Plot the data and the filtered data
def plot_data(data, filtered_data, fs, cutoff):
    plt.figure()
    plt.plot(data, 'b-', label='data')
    plt.plot(filtered_data, 'g-', linewidth=2, label='filtered data')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.title('Data and Filtered Data')
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')
    plt.show()

# Main function
def main():
    file = 'plataform_data[6].xlsx'
    df = read_excel(file)
    data = df['ResistiveSensor'].values
    fs = 1000.0
    cutoff = 100.0
    order = 6
    filtered_data = butter_lowpass_filter(data, cutoff, fs, order)
    
    plot_data(filtered_data, filtered_data, fs, cutoff)

if __name__ == "__main__":
    main()
    