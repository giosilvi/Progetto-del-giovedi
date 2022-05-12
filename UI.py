from tkinter import *

root = Tk()
root.geometry("400x400")

frame = Frame(root)
frame.pack()

def left_button_click(event):
    print('a')

def right_button_click(event):
    print('d')

button1 = Button(root, text="Left", font=("Arial", 20))
button1.bind("<Button-1>", left_button_click)
button1.pack(side=LEFT)

button2 = Button(root, text="Right", font=("Arial", 20))
button2.bind("<Button-1>", right_button_click)
button2.pack(side=RIGHT)

root.mainloop()
