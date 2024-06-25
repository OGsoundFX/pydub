from pydub import AudioSegment

# List of audio file paths to be mixed
audio_files = ["monster.wav", "punch.wav", "spell.wav"]

# Function to find the longest audio file
def find_longest_audio(files):
    longest_audio = None
    max_length = 0
    file_index = 0
    for file in files:
        audio = AudioSegment.from_wav(file)
        if len(audio) > max_length:
            longest_audio = audio
            max_length = len(audio)
            file_index = files.index(file)
    return longest_audio, file_index

# Find the longest audio file
mixed_audio = find_longest_audio(audio_files)[0]

# Remove the longest audio file from the list
audio_files.pop(find_longest_audio(audio_files)[1])

# Load the first audio file
# mixed_audio = AudioSegment.from_wav(audio_files[0])

# Iterate over the remaining audio files and overlay them
for file in audio_files[0:]:
    next_audio = AudioSegment.from_wav(file)
    mixed_audio = mixed_audio.overlay(next_audio)

# Export the mixed audio to a new file
mixed_audio.export("exports/mixed_audio.wav", format="wav")
