import random
import time

turn = 2
phealth = 3
ehealth = 3
rounds = 1
bpos = random.randrange(1, 6)

class color:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    END = '\033[0m'
    WHITE = '\033[97m'
    ORANGE = ' \033[38;2;255;165;0m'

def reset_round():
    global rounds, bpos
    rounds = 1
    bpos = random.randrange(1, 6)

def pturn():
    global rounds, bpos, phealth, ehealth, turn, rounds
    try:
        play = int(input(color.ORANGE + "Press number 1 to shoot yourself, number 2 to shoot your enemy or number 3 to quit\n" + color.END))
    except ValueError:
        print(color.RED + "Invalid Input. Please enter 1, 2 or 3." + color.END)
    
    if play == 1:
        if rounds == bpos:
            print(color.YELLOW + "You: " + color.YELLOW)
            print(color.YELLOW + "You shot yourself!" + color.END)
            print(color.RED + "-1 HP" + color.END)
            phealth -= 1
            reset_round()
        else:
            print(color.GREEN + "The gun didnt go off." + color.END)
    elif play == 2:
        if rounds == bpos:
            print(color.YELLOW + "You:" + color.END)
            print(color.GREEN + "You shot your enemy!" + color.END)
            print(color.RED + "-1 HP" + color.END)
            ehealth -= 1
            reset_round()
        else:
            print(color.RED + ("The gun didnt go off." + color.END))
    elif play == 3:
        quit()
    else:
        print("Invalid Choice. Try again with one of the options given")
    turn += 1
    rounds += 1

def eturn():
    global phealth, ehealth, turn, rounds
    decision = random.choice(['Shoot_Self', 'Shoot_Player'])

    if decision == 'Shoot_Self':
        if rounds == bpos:
            print(color.YELLOW + "Enemy: " + color.END)
            print(color.YELLOW + "The Enemy shot himself!" + color.END)
            print(color.RED + "-1 HP" + color.END)
            ehealth -= 1
            reset_round()
        else:
            print(color.YELLOW + "Enemy: " + color.END)
            print(color.GREEN + "They tried to shoot themselves but the gun didnt go off" + color.END)
            time.sleep(1.5)
    else:
        if rounds == bpos:
            print(color.YELLOW + "Enemy: " + color.END)
            print(color.RED + "The Enemy shot you" + color.END)
            phealth -= 1
            reset_round()
        else:
            print(color.YELLOW + "Enemy: " + color.END)
            print(color.GREEN + "The Enemy tried shooting you but the gun failed" + color.END)
    turn += 1
    rounds += 1

#Game Loop
while phealth > 0 and ehealth > 0:
    print(f"\n{color.GREEN}Your Health:{phealth}{color.END} || {color.RED}Enemy health:{ehealth} {color.END}\n")
    if rounds > 6:
        reset_round()
    if turn % 2 ==0:
        pturn()
    else:
        time.sleep(1.5)
        eturn()
#Game Over
if ehealth == 0:
    print(color.GREEN + "Congratulations you won! Press 3 next time" + color.END)
    time.sleep(1)
else:
    print(color.RED + "Sorry you lost. Press 3 next time " + color.END)
    time.sleep(1)