% Load data
data = readtable('dominant_frequencies_amplitudes_multi_songs.csv');

% Get unique songs
unique_songs = unique(data.Song);

% Define colors for each song
colors = jet(length(unique_songs));

% Plot 3D scatter plot with different colors for each song
figure;
hold on;

for i = 1:length(unique_songs)
    idx = strcmp(data.Song, unique_songs{i});
    scatter3(data.Amplitude(idx), data.Frequency(idx), data.Usage(idx), 50, colors(i, :), 'filled');
end

hold off;

title('3D Scatter Plot of Amplitude, Frequency, and Usage');
xlabel('Amplitude');
ylabel('Frequency (Hz)');
zlabel('Usage');
grid on;

% Adjust view for better visualization
view(45, 30);

% Add legend
legend(unique_songs, 'Location', 'Best');
