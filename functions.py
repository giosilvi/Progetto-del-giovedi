# FUNCTIONS DECLARATION
from pynput import keyboard
import numpy as np
import os
#import matplotlib.pyplot as plt 
def get_input_key():
    with keyboard.Events() as events: 
        # Block for as much as possible
        event = events.get(1e6) 
        # print('è stato premuto ', event.keyy)
    return event.key

def check_win(input_key, oracle_next, counto, county):
    if input_key == oracle_next:
        print('Oracle win, with ',oracle_next)
        counto = counto +1
                
    else:
        print('You win, with', input_key)
        county = county + 1
    return counto,county

def transform_in_percentage(contestants):
    # print('Pre',contestants)
    sum_of_values = sum(contestants.values()) # the sum of the 2 counts
    for key in contestants.keys(): #transform number in percentage (0 to 1)
        contestants[key] = contestants[key]/sum_of_values    
    # print('Post',contestants)
    return contestants

def find_contenders(last3keys, pattern_multi, n):
    contestants = {} #new dictionary, every time!
    for pat in pattern_multi.keys(): # for pat in ['aaa', 'aad','ada',....] #find contestant
        if last3keys[1:n]==pat[0:n-1]: #pat[0:2] = ['aa' ,'aa', 'ad,...]
            contestants[pat] = pattern_multi[pat] # take the number of the two contestant pattern
    return transform_in_percentage(contestants) #return the whole dictionary

def oracle_prediction(contestants, n):
    rand = np.random.rand()
    contest_pattern = list(contestants.keys()) #get both keys:e.g. ['ada','add']
    first_pattern = contest_pattern[0]
    secon_pattern = contest_pattern[1]
    if rand < contestants[first_pattern]:  #if rand is less than contestants['ada']= 0.4
        oracle_next = first_pattern[n-1] #the 3rd element 'a'
    else:
        oracle_next = secon_pattern[n-1] #the 3rd element 'd'
    return oracle_next

def save_dictionary(dictionary, filename):
    with open(filename, "w") as f:
        for key, value in dictionary.items():
            f.write("{} {}\n".format(key, value))
             

def load_dictionary(dictionary, filename): 
    if os.path.exists(filename):
        with open(filename) as f:
            for line in f:
                key, value = line.split()
                dictionary[key] = int(value)
    return dictionary

def plot_histogram(dictionary):
    for key, value in dictionary.items():
        plt.bar(key, value, color=np.random.rand(3,))
    plt.show()


def prepare(n=3):
    dictionary= {'a':1,
                 'd':1}
    for i in range(n-1):
        keyvalue=dictionary.items()
        for key, value in list(keyvalue):
            dictionary[key+'a']= value
            dictionary[key+'d']= value
    keys=dictionary.keys()
    for key in list(keys):
        if len(key)<n:
            dictionary.pop(key)

    return dictionary
    


    