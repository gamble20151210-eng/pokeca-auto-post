import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from fetch_data import fetch_all_market_data
from calculate_rate import calculate_rate
from generate_post import create_post_text
from post_to_x import post_to_x

def main():
    # 国内相場データ取得（スニダン＋メルカリ）
    top30_cards, top10_boxes = fetch_all_market_data()

    # 前日比計算（カード名で紐付け）
    rates = calculate_rate(top30_cards + top10_boxes)

    # 投稿文生成
    post = create_post_text(top30_cards, top10_boxes, rates)

    # X に投稿
    post_to_x(post)

if __name__ == "__main__":
    main()
