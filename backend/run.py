from pipeline.extract_audio import mp4_to_mp3, isolate_vocals
from pipeline.transcribe_audio import transcribe
import asyncio

def run(input, output, vocal_output):
    mp4_to_mp3(input, output)
    isolate_vocals(output)
    transcribe(vocal_output)

input_file = "./files/input.mp4"
output_file = "./files/output.mp3"
vocal_output_file = "./files/output_vocals.mp3"

run(input_file, output_file, vocal_output_file)