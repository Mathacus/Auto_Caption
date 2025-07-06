from faster_whisper import WhisperModel
from pipeline.verify_file import check_path

model_name = "large-v3-turbo"

def transcribe(audio):
    check_path(audio)
    
    model = WhisperModel(
        model_name,
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(
        audio,
        beam_size=5,
        word_timestamps=True
    )

    for seg in segments:
        print(seg.text)