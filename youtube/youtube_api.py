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
    print("https://www.youtube.com/results?search_query=" + query)
    # print(query)
    # html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + quote(query))
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
    
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    # print(len(video_ids))
    video_ids = video_ids[:10]
    jsonStr = json.dumps(video_ids)
    return jsonStr
    # print(video_ids)
    

app = Flask(__name__, static_url_path="")
   
@app.route("/youtube/", methods=['GET'])
def get_id():
    name = request.args.get('name')
    return get_yt_id(name)


if __name__ == "__main__":
    app.debug = True
    app.run()


# usage
# example
# http://127.0.0.1:5000/youtube/?name=spider-man
# http://127.0.0.1:5000/youtube/?name=蜘蛛人

# when using space, using + instead
# http://127.0.0.1:5000/youtube/?name=蜘蛛人+無家日

