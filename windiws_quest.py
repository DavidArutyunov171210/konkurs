from tkinter import *
from figure import figurf
from guess import  guss

right_answers=0
wrong_answers=0
counter =0
def showraven():
  
           
    room1 = Toplevel()
    room1.title('Равенства')
    room1.resizable(False, False)
    room1.geometry('1080x720+100+100')
    
    def result():
        if counter >=3:
            if right_answers==3 and wrong_answers==0:
                def correctDef():
                    figurf()
                correct=Button(room1,text='Ты победил',command=correctDef,font='Arial 50')
                correct.place(x=500,y=600)
                # room1.destroy()
            else:
                room1.destroy()
                guss()

    
    def b1():
        global right_answers,counter
        right_answers+=1
        counter +=1
        button1.place_forget()
        result()
    def b2():
        global right_answers,counter
        right_answers+=1
        counter+=1
        button2.place_forget()
        result()
    def b3():
        global right_answers,counter
        right_answers+=1
        counter+=1
        button3.place_forget()
        result()
    def b4():
        global wrong_answers,counter
        wrong_answers+=1
        counter+=1
        button4.place_forget()
        result()
    def b5():
        global wrong_answers,counter
        wrong_answers+=1
        counter+=1
        button5.place_forget()
        result()
    def b6():
        global wrong_answers,counter
        wrong_answers+=1
        counter +=1
        button6.place_forget()
        result()

   
    room1['bg'] = 'gray22'

    text1 = Label(
        room1,
        text='Выберете все правильные математические равенства.\n(Если равенство верно , то при нажатии кнопка пропадет)\n(Правельных равенств ровно 3) ',
        fg='white', background='gray22', font='Arial 30')
    text1.pack()

    # Buttons
    button1 = Button(room1, text='2+2=4', fg='black', font='Arial 20', command=b1)
    button1.place(x=300, y=200)

    button2 = Button(room1, text='6*6=36', fg='black', font='Arial 20', command=b2)
    button2.place(x=300, y=400)

    button3 = Button(room1, text='4^2=16', fg='black', font='Arial 20', command=b3)
    button3.place(x=500, y=200)
    # -----------------------------------------------------------------
    button4 = Button(room1, text='99+8=108', fg='black', font='Arial 20', command=b4)
    button4.place(x=500, y=400)

    button5 = Button(room1, text='3+3=7', fg='black', font='Arial 20', command=b5)
    button5.place(x=700, y=200)

    button6 = Button(room1, text='3+3>3*2', fg='black', font='Arial 20', command=b6)
    button6.place(x=700, y=400)

    room1.mainloop()


if __name__ == '__main__':
    showraven()

