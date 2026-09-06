import requests
from bs4 import BeautifulSoup
import re

# -----------------------------
# スニダンランキング取得
# -----------------------------
def fetch_snkrdunk_rankings():
    card_url = "https://snkrdunk.com/brands/pokemon/categories/33"  # シングル
    box_url = "https://snkrdunk.com/brands/pokemon/categories/26"   # BOX

    def fetch_items(url, limit):
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")

        items = []
        for item in soup.select(".item-card"):
            name = item.select_one(".item-card__title")
            price = item.select_one(".item-card__price")

            if not name or not price:
                continue

            items.append({
                "name": name.get_text(strip=True),
                "snkrdunk_price": price.get_text(strip=True)
            })

            if len(items) >= limit:
                break

        return items

    top30_cards = fetch_items(card_url, 30)
    top10_boxes = fetch_items(box_url, 10)

    return top30_cards, top10_boxes


# -----------------------------
# メルカリ価格取得
# -----------------------------
def fetch_mercari_price(keyword, limit=20):
    url = f"https://jp.mercari.com/search?keyword={keyword}&status=sold"

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    prices = []

    for item in soup.select("mer-item-card"):
        price_tag = item.select_one(".item-price")
        if not price_tag:
            continue

        price_text = price_tag.get_text(strip=True)
        price_num = int(re.sub(r"\D", "", price_text))

        prices.append(price_num)

        if len(prices) >= limit:
            break

    if len(prices) == 0:
        return None

    return sum(prices) // len(prices)


# -----------------------------
# 国内相場まとめ（スニダン＋メルカリ）
# -----------------------------
def fetch_all_market_data():
    top30_cards, top10_boxes = fetch_snkrdunk_rankings()

    # メルカリ価格を付与
    for card in top30_cards:
        card["mercari_price"] = fetch_mercari_price(card["name"])

    for box in top10_boxes:
        box["mercari_price"] = fetch_mercari_price(box["name"])

    return top30_cards, top10_boxes
