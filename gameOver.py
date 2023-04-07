import tkinter as tk
pic = ""

def gO():
    global pic
    go = tk.Toplevel()
    canvas1 = tk.Canvas(go, width=1000, height=1000)
    canvas1.pack()

    pic = tk.PhotoImage(file="/Users/david/PycharmProjects/test/__pycache__/image/go.png")
    image = canvas1.create_image(1,1 ,anchor=tk.NW, image=pic) 

    go.mainloop()
