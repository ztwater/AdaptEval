import scipy
# Read the .wav file
sample_rate, data = scipy.io.wavfile.read('directory_path/file_name.wav')

# Spectrogram of .wav file
sample_freq, segment_time, spec_data = scipy.signal.spectrogram(data, sample_rate)  
# Note sample_rate and sampling frequency values are same but theoretically they are different measures
