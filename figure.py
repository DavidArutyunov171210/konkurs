#5,1,2,3,1,4,3,5,4

from tkinter import *
from tkinter import messagebox
line_button1=-1
line_button2=-1
def figurf():
    

    size=20
    lines=['12','13','14','15','23','34','35','45']
    def chek_line(btn1, btn2):
        a = btn1.cget('text')
        b=btn2.cget('text')

        line = a+b
        print(line)
        if line in lines:
            return True
        line = b+a
        print('1',line)
        if line in lines:
            return True
        else:
            return False

    def click_button1():
        
        global line_button1,line_button2
        if line_button1==-1:
            line_button1=button1
            line_button1.config(bg='red')
        else:
            line_button2=button1
            if chek_line(line_button1,line_button2):
                print(132)
                line(line_button1,line_button2)
                line_button1=line_button2
                line_button2=-1
            else:
                print('НЕ ЗЯ')
                messagebox.Message('так незя')
            

    def click_button2():
        global line_button1,line_button2
        if line_button1==-1:
            line_button1=button2
        else:
            line_button2=button2
            line(line_button1,line_button2)
            line_button1=line_button2
            line_button2=-1

    def click_button3():
        global line_button1,line_button2
        if line_button1==-1:
            line_button1=button3
        else:
            line_button2=button3
            line(line_button1,line_button2)
            line_button1=line_button2
            line_button2=-1

    def click_button4():
        global line_button1,line_button2
        if line_button1==-1:
            line_button1=button4
        else:
            line_button2=button4
            line(line_button1,line_button2)
            line_button1=line_button2
            line_button2=-1

    def click_button5():
        global line_button1,line_button2
        if line_button1==-1:
            line_button1=button5
        else:
            line_button2=button5
            line(line_button1,line_button2)
            line_button1=line_button2
            line_button2=-1

    def line(b1,b2):
        x1=b1.winfo_x()+size
        y1=b1.winfo_y()+size
        x2=b2.winfo_x()+size
        y2=b2.winfo_y()+size
        

        canvas.create_line(x1,y1,x2,y2)
        

    room3=Toplevel()

    canvas=Canvas(room3,width=1000,height=1000)
    button1=Button(canvas,text='1',font='Arial 50',command=click_button1)
    button1.place(x=300,y=300)
    button2=Button(canvas,text='2',font='Arial 50',command=click_button2)
    button2.place(x=450,y=100)
    button3=Button(canvas,text='3',font='Arial 50',command=click_button3)
    button3.place(x=600,y=300)
    button4=Button(canvas,text='4',font='Arial 50',command=click_button4)
    button4.place(x=600,y=600)
    button5=Button(canvas,text='5',font='Arial 50',command=click_button5)
    button5.place(x=300,y=600)

    canvas.pack()
    room3.mainloop()

if __name__ == '__main__':
    figurf()