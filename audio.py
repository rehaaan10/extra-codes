!pip install moviepy --upgrade
import moviepy.editor
video=moviepy.editor.VideoFileClip(r'E:\VID1.mp4')
audio=video.audio
audio.write_audiofile(r'E:\vid1.mp3')
