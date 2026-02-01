#习近平 talks crawler

import httpx
import lxml.html
import time
import json
import pprint
from pathlib import Path

def crawler():

    """"
    Crawls for talks given by Xi Jin Ping

    """

    talks_repo = []

    url = "https://www.xinhuanet.com/politics/leaders/xijinping/jhqw.htm"

    time.sleep(0.5)
    response = httpx.get(url)

    root = lxml.html.fromstring(response.text)

    talks = root.cssselect("a")

    #Just grabbing the talks we want:
    talks = talks[51:]

    for talk in talks:

        talk_dict = {}

        talk_dict["Title"] = talk.text_content()
        talk_dict["url"] = talk.get("href")
        talks_repo.append(talk_dict)


    for talk in talks_repo:

        print(f"=========Crawling through {talk["url"]}=========")

        talk_response = httpx.get(talk["url"])
        talk_root = lxml.html.fromstring(talk_response.text)
        talk_content = talk_root.cssselect("p")

        text_body = ""

        for paragraph in talk_content:

            text_body += paragraph.text_content()
        
        talk["text"] = text_body

        print(f"=========Talk: {talk["Title"]}===========")
        pprint.pprint(talk)