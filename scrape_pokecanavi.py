import requests
from bs4 import BeautifulSoup

RANKING_URL = "https://www.pokecanavi.jp/ranking"

def scrape_pokecanavi():
    html = requests.get(RANKING_URL).text
    soup = BeautifulSoup(html, "html.parser")

    singles, boxes = [], []

    # シングルカードランキング（仮セレクタ）
    for item in soup.select(".ranking-item")[:30]:
        name = item.select_one(".ranking-item-name").get_text(strip=True)
        price = item.select_one(".ranking-item-price").get_text(strip=True)
        volume = item.select_one(".ranking-item-volume").get_text(strip=True)
        singles.append((name, price, volume))

    # BOXランキング（仮セレクタ）
    for item in soup.select(".box-ranking-item")[:10]:
        name = item.select_one(".ranking-item-name").get_text(strip=True)
        price = item.select_one(".ranking-item-price").get_text(strip=True)
        volume = item.select_one(".ranking-item-volume").get_text(strip=True)
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
