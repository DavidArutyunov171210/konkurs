from tkinter import *

counter = 0


def showraven():
    def button1def():
        global counter
        counter += 1
        button1.place_forget()
        ifcounter()

    def button2def():
        global counter
        counter += 1
        button2.place_forget()
        ifcounter()

    def button3def():
        global counter
        counter += 1
        button3.place_forget()
        ifcounter()

    def ifcounter():
        if counter == 0:
            counter == 0
        elif counter == 3:
            
            next = Button(room1, text='Дальше', font='Arial 50')
            next.place(x=700, y=600)

    def dalshedef():
        end1 = Tk()
        end1.mainloop()

    room1 = Tk()
    room1.resizable(False, False)
    room1.geometry('1080x720+100+100')

    room1['bg'] = 'gray22'

    text1 = Label(
        room1,
        text='Выберете все правильные математические равенства.\n(Если равенство верно , то при нажатии кнопка пропадет)\n(Правельных равенств ровно 3) ',
        fg='white', background='gray22', font='Arial 30')
    text1.pack()

    # Buttons
    button1 = Button(room1, text='2+2=4', fg='black', font='Arial 20', command=button1def)
    button1.place(x=300, y=200)

    button2 = Button(room1, text='6*6=36', fg='black', font='Arial 20', command=button2def)
    button2.place(x=300, y=400)

    button3 = Button(room1, text='4^2=16', fg='black', font='Arial 20', command=button3def)
    button3.place(x=500, y=200)
    # -----------------------------------------------------------------
    button4 = Button(room1, text='99+8=108', fg='black', font='Arial 20')
    button4.place(x=500, y=400)

    button5 = Button(room1, text='3+3=7', fg='black', font='Arial 20')
    button5.place(x=700, y=200)

    button6 = Button(room1, text='3+3>3*2', fg='black', font='Arial 20')
    button6.place(x=700, y=400)

    room1.mainloop()


if __name__ == '__main__':
    showraven()

    
