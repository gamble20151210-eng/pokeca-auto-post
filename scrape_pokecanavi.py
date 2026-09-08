import requests
from bs4 import BeautifulSoup

URL = "https://www.pokecanavi.jp/ranking"

def scrape_pokecanavi():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
    }

    html = requests.get(URL, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    singles = []
    boxes = []

    # シングルランキング
    for item in soup.select("#single-ranking li")[:30]:
        name = item.select_one(".name").get_text(strip=True)
        price = item.select_one(".price").get_text(strip=True)
        volume = item.select_one(".volume").get_text(strip=True)
        singles.append((name, price, volume))

    # BOXランキング
    for item in soup.select("#box-ranking li")[:10]:
        name = item.select_one(".name").get_text(strip=True)
        price = item.select_one(".price").get_text(strip=True)
        volume = item.select_one(".volume").get_text(strip=True)
        boxes.append((name, price, volume))

    return singles, boxes


def build_post_text(singles, boxes):
    text = "【ポケカ相場速報（直近72時間）】\n\n"

    text += "▼シングル取引数TOP30\n"
    for i, (name, price, volume) in enumerate(singles, 1):
        text += f"{i}. {
