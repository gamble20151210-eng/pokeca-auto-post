from scrape_pokecanavi import scrape_pokecanavi, build_post_text
from post_to_x import post_to_x

def main():
    singles, boxes = scrape_pokecanavi()
    text = build_post_text(singles, boxes)
    post_to_x(text)

if __name__ == "__main__":
    main()
