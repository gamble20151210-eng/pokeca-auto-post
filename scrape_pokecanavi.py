from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://www.pokecanavi.jp/ranking"

def scrape_pokecanavi():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/bin/chromium-browser"

    # ★ GitHub Actions で正しく動く ChromeDriver の起動方法
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        options=options
    )

    driver.get(URL)
    time.sleep(5)

    singles = []
    boxes = []

    # シングルランキング
    single_items = driver.find_elements(By.CSS_SELECTOR, "#single-ranking li")
    for item in single_items[:30]:
        name = item.find_element(By.CSS_SELECTOR, ".name").text
        price = item.find_element(By.CSS_SELECTOR, ".price").text
        volume = item.find_element(By.CSS_SELECTOR, ".volume").text
        singles.append((name, price, volume))

    # BOXランキング
    box_items = driver.find_elements(By.CSS_SELECTOR, "#box-ranking li")
    for item in box_items[:10]:
        name = item.find_element(By.CSS_SELECTOR, ".name").text
        price = item.find_element(By.CSS_SELECTOR, ".price").text
        volume = item.find_element(By.CSS_SELECTOR, ".volume").text
        boxes.append((name, price, volume))

    driver.quit()
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
