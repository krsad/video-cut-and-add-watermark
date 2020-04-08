import moviepy.editor as mp
import sys
from moviepy.editor import *



start_time = int(sys.argv[1])
end_time = int(sys.argv[2])
mp4_name = sys.argv[3]
output_name = sys.argv[4]



video = mp.VideoFileClip(mp4_name).subclip(start_time,end_time)
#video = VideoFileClip("") # 2.
logo = (mp.ImageClip("logo.png")
          .set_duration(end_time-start_time)
          .resize(height=50) # if you need to resize...
          .margin(right=8, bottom=8, opacity=0) # (optional) logo-border padding
          .set_pos(("left","bottom")))


audio = video.audio
final = mp.CompositeVideoClip([video, logo]).set_audio(audio)
mp3_name = "mp3_name.mp3"
audio.write_audiofile(mp3_name)
final = final.set_audio(audio.set_duration(19))
final.write_videofile("output.mp4")

new_string = "ffmpeg -i output.mp4 -i "  + mp3_name + " -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 "+output_name

os.system(new_string)

os.remove(mp3_name)




