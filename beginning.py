from tkinter import *
from PIL import Image 
from PIL import ImageTk

from windiws_quest import showraven
from figure import figurf
from guess import guss

w = 920
h = 600

def door1com():
    figurf()
def door2com():
    showraven()

def door3com():
    guss()
    
win = Tk()
win.resizable(False, False)
win.title('Восточный дворец')

# настроили фон окна
canvas = Canvas(win, width=w, height=h)
canvas.pack()
img = ImageTk.PhotoImage(Image.open('__pycache__/project/fone.png'))
canvas.create_image(w // 2, h // 2, image=img)

# поставили три кнопки в комнате

door1 = ImageTk.PhotoImage(Image.open('__pycache__/project/door1.png'))
btndoor1 = Button(image=door1,command=door1com)
btndoor1.place(x=404, y=18)



door2 = ImageTk.PhotoImage(Image.open('__pycache__/project/door2.png'))
btndoor2 = Button(image=door2,command=door2com)
btndoor2.place(x=256, y=318)


door3 = ImageTk.PhotoImage(Image.open('__pycache__/project/door3.png'))
btndoor3 = Button(image=door3, command=door3com)
btndoor3.place(x=555, y=293)

win.mainloop()
