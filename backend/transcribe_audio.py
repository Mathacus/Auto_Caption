from faster_whisper import WhisperModel

model_name = "large-v3-turbo"

def transcribe(audio):
    model = WhisperModel(
        model_name,
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(
        "output_vocals.mp3",
        beam_size=5,
        word_timestamps=True
    )

    for seg in segments:
        print(seg.text)