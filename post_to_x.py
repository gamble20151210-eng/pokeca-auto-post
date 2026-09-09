import os
import tweepy

def post_to_x(text):
    if not text.strip():
        print("投稿内容が空のためスキップしました。")
        return

    client = tweepy.Client(
        consumer_key=os.getenv("API_KEY"),
        consumer_secret=os.getenv("API_KEY_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )

    try:
        client.create_tweet(text=text)
        print("投稿完了！")
    except tweepy.errors.Unauthorized:
        print("401 Unauthorized: 投稿が拒否されました。内容または権限を確認してください。")
    except Exception as e:
        print(f"投稿中にエラーが発生しました: {e}")
