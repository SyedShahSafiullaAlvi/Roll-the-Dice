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

def roll():
    while 1:
        import random
        num=random.randint(1,7)
        if num==1:
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
        elif num==6:
            print('''
                 -----
                |  6  |
                 -----
                ''')
            continue

print("Hey, Lets roll the dice.")
roll()
while 1:
    roll_again= input("Wanna roll again? Type 'S' or else Type 'N':  ").upper()
    if roll_again=='S':
        roll()
        continue
    elif roll_again=='N':
        break
    else:
        print("Invalid choice!!")
        continue
