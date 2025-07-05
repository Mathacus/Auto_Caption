import ffmpeg 

input = "input.mp4"
output = "output.mp3"

def  mp4_to_mp3(input, output):
    ffmpeg.input(input).output(output).run()

mp4_to_mp3(input, output)