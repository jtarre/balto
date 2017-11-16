import requests
import time
from bs4 import BeautifulSoup


playlists='playlists.txt'
talks='talks.txt'

f=open(playlists,'r')
output=open(talks,'w')
for row in f:
    print(row)
# fix insecure platform error with requests library.
# https://stackoverflow.com/questions/29099404/ssl-insecureplatform-error-when-using-requests-package
    result = requests.get(row)
    content = result.content
    soup = BeautifulSoup(content, "html.parser")
    print(soup.title.string)

    # Get links
    links = soup.find_all('a', class_="ga-link playlist-talks__play playlist-talks__thumb")
    for link in links:
        output.write(link['href'])
        output.write("\n")
    	print(link['href'])
    time.sleep(1.5)
output.close()
f.close()
    # links2 = soup.find_all('a')
    # # print(links2)
    # for link in links2:
    #     print(link)
