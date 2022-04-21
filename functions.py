# FUNCTIONS DECLARATION
from pynput import keyboard
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

def find_contenders(last3keys, pattern_multi):
    contestants = {} #new dictionary, every time!
    for pat in pattern_multi.keys(): # for pat in ['aaa', 'aad','ada',....] #find contestant
        if last3keys[1:3]==pat[0:2]: #pat[0:2] = ['aa' ,'aa', 'ad,...]
            contestants[pat] = pattern_multi[pat] # take the number of the two contestant pattern
    return transform_in_percentage(contestants) #return the whole dictionary

def oracle_prediction(contestants):
    rand = np.random.rand()
    contest_pattern = list(contestants.keys()) #get both keys:e.g. ['ada','add']
    first_pattern = contest_pattern[0]
    secon_pattern = contest_pattern[1]
    if rand < contestants[first_pattern]:  #if rand is less than contestants['ada']= 0.4
        oracle_next = first_pattern[2] #the 3rd element 'a'
    else:
        oracle_next = secon_pattern[2] #the 3rd element 'd'
    return oracle_next