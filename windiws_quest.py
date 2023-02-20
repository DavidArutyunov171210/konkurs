from tkinter import *


def showraven():
    room1 = Toplevel()
    room1.resizable(False, False)
    room1.geometry('1080x720+100+100')

    room1['bg'] = 'gray22'

    text1 = Label(
        text='Выберете все правильные математические равенства.\n(Если равенство верно , то при нажатии кнопка пропадет)\n(Правельных равенств ровно 3) ',
        fg='white', background='gray22', font='Arial 30')
    text1.pack()

    # Buttons
    button1 = Button(room1, text='2+2=4', fg='black')
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
showraven()
