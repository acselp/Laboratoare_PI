from tkinter import *
from tkhtmlview import *
import tkinter as tk

root = Tk()

root['bg'] = '#fff'
root.title('Piatra foarfece hartie')
root.geometry("1280x720")

mainLabel = HTMLLabel(root, html="<img src='./img/Bg.jpg' width='1280' height='720'>")
mainLabel.pack(pady=0, padx=0,fill="both", expand='True')


startBtn = Button(mainLabel, text="Start")
quitBtn = Button(mainLabel, text="Quit")
titleLabel = Label(mainLabel, text="Foarfece Hartie Piatra")


startBtn.place(x="603", y="380", width="75", height="40")
quitBtn.place(x="603", y="340", width="75", height="40")
titleLabel.place(x="582", y="75")

root.mainloop()