# Ver1.2（公開用コード）
# ------------------

#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import urllib.request
import re
import requests
import time

# ---------- 使用環境に応じて変更 ----------
webhook_url = "自分のwebhookURL"
DEVELOPER_KEY = "YoutubeのAPIキー"
filename = "IDlist.txt"
# ファイル名は自由。確認したいYoutubeチャンネルのIDを一行ごとに記入したテキストファイルを同じ階層に置く
# ---------- ここまで ----------

def youtube_search(ID, DEVELOPER_KEY):
    # チャンネル登録者数取得部
    url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + str(ID) + "&key=" + str(DEVELOPER_KEY)
    res = urllib.request.urlopen(url)
    data = json.loads(res.read().decode("utf-8"))
    for item in data["items"]:
        global subscriber
        subscriber = item["statistics"].get("subscriberCount")
    # チャンネル名取得部
    url2 = "https://www.googleapis.com/youtube/v3/channels?part=snippet&id=" + str(ID) + "&key=" + str(DEVELOPER_KEY)
    res2 = urllib.request.urlopen(url2)
    data2 = json.loads(res2.read().decode("utf-8"))
    for item2 in data2["items"]:
        global title
        title = item2["snippet"].get("title")

# コメント送信部
def send_discord(channel,comment):
    # メッセージを変更したい場合はcontentを編集
    content = str(channel) + "のチャンネル登録者数は現在約" + str(comment) + "名です。"
    payload ={"content": content}
    result =requests.post(webhook_url, data=payload)

def main():
    with open(filename,"r") as file:
        for ID in file.read().splitlines():
            youtube_search(ID, DEVELOPER_KEY)
            send_discord(title,subscriber)
            time.sleep(3) # 連打対策

if __name__ == "__main__":
    main()
