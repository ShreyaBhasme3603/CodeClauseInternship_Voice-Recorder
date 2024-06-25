import pyaudio
import wave

def record_audio(output_file, duration, sample_rate=44100, channels=2, format=pyaudio.paInt16):
    audio = pyaudio.PyAudio()

    # Set up recording parameters
    stream = audio.open(format=format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=1024)

    print("Recording...")

    frames = []
    # Record audio for the specified duration
    for i in range(0, int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate() 
    
    # Save the recorded audio to a WAV file
    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

if __name__ == "__main__":
    output_file = "recorded_audio.wav"  # Change the output file name if needed
    duration = 5  # Specify the duration of the recording in seconds
    record_audio(output_file, duration)
