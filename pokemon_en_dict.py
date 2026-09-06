import re

def parse_pokemon_table(text):
    """
    日本語名 → 英語名 の辞書を生成する
    """
    lines = text.split("\n")
    dictionary = {}

    jp = None
    en = None

    for line in lines:
        # 日本語名の抽出
        m_jp = re.search(r"\|

\[

\[(.*?)\]

\]

", line)
        if m_jp:
            jp = m_jp.group(1)
            continue

        # 英語名の抽出
        m_en = re.search(r"\|(?!lang=)([A-Za-z][A-Za-z0-9\s\.'-]+)$", line)
        if m_en:
            en = m_en.group(1)

        # 両方揃ったら辞書に追加
        if jp and en:
            dictionary[jp] = en
            jp = None
            en = None

    return dictionary


# ここにあなたが貼ったテキストを入れる
with open("pokemon_table.txt", "r", encoding="utf-8") as f:
    text = f.read()

pokemon_en_dict = parse_pokemon_table(text)

# 辞書を確認
for k, v in list(pokemon_en_dict.items())[:20]:
    print(k, "→", v)
