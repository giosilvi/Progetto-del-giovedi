
from tkinter import *
import time
from turtle import color


root = Tk() # create a window
root.geometry("800x800") # width x height
root.title ("Matrix Code") # title of the window
root.configure(background='#fff') # background color 

frame = Frame(root) # create a frame
frame.pack() # pack the frame, which means that it will be displayed

def left_button_click(event):
    print('a')

def right_button_click(event):
    print('d')

text =Label(root, text="I am the Oracle", font=("Lato", 30)) # create a label, with text
text.configure(foreground="green") # text color
text.pack(anchor="n", pady=20) 
subtitle =Label(root, text="I am the all-seeing, all-knowing being of the Matrix", font=("Lato", 15))
subtitle.configure(foreground="black")
subtitle.pack(anchor="n", pady=10)

button1 = Button(root, text="Left", font=("Arial", 10), width=30, height= 1, bg="red")
button1.bind("<Button-1>", left_button_click)
button1.pack(side=LEFT, padx=0, expand=True, fill=Y)

button2 = Button(root, text="Right", font=("Arial", 10), width=30, height= 1, bg="blue")
button2.bind("<Button-1>", right_button_click)
button2.pack(side=RIGHT, padx=10, expand=True, fill=Y)

time1 = ''
clock = Label(root, font=('times', 20, 'bold'), bg='#fff')
clock.pack(fill=BOTH, expand=1)

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)

def close_window():
    root.destroy()

button3 = Button(root, text="Close", font=("Arial", 20), command=close_window)
button3.pack()

tick()

root.mainloop()