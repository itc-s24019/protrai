import tkinter as tk

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
bin = tk.Button(text="PUSH")

lbl.pack()
bin.pack()
tk.mainloop()
