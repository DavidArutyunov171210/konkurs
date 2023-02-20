from tkinter import *
from PIL import Image
from PIL import ImageTk

w = 920
h = 600


def door3com():
    win.destroy()
    room1 = Tk()
    room1.resizable(False, False)
    room1.geometry('1080x720+100+100')

    room1['bg'] = 'gray22'

    text1 = Label(
        text='Выберете все правильные математические равенства.\n(Если равенство верно , то при нажатии кнопка пропадет)\n(Правельных равенств ровно 3) ',
        fg='white', background='gray22', font='Arial 30')
    text1.pack()

    # Buttons
    button1 = Button(room1, textvariableы='2+2=4',font='Arial 20', fg='black')
    button1.place(x=200, y=100)

    button2 = Button(room1, text='6*6=36')
    button2.place()

    button3 = Button(room1, text='4^2=16')
    button3.place()
    # -----------------------------------------------------------------
    button3 = Button(room1, text='99+8=108')
    button3.place()

    button4 = Button(room1, text='3+3=7')
    button4.place()

    button5 = Button(room1, text='3+3>3*2')
    button5.place()

    button6 = Button(room1, text='7*8=65')
    button6.pack()

    room1.mainloop()


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
