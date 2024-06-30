# dispImageGrey.py
#モノクロ画像に変換
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).covert("L").resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)

root =tk.Tk()
root.geometry("400x200")#画面の大きさを決める

lbl = tk.Label(text="画像表示アプリ　バージョン2.0")
btn = tk.Button(text="ファイルを開く",command=openFile)
imageLabel=tk.Label()

lbl.pack()
btn.pack()
imageLabel.pack()

tk.mainloop()
