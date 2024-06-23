import os
import librosa
import numpy as np

def is_silent(file_path, silence_threshold=1e-4, sr=22050):
    """
    Check if an audio file is silent based on a given RMS threshold.
    
    Args:
    - file_path (str): Path to the audio file.
    - silence_threshold (float): RMS threshold to determine silence.
    - sr (int): Sampling rate to use for the audio file.
    Returns:
    - bool: True if the audio file is considered silent, False otherwise.
    """
    try:
        # Load the audio file
        y, _ = librosa.load(file_path, sr=sr)
        # Calculate the root mean square (RMS) of the audio signal
        rms = np.sqrt(np.mean(y**2))
        # Check if RMS is below the silence threshold
        return rms < silence_threshold
    except Exception as e:
        pass
        return False

def delete_silent_files(directory, silence_threshold=1e-4, sr=22050):
    """
    Delete silent audio files in a specified directory.
    
    Args:
    - directory (str): Path to the directory containing audio files.
    - silence_threshold (float): RMS threshold to determine silence.
    - sr (int): Sampling rate to use for the audio files.
    
    Returns:
    - list: List of deleted silent files.
    """
    deleted_files = []
    # Walk through the directory and process each file
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file has a supported audio extension
            if file.endswith(('.wav', '.mp3', '.flac')):
                file_path = os.path.join(root, file)
                # If the file is silent, delete it and add to the list of deleted files
                if is_silent(file_path, silence_threshold, sr):
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    print(f"Deleted silent file: {file_path}")
    return deleted_files

# Define the input directory containing audio files
input_dir = 'path/to/directory'
# Delete silent files and get the list of deleted files
deleted_files = delete_silent_files(input_dir)

# Print completion message and the list of deleted files
print("Silent files have been deleted successfully")
print(f"Deleted files: {deleted_files}")
