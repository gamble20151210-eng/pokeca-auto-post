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

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(URL)

    time.sleep(5)

    singles = []
    boxes = []

    single_items = driver.find_elements(By.CSS_SELECTOR, "#single-ranking li")
    for item in single_items[:30]:
        name = item.find_element(By.CSS_SELECTOR, ".name").text
        price = item.find_element(By.CSS_SELECTOR, ".price").text
        volume = item.find_element(By.CSS_SELECTOR, ".volume").text
        singles.append((name, price, volume))

    box_items = driver.find_elements(By.CSS_SELECTOR, "#box-ranking li")
    for item in box_items[:10]:
        name = item.find_element(By.CSS_SELECTOR, ".name").text
        price = item.find_element(By.CSS_SELECTOR, ".price").text
        volume = item.find_element(By.CSS_SELECTOR, ".volume").text
        boxes.append((name, price, volume))

    driver.quit()
    return singles, boxes
