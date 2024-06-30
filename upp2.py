

import tkinter as tk

def dispLabel():
    lbl.config(text="こんにちは")
    
root = tk.Tk()

#
root.geometry("400x200")

#
lbl = tk.Label(text="LABEL", font=("Helvetica", 20))

#
btn = tk.Button(text="PUSH", command=dispLabel, font=("Helvetica", 20))

#
btn.pack()

#
lbl.pack()

lbl2 = tk.Label(text="ラベル2", font=("Helvetica", 20)).pack()

btn2 = tk.Button(text="何もしないボタン",command=dispLabel, font=("Helvetica", 20)).pack()

tk.mainloop()
