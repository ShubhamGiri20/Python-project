from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)
print("Title: ",yt.title)
print("Views: ",yt.views)
print("Length: ",yt.length)
s = yt.filesize // 1000000
print("Download Size: ",s)
yd = yt.streams.get_highest_resolution()
yd.download(r'C:\Users\aniru\OneDrive\Code\PYTHON\Games\Image')