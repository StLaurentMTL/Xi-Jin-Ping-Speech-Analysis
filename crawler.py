# 习近平 talks crawler

import httpx
import lxml.html
import time
import json
import pprint
import csv
from pathlib import Path

SAVE_PATH = Path()

speeches_filepath_json = SAVE_PATH / "speeches.json"
speeches_filepath_csv = SAVE_PATH / "speeches.csv"

HEADERS = ["publication", "title", "url", "text"]


def crawler():
    """ "
    Crawls for public talks given by Xi Jinping published on state news agency
    Xinhua from 2022 to 2026

    """

    speeches_repo = []

    url = "https://www.xinhuanet.com/politics/leaders/xijinping/ds_3f92a99f87704592957a7478f07111c7.json"

    time.sleep(0.5)
    response = httpx.get(url)
    speeches = response.json()

    # Grabbing urls, speech titles, and date of publication
    for speech in speeches["datasource"]:
        speech_dict = {}

        speech_dict["url"] = speech["publishUrl"]
        speech_dict["publication"] = speech["publishTime"]
        speech_dict["title"] = (
            speech["title"].split(">", 1)[1].rsplit("<", 1)[0].strip()
        )

        speeches_repo.append(speech_dict)

    # Grabbing text corpus
    for speech in speeches_repo:
        time.sleep(0.5)
        speech_response = httpx.get(speech["url"])
        speech_root = lxml.html.fromstring(speech_response.text)
        speech_content = speech_root.cssselect("p")

        text_body = ""

        for paragraph in speech_content:
            text_body += paragraph.text_content()

        speech["text"] = text_body

    # JSON file save
    with open(speeches_filepath_json, "w", encoding="utf-8") as json_file:
        json.dump(speeches_repo, json_file, indent=1, ensure_ascii=False)

    # CSV file save
    with open(speeches_filepath_csv, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, HEADERS)
        writer.writeheader()
        writer.writerows(speeches_repo)
