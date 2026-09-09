from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://pokeca-chart.com/all-card/?sort=rise7"

def scrape_pokeca_chart():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(URL)
    time.sleep(8)  # JS描画待ち

    results = []
    cards = driver.find_elements(By.CSS_SELECTOR, "div.flex.flex-col.items-center")

    for card in cards[:10]:
        try:
            name = card.find_element(By.CSS_SELECTOR, "p.text-sm.font-bold").text
            price = card.find_element(By.CSS_SELECTOR, "p.text-xs.text-gray-700").text
            rise = card.find_element(By.CSS_SELECTOR, "p.text-xs.text-green-600").text
            results.append((name, price, rise))
        except Exception:
            continue

    driver.quit()
    return results


def build_post_text(results):
    if not results:
        return "【ポケカ値上がりランキング（直近7日）】\n\nデータ取得に失敗しました。\n#ポケカ #ポケカ相場"

    text = "【ポケカ値上がりランキング（直近7日）】\n\n"
    for i, (name, price, rise) in enumerate(results, 1):
        text += f"{i}. {name}（{price} / {rise}）\n"
    text += "\n#ポケカ #ポケカ相場 #ポケカ高騰"
    return text
