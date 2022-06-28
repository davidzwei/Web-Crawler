import requests
from bs4 import BeautifulSoup 
import time
import json
import re
import numpy as np
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

def search_animate(name):
    #return animattion dictionary
    animate = {}
    url = "https://ani.gamer.com.tw/search.php?kw="+name
    print(url)
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"})
    soup = BeautifulSoup(r.text,"html.parser")
    theme = soup.find('div', 'theme-list-block')
    list = theme.find_all('a', 'theme-list-main')

    #finding
    # print(len(list))
    if(len(list) == 0):
        nothing = {}
        # print('not-found')
        return nothing
    else:
        # print("exist")
        #name
        title = []
        infoblock = theme.find_all('p', 'theme-name')
        # print(len(infoblock))
        # infoblock
        for i in infoblock:
            x = i.getText()
            title.append(x)

        #images
        images = []
        for i in list:
            part = i.find('img')
            images.append(part.get("src"))

        #address
        address = []
        for a in list:
            address.append(a['href'])
        new_url = address[0]

        #view
        view = []
        for b in list:
            view.append(b.find('p').getText())

        #update
        animate['name'] = title[0]
        # animate['address'] = new_url
        animate['img'] = images[0]
        animate['view'] = view[0]

        des_url = "https://ani.gamer.com.tw/"+new_url
        # print(des_url)
        r = requests.get(des_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"})
        soup1 = BeautifulSoup(r.text,"html.parser")

        # intro
        intro = soup1.find('div', 'data_intro')
        intro_p = intro.find('p')
        introduction = intro_p.getText()
        intro = introduction.replace('\r', '')
        intro = intro.replace(' ', '')
        # print(intro)

        # score 
        score = soup1.find('div', 'score-overall-number').getText()
        # score = float(score)

        #type
        datatype = soup1.find('ul', 'data_type')
        category = datatype.find('li').getText()

        #update
        animate['intro'] = intro
        animate['rank'] = score
        animate['type'] = category

        # print(animate['intro'])
        animate['intro'] = animate['intro'].replace(u'\u3000',u' ')
        print(animate)
        # df = pd.DataFrame.from_dict([animate])
        return animate
        #result to json
        # json_object = json.dumps(animate, indent = 4, ensure_ascii=False) 
        # print(json_object)
        # json_object.headers.add('Access-Control-Allow-Origin', '*')
        # return json_object


# search("zcxjvlkjmzldsxvml")

def insert_anime(name):
    anime = search_animate(name)
    if(len(anime) == 0):
        print("insert nothing")
    else:
        df = pd.DataFrame([anime]) #convert to df
        print(df)
    

insert_anime("進擊的巨人")

# app = Flask(__name__, static_url_path="")
# CORS(app)

# @app.route("/animate/", methods=['GET'])
# def animate():
#     name = request.args.get('name')
#     return search(name)

# if __name__ == "__main__":
#     app.debug = True
#     app.run()
