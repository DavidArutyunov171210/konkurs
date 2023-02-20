from tkinter import *
from PIL import Image
from PIL import ImageTk
from windiws_quest import showraven
w = 920
h = 600


def door3com():
    win.destroy()

    showraven()


win = Tk()
win.resizable(False, False)
win.title('Начало КвЕЕста')

# настроили фон окна
canvas = Canvas(win, width=w, height=h)
canvas.pack()
img = ImageTk.PhotoImage(Image.open('fone.png'))
canvas.create_image(w // 2, h // 2, image=img)

# поставили три кнопки в комнате
door1 = ImageTk.PhotoImage(Image.open('door1.png'))
btndoor1 = Button(image=door1)
btndoor1.place(x=404, y=18)

door2 = ImageTk.PhotoImage(Image.open('door2.png'))
btndoor2 = Button(image=door2)
btndoor2.place(x=256, y=318)

door3 = ImageTk.PhotoImage(Image.open('door3.png'))
btndoor3 = Button(image=door3, command=door3com)
btndoor3.place(x=555, y=293)

win.mainloop()
