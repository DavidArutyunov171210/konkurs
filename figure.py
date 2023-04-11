#5,1,2,3,1,4,3,5,4

from tkinter import *
from tkinter import messagebox
from won import win
line_button1=-1
line_button2=-1

def figurf():
    global line_button1,line_button2
    
    size=20
    lines=['12','13','14','15','23','34','35','45']
    copy_lines=lines[:]
    def chek_line(btn1, btn2):

        if len(lines)==0:
            win() 

        a = btn1.cget('text')
        b=btn2.cget('text')

        line = a+b
        print(line)
        if line in lines:
            lines.remove(line)
            return True            
        line = b+a
        print('1',line)
        



        if line in lines:
            lines.remove(line)
            return True
        else:
            return False
        

    def click_button(event):


        button1=event.widget
        
        global line_button1,line_button2
        
        if line_button1==-1:
            line_button1=button1
            # line_button1.config(bg='red')
        else:
            
            line_button2=button1
            if chek_line(line_button1,line_button2):
                line(line_button1,line_button2)
                line_button1=line_button2
                line_button2=-1
            else:
                messagebox.showinfo('Вы уже провели это линию,\nделать это второй раз нельзя')
            

    

    def line(b1,b2):
        x1=b1.winfo_x()+size
        y1=b1.winfo_y()+size
        x2=b2.winfo_x()+size
        y2=b2.winfo_y()+size
        

        canvas.create_line(x1,y1,x2,y2)

    def giveup():
        room3.destroy()
        
    print(lines)
    room3=Toplevel()
    room3.title('Не отрывая руки')

    canvas=Canvas(room3,width=1000,height=1000)
    button1=Button(canvas,text='1',font='Arial 50')
    button1.bind('<Button-1>',click_button)
    button1.place(x=300,y=300)
    button2=Button(canvas,text='2',font='Arial 50')
    button2.bind('<Button-1>',click_button)
    button2.place(x=450,y=100)
    button3=Button(canvas,text='3',font='Arial 50')
    button3.bind('<Button-1>',click_button)
    button3.place(x=600,y=300)
    button4=Button(canvas,text='4',font='Arial 50')
    button4.place(x=600,y=600)
    button4.bind('<Button-1>',click_button)
    button5=Button(canvas,text='5',font='Arial 50')
    button5.bind('<Button-1>',click_button)
    button5.place(x=300,y=600)

  
    canvas.pack()
    
    give_up=Button(room3,text='Я сдаюсь',font='Arial 40',command=giveup)
    give_up.place(x=700,y=700)
    room3.mainloop()

   
    
if __name__ == '__main__':
    figurf()

 