from __future__ import print_function

from pydub import AudioSegment

from matplotlib import pyplot as plt

import numpy as np
import math
import sys
import os

argv_l = len(sys.argv)

if argv_l < 2:
    sys.exit('ERROR: Please supply a mp3 file path')

file_name = sys.argv[1]

# getting extension of file
_, ext = os.path.splitext(file_name)
# not mp3 extension
if ext != '.mp3':
    print(ext)
    sys.exit('ERROR: File must be a mp3 audio file')

# opening mp3 song
song = AudioSegment.from_mp3(sys.argv[1])

print()
print("Analyzing", os.path.splitext(os.path.basename(file_name))[0])
sys.stdout.flush()

# duration of song in seconds
t_s = int(len(song) / 1000)
# t_s = 10
# frames per secod of the song
fps = song.frame_rate

# splitting song into different
# channels for multi-channel songs
channels = song.split_to_mono()

# Initializing plot data array
# plot_data = [(0.0, 0.0)] * (t_s * 10)
plot_data = [0.0] * (t_s * 10)

for i in range(t_s * 10):
    # array.array object of song
    data = channels[0][(i * 100):((i + 1) * 100)].get_array_of_samples()

    # performing fourier transformation
    res_fft = np.fft.rfft(data)

    # getting the frequencies
    freq_data = np.fft.rfftfreq(res_fft.size)

    max_amp = 0
    max_freq = 0

    # populating plot data
    for vfft, freq in zip(res_fft, freq_data):
        hz = int(abs(freq * fps))
        if hz > 20 and hz < 16000:
            amp = np.abs(vfft)
            if amp > max_amp:
                max_amp = amp
                max_freq = hz

    # plot_data[i] = (20 * math.log10(max_amp), max_freq)
    plot_data[i] = max_freq

plt.plot(plot_data)
plt.show()

# # output file name
# if argv_l < 3:
#     print()
#     print("Output file name not specified!")
#     print("Defaulting to 'spectrum.plot'")
#     print()
#     file_name = 'spectrum.plot'
# else:
#     file_name = sys.argv[2]

# # opening output file
# f = open(file_name, 'w')

# # writing plot data
# for index, item in enumerate(plot_data):
#     if(item > 0):
#         f.write(repr(index) + " " + repr(item) + "\n")
