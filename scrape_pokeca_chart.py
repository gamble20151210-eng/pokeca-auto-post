import requests
from bs4 import BeautifulSoup

URL = "https://pokeca-chart.com/all-card/?sort=rise7"

def scrape_pokeca_chart():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
    }

    html = requests.get(URL, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    rows = soup.select("table tbody tr")

    results = []

    for row in rows[:10]:  # 上位10件だけ
        cols = row.select("td")
        if len(cols) < 4:
            continue

        name = cols[1].get_text(strip=True)
        price = cols[2].get_text(strip=True)
        rise7 = cols[3].get_text(strip=True)

        results.append((name, price, rise7))

    return results


def build_post_text(results):
    text = "【ポケカ値上がりランキング（直近7日）】\n\n"

    for i, (name, price, rise7) in enumerate(results, 1):
        text += f"{i}. {name}（{price} / {rise7}）\n"

    text += "\n#ポケカ #ポケカ相場 #ポケカ高騰"
    return text
