### Resources:
- [Library](https://pypi.org/project/pydub/)
- [Documentation](https://pydub.com/)
- [Github](https://github.com/jiaaro/pydub/)

### Installation:
1. Install `pydub` library:
```shell
pip3 install pydub
```
2. Write some code:
```python
from pydub import AudioSegment

# List of audio file paths to be mixed
audio_files = ["monster.wav", "punch.wav", "spell.wav"]

# Load the first audio file
mixed_audio = AudioSegment.from_wav(audio_files[0])

# Iterate over the remaining audio files and overlay them
for file in audio_files[0:]:
    next_audio = AudioSegment.from_wav(file)
    mixed_audio = mixed_audio.overlay(next_audio)

# Export the mixed audio to a new file
mixed_audio.export("exports/mixed_audio.wav", format="wav")

```
