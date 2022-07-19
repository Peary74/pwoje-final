from asyncio import streams
from pytube import YouTube

video= YouTube('http://youtube.com/watch?v=9bZkp7q19f0')

print(video.streams.first().download())

# print(f"""
# Title: {video.title}
# Owner: {video.channel_id}
# Length: {video.length}
# Date Published: {video.publish_date}
# Rating: {video.rating}
# Views: {video.views}
# File Size: {video.filesize}
# """)



# stream = video.streams.get_by_resolution(144)
# stream.download()