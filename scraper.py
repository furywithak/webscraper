from bs4 import BeautifulSoup
import requests
import urllib

"""
Youtube API
    
"""
youtube_live = "https://www.youtube.com/watch?v=xd45_GYjjn0"


# page = requests.get(youtube_live)
pages = urllib.urlopen(youtube_live)
youtube_page = BeautifulSoup(pages)
print(youtube_page.prettify())

# youtube_page = BeautifulSoup(page.content, "html.parser")
#
# #print(youtube_page.prettify())
# comments = youtube_page.find_all("div", class_="fyre-comment-count")
# print (comments)
