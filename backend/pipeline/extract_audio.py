import ffmpeg 
from audio_separator.separator import Separator
from pipeline.verify_file import check_path

def mp4_to_mp3(input, output):
    check_path(input)
    check_path(output)
    ffmpeg.input(input).output(output).overwrite_output().run()

def isolate_vocals(output):
    check_path(output)
    seperator = Separator(output_format="MP3", output_single_stem="Vocals")
    seperator.load_model("mel_band_roformer_kim_ft_unwa.ckpt")
    seperator.separate(output, {"Vocals": "output_vocals"})

