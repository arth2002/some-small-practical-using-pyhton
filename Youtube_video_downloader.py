import pytube
from pytube import YouTube
video_url = input("Enter Video URL here:")
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
# video = youtube.streams.all() --> It will show all quality of video
# for i in video:
#     print(i)
video.download("C:/Users/arthp/OneDrive/Desktop/Extra")

'''
--> WE can get following information from video:
print(f"Title :{youtube.title}")
print(f"Vidoe ID:{youtube.video_id}")
print(f"Derscription:{youtube.description}")
print(f"Length:{youtube.length} Seconds")
print(f"Thumbnail_URL:{youtube.thumbnail_url}")
print(f"Views:{youtube.views}")
print(f"Rating:{youtube.rating}")
print(f"Is age restricted:{youtube.age_restricted}")

'''
