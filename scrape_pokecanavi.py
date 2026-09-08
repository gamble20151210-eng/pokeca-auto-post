import requests
from bs4 import BeautifulSoup

RANKING_URL = "https://www.pokecanavi.jp/ranking"

def scrape_pokecanavi():
    html = requests.get(RANKING_URL).text
    soup = BeautifulSoup(html, "html.parser")

    # シングルカードランキング
    single_items = soup.select(".ranking-list .ranking-item")
    singles = []

    for item in single_items[:30]:
        name = item.select_one(".card-name").get_text(strip=True)
        price = item.select_one(".price").get_text(strip=True)
        volume = item.select_one(".volume").get_text(strip=True)
        singles.append((name, price, volume))

    # BOXランキング
    box_items = soup.select(".box-ranking-list .ranking-item")
    boxes = []

    for item in box_items[:10]:
        name = item.select_one(".card-name").get_text(strip=True)
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
