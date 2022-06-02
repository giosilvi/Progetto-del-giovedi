# 

from ctypes import alignment
import numpy as np 
import time
from functions import * # import all functions

from tkinter import *






print('******Welcome to the ORACLE game********\nThe oracle will try to guess what are you gonna press next.')
print('Enter space to exit.')
#declare global variables
global counto # global variable to store the number of oracle wins
global county # global variable to store the number of user wins
global oracle_next # global variable to store next guess
global last_n_keys # global variable to store last n keys
global pattern_multi
global n
counto = 0
county = 0
n = 4 # number of keys in the pattern
oracle_next = 'a' if np.random.rand()<0.5 else 'd' #first guess
pattern_multi = prepare(n) # prepare the list of patterns of length n

name_of_the_file = str(n)+'oracle_memory.txt' # file to save the pattern dictionary
pattern_multi = load_dictionary(pattern_multi, name_of_the_file) # load the dictionary

input_key = '' # to store the input key, char value
last_n_keys =' '*n # initialize last n keys, type string


def the_game(input_key): # main function
        global last_n_keys # global variable to store last n keys
        global oracle_next # global variable to store next guess
        global counto # global variable to store the number of oracle wins
        global county # global variable to store the number of user wins
        
        # update the last n keys
        last_n_keys = last_n_keys[1:n] + input_key  # ada -> da + key(a) -> daa -> aa.....

        #check if you win
        counto,county = check_win(input_key, oracle_next, counto, county)
        # compute the percentage of victories
        youwin=round(county/(counto+county)*100, ndigits = 3) # round to 3 decimal
        print("Winning rate: ", youwin, '%')
        #call function to insert winning rate
        update_winning_rate(title,youwin) # update the winning rate, passing the label and the percentage

        if last_n_keys in pattern_multi: # if last_n_keys is in the pattern_multi dictionary
            pattern_multi[last_n_keys] +=1 # add 1 to the value of the key, e.g. pattern_multi['ada'] = pattern_multi['ada'] + 1
            
            contestants = find_contenders(last_n_keys, pattern_multi, n) # find the new contenders
            oracle_next = oracle_prediction(contestants, n) # find the next guess
        
        else: # if last_n_keys is not in the pattern_multi dictionary
            # If no pattern, next oracle is random
            oracle_next = 'a' if np.random.rand() > 0.5 else 'd' # random guess
        return oracle_next # return the next guess



root = Tk() # create a window
root.geometry("800x800") # width x height
root.title ("Matrix Code") # title of the window
root.configure(background='#fff') # background color 

frame = Frame(root) # create a frame
frame.pack() # pack the frame, which means that it will be displayed


label = Label(frame, text=last_n_keys) # create a label
label.pack(side = TOP) # pack the label

def left_button_click(event): # function to call when left button is clicked
    the_game('a') # call the main function
    return 

def right_button_click(event): # function to call when right button is clicked
    the_game('d') # call the main function
    return 
def erase_file(event):
    global pattern_multi
    global n
    pattern_multi = prepare(n)
    print("The file has been erased.")

title =Label(root, text="I am the Oracle", font=("Lato", 30)) # create a label, with text
title.configure(foreground="green") # text color
title.pack(anchor="n", pady=20) 

subtitle =Label(root, text="I am the all-seeing, all-knowing being of the Matrix", font=("Lato", 15))
subtitle.configure(foreground="black")
subtitle.pack(anchor="n", pady=10)



button1 = Button(root, text="Left", font=("Arial", 55), width=6, height=2, bg="red", fg="white")
button1.bind("<Button-1>", left_button_click)
button1.pack(side=LEFT, padx=0, expand=True) # expand=True means that the button will take up all the space available
root.bind("<Key-a>", left_button_click) # bind the a button to the function
root.bind("<Left>", left_button_click) # bind the left button to the function



button2 = Button(root, text="Right", font=("Arial", 55), width=6, height=2, bg="blue", fg="white")
button2.bind("<Button-1>", right_button_click)
button2.pack(side=RIGHT, padx=10, expand=True)
root.bind("<Key-d>", right_button_click) # bind the d button to the function
root.bind("<Right>", right_button_click) # bind the right button to the function

#make a button on the bottom that call the function to erase the file
button3 = Button(root, text="Reset", font=("Arial", 15), width=6, height=2, bg="gray", fg="white")
button3.bind("<Button-1>", erase_file)
#pack the button
button3.pack(side=BOTTOM, pady=10)


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

# function to update winning rate
def update_winning_rate(winning_text,winning_rate):
    winning_text.configure(text="Winning rate: "+str(winning_rate))




button3 = Button(root, text="Close", font=("Arial", 20), command=close_window)
button3.pack()

tick()

root.mainloop()
save_dictionary(pattern_multi, name_of_the_file)