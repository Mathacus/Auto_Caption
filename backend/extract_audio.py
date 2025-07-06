import ffmpeg 
from audio_separator.separator import Separator

def mp4_to_mp3(input, output):
    ffmpeg.input(input).output(output).run()

def isolate_vocals():
    seperator = Separator(output_format="MP3", output_single_stem="Vocals")
    seperator.load_model("mel_band_roformer_kim_ft_unwa.ckpt")
    seperator.separate("output.mp3", {"Vocals": "output_vocals"})
