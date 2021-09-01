import moviepy.editor as mp

video = input("Enter path of video: ")

mp.VideoFileClip(video)

video.audio.write_audiofile(r"output.mp3")