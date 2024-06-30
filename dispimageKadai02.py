# dispimageKadai02.py
#dispImageをグレートスケールに変換して、90度回転させ、水平方向に反転させ、メソッドで画像サイズを調整するアレンジ。

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    #画像を読み込んでモザイクに変換
    newImage = PIL.Image.open(path).convert("L").rotate(90).transpose(PIL.Image.FLIP_LEFT_RIGHT).resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)
        lbl = tk.Label(text=fpath)
        lbl.pack()

root =tk.Tk()
root.geometry("400x500")#画面の大きさを決める

lbl = tk.Label(text="画像表示アプリ　バージョン2.0")
btn = tk.Button(text="ファイルを開く",command=openFile)
imageLabel=tk.Label()

lbl.pack()
btn.pack()
imageLabel.pack()

tk.mainloop()
