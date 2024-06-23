# Audio Silence Detector and Remover with Python

**Purpose:**
This Python script detects and deletes silent audio files in a specified directory. It calculates the root mean square (RMS) of audio signals to determine if they are below a specified silence threshold.

**Features:**
- Supports multiple audio formats: `.wav`, `.mp3`, `.flac`. (You can adjust by extension if you need to.)
- Adjustable silence threshold for flexibility.
- Processes all audio files in the specified directory and deletes those deemed silent.
- Provides a list of deleted silent files.

**Requirements:**
- Python 3.x
- librosa
- numpy

**Installation:**
pip install librosa numpy

**Usage:**
1. Define the path to your directory containing audio files.
2. Run the script to delete silent audio files.

**License:**
MIT License
