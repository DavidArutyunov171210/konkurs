from tkinter import *
from PIL import Image 
from PIL import ImageTk

from windiws_quest import showraven
from figure import figurf

w = 920
h = 600


win = Tk()
win.resizable(False, False)
win.title('Начало КвЕЕста')

# настроили фон окна
canvas = Canvas(win, width=w, height=h)
canvas.pack()
img = ImageTk.PhotoImage(Image.open('/Users/david/PycharmProjects/test/__pycache__/image/fone.png'))
canvas.create_image(w // 2, h // 2, image=img)

# поставили три кнопки в комнате
def door1com():
    figurf()

door1 = ImageTk.PhotoImage(Image.open('/Users/david/PycharmProjects/test/__pycache__/image/door1.png'))
btndoor1 = Button(image=door1,command=door1com)
btndoor1.place(x=404, y=18)

door2 = ImageTk.PhotoImage(Image.open('/Users/david/PycharmProjects/test/__pycache__/image/door2.png'))
btndoor2 = Button(image=door2)
btndoor2.place(x=256, y=318)

def door3com():

    showraven()

door3 = ImageTk.PhotoImage(Image.open('/Users/david/PycharmProjects/test/__pycache__/image/door3.png'))
btndoor3 = Button(image=door3, command=door3com)
btndoor3.place(x=555, y=293)

win.mainloop()
