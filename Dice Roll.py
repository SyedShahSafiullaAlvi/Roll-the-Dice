print('''
   _______
  /\ o o o\
 /o \ o o o\_______
<    >------>   o /|
 \ o/  o   /_____/o|
  \/______/     |oo|
        |   o   |o/
        |_______|/
 
''')

def roll():          # writing a function for dice rolling
    while 1:
        import random       # importing random module to randomise the outcoming number
        num=random.randint(1,7)         # num variable be assigned any number among 1,2,3,4,5 and 6
        
        if num==1:              # printing the number we got on rolling the dice
            print('''
                 -----
                |  1  |
                 -----
                ''')
            break
        elif num==2:
            print('''
                 -----
                |  2  |
                 -----
                ''')
            break
        elif num==3:
            print('''
                 -----
                |  3  |
                 -----
                ''')
            break
        elif num==4:
            print('''
                 -----
                |  4  |
                 -----
                ''')
            break
        elif num==4:
            print('''
                 -----
                |  5  |
                 -----
                ''')
            break
        elif num==6:                # if got 6, dice is automatically rolled again
            print('''
                 -----
                |  6  |
                 -----
                ''')
            continue

print("Hey, Lets roll the dice.")
roll()              # calling the dice rolling function
while 1:
    roll_again= input("Wanna roll again? Type 'S' or else Type 'N':  ").upper()     # asking user 
    if roll_again=='S':             # If yes, dice is rolled again
        roll()
        continue
    elif roll_again=='N':           # if no program is terminated
        break
    else:
        print("Invalid choice!!")      # if user by mistakely enters anything else except 'S' and 'No', It asks user to enter choice once again
        continue
