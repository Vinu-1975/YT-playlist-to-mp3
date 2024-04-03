from pytube import Playlist,YouTube
from moviepy.editor import AudioFileClip

p = Playlist('https://www.youtube.com/playlist?list=PLfPsb_5VpqQOHzTJuROx_4jLMou5TOccW')

print(f'Downloading: {p.title}')
# print(p.videos)
for url in p.video_urls:
    yt = YouTube(url)
    # video = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
    audio = yt.streams.filter(only_audio=True).first()
    audio_file = audio.download(output_path='Audio/')
    mp4_audio = AudioFileClip(audio_file)
    mp3_audio = mp4_audio.write_audiofile(audio_file.replace('.mp4','.mp3'))
    mp4_audio.close()
    print("Done : ",yt.title)

print("All Done")


#### if you want to delete mp4 files uncomment this
# import os

# def delete_mp4_files(folder_path):
#     for file in os.listdir(folder_path):
#         if file.endswith(".mp4"):
#             os.remove(os.path.join(folder_path, file))
#             print(f"Deleted: {file}")


# audio_folder = "Audio"
# delete_mp4_files(audio_folder)
