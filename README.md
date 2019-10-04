# Channels_Checker
It can check number of Youtube subscribers and post result at your Discord server.（Japanese）

Channels Checker
Youtubeのチャンネル登録者数をAPI経由で取得し、Webhookを通じてDiscordにポストします。
（WebhookURLが使用できればDiscordに限らず動くとは思いますがテストしてません）

必要モジュール:requests

使用方法
1.ポストしたいサーバーでウェブフックを作成する。
サーバー設定が触れないと使えないので、作成できない場合はサーバー管理者に作ってもらう。
2.YoutubeのAPIキーを発行する。
取得にはこちらの記事 https://www.plusdesign.co.jp/blog/?p=7752　などを参考にして取得する。
3.チャンネル登録者数を確認したいユーザーのページに移動し、URLの"https://www.youtube.com/channel/"の後ろに来る部分をコピーし、
IDlist.txtに一行ずつ記入する。（例を参考に）
4.Channels_Checker.pyのウェブフックのURL、YoutubeのAPIキー、IDリストの場所を自身のものに置き換える。
5.Channels_Checker.pyを実行する。cron等を使って定時実行にすると便利。
