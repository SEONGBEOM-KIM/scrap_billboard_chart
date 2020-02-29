import csv
import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100"


def get_music_info():
    html = requests.get(URL)
    soup = BeautifulSoup(html.text, "html.parser")
    boxes = soup.find_all("button", {"class": "chart-element__wrapper"})
    chart_list = []
    for box in boxes:
        rank = box.find(
            "span", {"class": "chart-element__rank__number"}).get_text()
        song = box.find(
            "span", {"class": "chart-element__information__song"}).get_text()
        artist = box.find(
            "span", {"class": "chart-element__information__artist"}).get_text()
        chart = {"rank": rank, "song": song, "artist": artist}
        chart_list.append(chart)
    return chart_list


def save_to_file(infos):
    file = open("billboard.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["rank", "song", "artist"])
    for info in infos:
        writer.writerow(list(info.values()))


def extract_music_info():
    music_info = get_music_info()
    save_to_file(music_info)


extract_music_info()
