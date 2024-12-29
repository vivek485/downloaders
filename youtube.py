from curl_cffi import requests
from yt_dlp import YoutubeDL
path = '/home/vivek/softwares/tornet/'

url =input('url--')
with YoutubeDL({"outtmpl":'/home/vivek/softwares/tornet/%(funny)s.%(ext)s',
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best'})as ydl:
    ydl.download([url])




# from __future__ import unicode_literals
# import youtube_dl
#
# downloadLinks = []
#
# downloadLink = input('Link to download: ')
# downloadLinks.append(downloadLink)
#
# youtube_dl_options = {
#     "outtmpl": "%(title)s-%(id)s.%(ext)s",
#     "restrictfilenames": True,
#     "nooverwrites": True,
#     "writedescription": True,
#     "writeinfojson": True,
#     "writeannotations": True,
#     "writethumbnail": True,
#     "writesubtitles": True,
#     "writeautomaticsub": True,
#     'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best'
# }
#
# with youtube_dl.YoutubeDL(youtube_dl_options) as ydl:
#     ydl.download(downloadLinks)
