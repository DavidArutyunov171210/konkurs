import tkinter as tk
pic = ""

def win():
    global pic
    root = tk.Toplevel()
    canvas1 = tk.Canvas(root, width=1000, height=1000)
    canvas1.pack()

    pic = tk.PhotoImage(file="__pycache__/project/wonimage.png")
    image = canvas1.create_image(1,1 ,anchor=tk.NW, image=pic) 

    root.mainloop()

