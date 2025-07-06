from extract_audio import mp4_to_mp3, isolate_vocals
from transcribe_audio import transcribe

input = "input.mp4"
output = "output.mp3"
vocal_output = "output_vocals.mp3"

def run():
    mp4_to_mp3(input, output)
    isolate_vocals()
    transcribe(vocal_output)

run()