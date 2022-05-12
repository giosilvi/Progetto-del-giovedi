# 
import tkinter
import numpy as np 
from pynput import keyboard
import time

from functions import * # import all functions

from tkinter import *


root = Tk()
root.geometry("400x400")



print('******Welcome to the ORACLE game********\nThe oracle will try to guess what are you gonna press next.')
print('Enter space to exit.')
global counto
global county
counto = 0
county = 0
n = 4

# pattern = [['d','a'],['a','d']]
pattern = {'d': 'a', 'a':'d'}

""" pattern_multi = {'aaa':1,
                'aad':1, 
                'ada':1,
                'add':1,
                'daa':1,
                'dad':1,
                'dda':1,
                'ddd':1} """

pattern_multi = prepare(n)
name_of_the_file = str(n)+'oracle_memory.txt'
pattern_multi = load_dictionary(pattern_multi, name_of_the_file)
print(pattern_multi)

global oracle_next
oracle_next = 'a' if np.random.rand()<0.5 else 'd'
input_key = ''
global last3keys
last3keys =' '*n

turn = 0


def main_function(input_key):
        # Update pattern here
        global last3keys
        last3keys = last3keys[1:n] + input_key  # ada -> da + key(a) -> daa -> aa.....

        #check if you win
        global oracle_next
        global counto
        global county
        counto,county = check_win(input_key, oracle_next, counto, county)
            
        print('Oracle: ', counto, ' You: ', county)

        youwin=round(county/(counto+county)*100, ndigits = 3) #percentage of victory
        print("Winning rate: ", youwin, '%')
        

        if last3keys in pattern_multi: # if pattern is recognized
            pattern_multi[last3keys] +=1 #update likelihood
            
            contestants = find_contenders(last3keys, pattern_multi, n) 
            #print('The contestant are:', contestants)
            oracle_next = oracle_prediction(contestants, n)
        
        else:
            # If no pattern, next oracle is random
            oracle_next = 'a' if np.random.rand() > 0.5 else 'd'
        return oracle_next





frame = Frame(root)
frame.pack()
import datetime
root.title("Time") 
root.geometry("500x500") 
time_label = Label(root, text="Time: ")
time_label.pack() 
time_text = Text(root, height=1, width=8) 
time_text.pack() 
def update_time(): 
    time_text.delete(1.0, END) 
    time_text.insert(END, str(datetime.datetime.now().time())) 
    root.after(1000, update_time) 
update_time()


label = Label(frame, text=last3keys)
label.pack(side = TOP)

def left_button_click(event):
    print('a')
    main_function('a')
    return 

def right_button_click(event):
    main_function('d')
    return 

button1 = Button(root, text="Left", font=("Arial", 20))
input_key = button1.bind("<Button-1>", left_button_click)
button1.pack(side=LEFT)

button2 = Button(root, text="Right", font=("Arial", 20))
input_key = button2.bind("<Button-1>", right_button_click)
button2.pack(side=RIGHT)
root.mainloop()

save_dictionary(pattern_multi, name_of_the_file)
print(pattern_multi)
