# Date: 9 Sep. 2022
# !/usr/bin/python
# Author: hyper

from keyword import kwlist
import pytube
import math
from progress.bar import Bar 
import time
from simple_term_menu import TerminalMenu

videoSize = 0
oldProgress = 0

def progress_function(stream, chunk, bytes_remaining):
    global bar
    global oldProgress
    progress = float(abs(bytes_remaining-stream.filesize)/stream.filesize)*float(100)
    for i in range(int(progress -oldProgress)):
        time.sleep(0.05)
        bar.next()
    oldProgress = progress

url = input("Enter video url: ")
client = pytube.YouTube(url=url, on_progress_callback=progress_function)
bar = Bar('Downloading', max=100)
streams = client.streams

resolution =[str(i.split("nothing")[0]) for i in (list(dict.fromkeys([i.resolution for i in client.streams if i.resolution])))]
resolution.sort()

try:
    while True:
        resolutionMenu = TerminalMenu(resolution)
        selectedResolution = resolutionMenu.show()
        try:
            streams.get_by_resolution(resolution[selectedResolution]).download()
            needed = 100 - oldProgress
            bar.goto(100)
            break
        except:
            print("An error occured, try again.")
except KeyboardInterrupt:
    pass