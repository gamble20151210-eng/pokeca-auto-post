def create_post_text(top30_cards, top10_boxes, rates):
    """
    国内相場データ（スニダン＋メルカリ）を使って投稿文を生成する
    top30_cards: スニダンTOP30（メルカリ価格付与済み）
    top10_boxes: スニダンBOX TOP10（メルカリ価格付与済み）
    rates: 前日比データ（calculate_rate.py）
    """

    # -----------------------------
    # シングルカード TOP30
    # -----------------------------
    post = "【AIホタテのポケカ相場速報｜国内相場まとめ】\n"
    post += "📅 本日のシングルカード相場 TOP30\n"
    post += "※価格はスニダン・メルカリ等の参考値\n\n"

    for i, card in enumerate(top30_cards, 1):
        name = card["name"]
        snkr = card["snkrdunk_price"]
        merc = card["mercari_price"] or "---"
        rate = rates.get(name, 0)

        post += f"{i}位：{name}（平均 {merc}円／前日比 {rate:+.1f}%）\n"

    post += "\n"

    # -----------------------------
    # BOX TOP10
    # -----------------------------
    post += "📦 本日のBOX相場 TOP10\n\n"

    for i, box in enumerate(top10_boxes, 1):
        name = box["name"]
        snkr = box["snkrdunk_price"]
        merc = box["mercari_price"] or "---"
        rate = rates.get(name, 0)

        post += f"{i}位：{name}（平均 {merc}円／前日比 {rate:+.1f}%）\n"

    post += "\n"

    # -----------------------------
    # AIホタテの一言
    # -----------------------------
    post += (
        "🐚 AIホタテの一言：\n"
        "今日も相場が大きく動いてるみたい。\n"
        "気になるカードやBOXは早めにチェックしておこう✨\n\n"
        "#ポケカ相場速報 #AIホタテ #ポケモンカード\n"
    )

    return post
