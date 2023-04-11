import random
import tkinter as tk
from figure import figurf


lives=7
def guss():
    
    def check_guess():
        global lives
       
        lives_label.config(text=str(lives))
        lives-=1
        guess = int(guess_entry.get())
        if guess == secret_number:
            figurf()

        elif lives==0:
            room5.destroy()
            figurf()
            
        if guess > secret_number:
            result_label.config(text="Бери меньше",font='Arial 20')

        if guess < secret_number:
            result_label.config(text="Бери больше ",font='Arial 20')

        
        
                
    secret_number = random.randint(1, 100)


    room5 = tk.Toplevel()
    room5.title('Угадай число')
    room5.geometry('720x360')
    room5.title("Угадай число")


    instruction_label = tk.Label(room5, text="Угадайте число от 1 до 100.У вас есть 7 попыток",font='Arial 20')
    instruction_label.pack()
    lives_label = tk.Label(room5,text=lives)
    lives_label.pack()
    guess_entry = tk.Entry(room5,font='Arial 20')
    guess_entry.pack()

    check_button = tk.Button(room5, text="Проверить", command=check_guess,font='Arial 20')
    check_button.pack()

    result_label = tk.Label(room5, text="",font='Arial 20')
    result_label.pack()

    room5.mainloop()