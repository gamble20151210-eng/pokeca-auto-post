import requests
from bs4 import BeautifulSoup

RANKING_URL = "https://www.pokecanavi.jp/ranking"

def scrape_pokecanavi():
    html = requests.get(RANKING_URL).text
    soup = BeautifulSoup(html, "html.parser")

    singles, boxes = [], []

    # シングルカードランキング
    single_items = soup.select("div#single-ranking ul li")
    for item in single_items[:30]:
        name = item.select_one(".name").get_text(strip=True)
        price = item.select_one(".price").get_text(strip=True)
        volume = item.select_one(".volume").get_text(strip=True)
        singles.append((name, price, volume))

    # BOXランキング
    box_items = soup.select("div#box-ranking ul li")
    for item in box_items[:10]:
        name = item.select_one(".name").get_text(strip=True)
        price = item.select_one(".price").get_text(strip=True)
        volume = item.select_one(".volume").get_text(strip=True)
        boxes.append((name, price, volume))

    return singles, boxes


def build_post_text(singles, boxes):
    text = "【ポケカ相場速報（直近72時間）】\n\n"

    text += "▼シングル取引数TOP30\n"
    for i, (name, price, volume) in enumerate(singles, 1):
        text += f"{i}. {name}（{price} / {volume}件）\n"

    text += "\n▼BOX取引数TOP10\n"
    for i, (name, price, volume) in enumerate(boxes, 1):
        text += f"{i}. {name}（{price} / {volume}件）\n"

    return text

import requests
from bs4 import BeautifulSoup

RANKING_URL = "https://www.pokecanavi.jp/ranking"

def scrape_pokecanavi():
    html = requests.get(RANKING_URL).text

    # ★ まずは HTML を確認する（最短ルート）
    print(html[:2000])  # 最初の2000文字だけ表示

    soup = BeautifulSoup(html, "html.parser")

    return [], []  # 一旦空で返す

import requests

html = requests.get("https://www.pokecanavi.jp/ranking").text
print(html[:5000])
