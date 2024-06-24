#s24019
#実行が確認出来たら時間を表示させる「時計アプリ」を作ってみたいと思います。
#時計アプリはモジュール名「time_kadai.py」で作成します。
#時計アプリを使いやすくバージョンアップしていきます。

import datetime
import tkinter as tk  # GUIでアプリを作ることができるモジュール

#時間を処理する部分を関数で実装
def updata_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日　%H時%M分%S秒")
    
#現在の時刻を習得し、ラベルに表示する
    lbl.config(text=current_time)

#一秒後に関数を呼び出し、再び現在時刻を習得して常にラベルの表示が最新であるようにする
    root.after(1000, updata_time)

# Tkinterのウィンドウを作成
root = tk.Tk() #はじめのおまじない

#サブタイトルを設定する
root.title("現在の時間")

#テキストや画像を表示する
lbl = tk.Label()

#すでに作成されたラベルの表示内容やスタイルの設定や変更
lbl.config(text="",font=("Helvetica", 20))

#ラベルをウィンドウ内に設置する
lbl.pack()

#関数の呼び出し
updata_time()


root.mainloop() #終わりのおまじない 
