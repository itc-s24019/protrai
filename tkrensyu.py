# GUIで動くアプリを作ってみるよ

import tkinter as tk #まずこの行を書く必要があるよ

root= tk.Tk() #はじめのおまじない


root.geometry("500x500")
root.title("ハローアプリ")#ウィンドウズのタイトルを決める
lbl =tk.Label(text="こんにちは世界") #いつもの
lbl.pack()#lblを配置させる必要があるよ





root.mainloop() #終わりのおまじない
