import requests

API_URL = "https://www.pokecanavi.jp/api/ranking"

def scrape_pokecanavi():
    data = requests.get(API_URL).json()

    singles = []
    boxes = []

    # シングルカードランキング
    for item in data["single"][:30]:
        name = item["name"]
        price = item["price"]
        volume = item["volume"]
        singles.append((name, price, volume))

    # BOXランキング
    for item in data["box"][:10]:
        name = item["name"]
        price = item["price"]
        volume = item["volume"]
        boxes.append((name, price, volume))

    return singles, boxes


def build_post_text(singles, boxes):
    text = "【ポケカ相場速報（直近72時間）】\n\n"

    text += "▼シングル取引数TOP30\n"
    for i, (name, price, volume) in enumerate(singles, 1):
        text += f"{i}. {name}（¥{price} / {volume}件）\n"

    text += "\n▼BOX取引数TOP10\n"
    for i, (name, price, volume) in enumerate(boxes, 1):
        text += f"{i}. {name}（¥{price} / {volume}件）\n"

    return text
