import torch
import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wav
import io
from silero_vad import load_silero_vad, get_speech_timestamps, collect_chunks

model, utils = torch.hub.load(
    repo_or_dir='snakers4/silero-vad',
    model='silero_vad',
    force_reload=False  
)
(get_speech_timestamps, save_audio, read_audio, VADIterator, collect_chunks) = utils


SAMPLE_RATE = 16000
CHANNELS = 1
MAX_DURATION = 20  

def record_speech():

    print('Started Recording')
    # Record from microphone
    recording = sd.rec(int(MAX_DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype="float32")
    sd.wait()

    # Convert to mono numpy
    audio = recording.squeeze()

    # 🔹 Detect speech segments
    torch_audio = torch.from_numpy(audio).float()
    speech_timestamps = get_speech_timestamps(torch_audio, model, sampling_rate=SAMPLE_RATE)

    if not speech_timestamps:
        print("❌ No speech detected.")
        return False
    else:
        # Collect only speech parts (auto-trim silence)
        speech_audio = collect_chunks(speech_timestamps, torch_audio)

        # Save trimmed audio to memory (WAV)
        buffer = io.BytesIO()
        wav.write(buffer, SAMPLE_RATE, speech_audio.numpy())
        buffer.seek(0) # Moves the pointer to the starting of the audio file in memory

        with open('recordings/recording.mp3','wb') as f:
            f.write(buffer.read())
        
        print('Recording done')
    return True


