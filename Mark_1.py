# 
import numpy as np 
from pynput import keyboard
import time

from functions import * # import all functions

print('******Welcome to the ORACLE game********\nThe oracle will try to guess what are you gonna press next.')
print('Enter space to exit.')
print('If you are Andrea be aware....you will lose')

counto = 0
county = 0

# pattern = [['d','a'],['a','d']]
pattern = {'d': 'a', 'a':'d'}

pattern_multi = {'aaa':1,
                'aad':1, 
                'ada':1,
                'add':1,
                'daa':1,
                'dad':1,
                'dda':1,
                'ddd':1}

oracle_next = 'a' if np.random.rand()<0.5 else 'd'
input_key = ''
last3keys ='   '

turn = 0

while input_key!= keyboard.Key.space:
    turn +=1
    time.sleep(0.5) #weird

    print('\nSeries:',last3keys)
    print('Press A o D (turn=',turn,')')#ask

    input_key = get_input_key()
    # print('pressed:',input_key)

    if input_key == keyboard.Key.space:
        print('Exiting')
        print(' Patterns:',pattern_multi)
        break #exit from while loop
    
    if hasattr(input_key, 'char'):
        if input_key.char in ['a', 'd']: 
            input_key = input_key.char # input_key: KeyCode -> input_key:char
            
            # Update pattern here
            last3keys = last3keys[1:3] + input_key  # ada -> da + key(a) -> daa -> aa.....

            #check if you win
            counto,county = check_win(input_key, oracle_next, counto, county)
                
            print('Oracle: ', counto, ' You: ', county)

            youwin=round(county/(counto+county)*100, ndigits = 3) #percentage of victory
            print("Winning rate: ", youwin, '%')
            

            if last3keys in pattern_multi: # if pattern is recognized
                pattern_multi[last3keys] +=1 #update likelihood
                
                contestants = find_contenders(last3keys, pattern_multi) 
                #print('The contestant are:', contestants)
                oracle_next = oracle_prediction(contestants)
               
            else:
                # If no pattern, next oracle is random
                oracle_next = 'a' if np.random.rand() > 0.5 else 'd'
      
        else:
            print('Wrong char key')
  
    else:
        print('Wrong key')

print('Last goodbye')
    