# 
import numpy as np 
from pynput import keyboard


print('******Welcome to the ORACLE game********\nThe oracle will try to guess what are you gonna press next.')
print('Enter space to exit.')

counto = 0
county = 0

# pattern = [['d','a'],['a','d']]
pattern = {'d': 'a', 'a':'d'}

patter_multi = {'aaa':1,
                'aad':1, 
                'ada':1,
                'add':1,
                'daa':1,
                'dad':1,
                'dda':1,
                'ddd':1}

oracle_next = 'a' if np.random.rand()<0.5 else 'd'
input_key = ''
lastkeys ='   '

turn = 0

while input_key!= keyboard.Key.space:
    turn +=1


    print('\nSeries:',lastkeys)
    print('Press A o D (turn=',turn,')')#ask
    with keyboard.Events() as events: 
        # Block for as much as possible
        event = events.get(1e6)
        input_key = event.key 
        
        print('è stato premuto ', input_key)
  
    if input_key in [keyboard.KeyCode.from_char('a'), keyboard.KeyCode.from_char('d')]: 
        if input_key == keyboard.KeyCode.from_char('a'):
            input_key = 'a'
        else:
            input_key = 'd'
            
        # Update pattern here
        
        lastkeys = lastkeys[1:3] + input_key  # ada -> da + key(a) -> daa -> aa.....

        #check if you win
        if input_key == oracle_next:
            print('Oracle win, with ',oracle_next)
            counto = counto +1
            
        else:
            print('You win, with', input_key)
            county = county + 1
            
        print('Oracle: ', counto, ' You: ', county)
        youwin=round(county/(counto+county)*100, ndigits = 3)
        print("Winning rate: ", youwin, '%')
        

        if lastkeys in patter_multi: # if pattern is recognized
            patter_multi[lastkeys] +=1 #update likelihood
            contest = {} #new dictionary, every time!
            for pat in patter_multi.keys(): # for pat in ['aaa', 'aad','ada',....] #find contestant
                if lastkeys[1:3]==pat[0:2]: #pat[0:2] = ['aa' ,'aa', 'ad,...]
                    #print('next',pat[0:2],'(',pat[2],') with probability', patter_multi[pat])  
                    contest[pat] = patter_multi[pat] # take the number of the two contestant pattern
            
            sum_of_values = sum(contest.values()) # the sum of the 2 counts

            for key in contest.keys(): #transform number in percentage ( 0 to 1)
                contest[key] = contest[key]/sum_of_values
            #print('The contestant are:', contest)
            
            rand = np.random.rand()
            keys = list(contest.keys()) #get both keys:e.g. ['ada','add']
            first_pattern = keys[0]
            secon_pattern = keys[1]
            if rand < contest[first_pattern]:  #if rand is less than contest['ada']= 0.4
                oracle_next = first_pattern[2] #the 3rd element 'a'
            else:
                oracle_next = secon_pattern[2] #the 3rd element 'd'
        else:
            # If no pattern, next oracle is random
            if np.random.rand() > 0.5:
                oracle_next = 'a'
            else:
                oracle_next = 'd'
        #
        #
    elif input_key == keyboard.Key.space:
        print('Exiting')
        print(' Patterns:',patter_multi)
    else:
        print('Wrong key')
    