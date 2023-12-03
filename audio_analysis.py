import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import csv
import os

def analyze_audio(audio_path):
    # Load audio file
    y, sr = librosa.load(audio_path)

    # Compute the spectrogram
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

    # Generate time values
    time = np.linspace(0, len(y)/sr, len(y))

    # Assume dominant_frequencies and amplitudes are lists containing the top 20 dominant frequencies and their amplitudes
    # For illustration purposes, generate some sample frequencies and amplitudes
    dominant_frequencies = np.linspace(100, 1000, 20)
    amplitudes = np.random.rand(20)  # Replace this with the actual amplitudes from your analysis

    # Sort frequencies based on amplitudes (usage)
    sorted_indices = np.argsort(amplitudes)[::-1]
    dominant_frequencies = dominant_frequencies[sorted_indices]
    amplitudes = amplitudes[sorted_indices]

    # Assign rank based on sorted order
    ranks = np.arange(0, len(dominant_frequencies))

    return time, amplitudes, dominant_frequencies, ranks

# Specify the folder containing audio files
audio_folder = "./audio_folder"

# Analyze multiple songs in the folder
all_times = []
all_amplitudes = []
all_frequencies = []
all_ranks = []

for filename in os.listdir(audio_folder):
    if filename.endswith(".mp3"):
        audio_path = os.path.join(audio_folder, filename)
        time, amps, frequencies, ranks = analyze_audio(audio_path)
        all_times.append(time)
        all_amplitudes.append(amps)
        all_frequencies.append(frequencies)
        all_ranks.append(ranks)

# Save to CSV with amplitude, frequency, and rank for all songs
with open('dominant_amplitudes_frequencies_ranks_multi_songs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Song', 'Amplitude', 'Frequency', 'Rank'])
    for i, (time, amps, freqs, ranks) in enumerate(zip(all_times, all_amplitudes, all_frequencies, all_ranks)):
        for t, amp, freq, rank in zip(time, amps, freqs, ranks):
            writer.writerow([f"Song {i+1}", t, amp, freq, rank])
