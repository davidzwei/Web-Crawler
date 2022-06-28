import requests
import json
from flask import Flask, request
import re
import urllib.request
import urllib
from urllib.parse   import quote


def get_yt_id(name):
    name = str(name).split(" ")
    # print(name)
    query = '+'.join(str(quote(x)) for x in name)
    print(type(query))
    print(query)
    # print("https://www.youtube.com/results?search_query=" + query + "%E5%BD%B1%E8%A9%95&sp=CAM%253D")
    # print(query)
    print("https://www.youtube.com/results?search_query=" + query)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + (query))
    
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    # print(len(video_ids))
    # video_ids = video_ids[:5]
    print(video_ids)
    
        
get_yt_id("蜘蛛人 無家日")
get_yt_id("Spider-Man: No Way Home")
