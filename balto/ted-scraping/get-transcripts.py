import requests
import time
import re
from bs4 import BeautifulSoup
import sqlite3


talkstxt="talks.txt"
talks=open(talkstxt, 'r')

for talk in talks:
    talkclean = re.sub("\n","", talk)
    transcript="https://www.ted.com" + talkclean + "/transcript?language=en"
    print(transcript)
    result = requests.get(transcript)
    content = result.content
    soup = BeautifulSoup(content, "html.parser")
    talktxt = re.sub("/talks/","", talkclean)
    talktxt = talktxt + ".txt"
    print(talktxt)
    talkfile = open("transcripts/" + talktxt, "w+")
    talkfile.write(soup.title.string + "    " + talkclean)
    talkfile.close()
    print(soup.title.string)
    time.sleep(1.5)
talks.close()