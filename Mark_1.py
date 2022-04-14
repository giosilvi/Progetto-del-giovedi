# 
import numpy as np 


key = ''
print('******Welcome to the ORACLE game********\nThe oracle will try to guess what are you gonna press next.')
print('Enter space to exit.')

counto = 0
county = 0
while key!=' ':
    print('\nPress A o D')
    randomnumber = np.random.rand()
    if randomnumber > 0.5:
        oracle = ['a', 'A']
    else:
        oracle = ['d', 'D']

    key = input() # get input here

    if key in ['a','d','A','D']: 
        # print('Oracle prediction:',oracle)
        
        if key in oracle:
            print('oracle win')
            counto = counto +1
            
        else:
            print('you win')
            county = county + 1
            
        print('Oracle: ', counto, ' You: ', county)
        youwin=round(county/(counto+county)*100, ndigits = 3)
        print("Winning rate: ", youwin, '%')
        #
        #
        #
        #
        #
        #
        #
    elif key == ' ':
        print('Exiting')
    else:
        print('Wrong key')
    