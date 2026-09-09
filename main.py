from scrape_pokeca_chart import scrape_pokeca_chart, build_post_text
from post_to_x import post_to_x

def main():
    results = scrape_pokeca_chart()
    text = build_post_text(results)
    print(text)  # デバッグ用
    post_to_x(text)

if __name__ == "__main__":
    main()
