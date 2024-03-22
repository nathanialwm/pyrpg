import random
import numpy
import os
import math
import player_object as p
import enemy_object as en



def newGame():
    
    pt = p.Player(input("What is your characters name?"), 1, 0, 10, 2, 0, 1, 1, 1)
    return pt

def loadGame():
    
    lines = open('player.txt', 'r').readlines()
    pv = []
    for line in lines:
        pv.append(line.strip())
    pt = p.Player(pv[0],int(pv[1]),int(pv[2]),int(pv[3]),int(pv[4]),int(pv[5]),int(pv[6]),int(pv[7]))
    return pt

#save to file
def saveGame():
    global p1
    with open('player.txt', 'w') as f:
        f.write(p1.name + "\n" + p1.lvl + "\n" + p1.exp + "\n" + p1.hp + "\n" + p1.att + 
                "\n" + p1.defe + "\n" + p1.hit + "\n" + p1.luck)
        
#on game start check for saved player.txt
def start():    
    
    #find if a player file exists already
    if os.path.isfile('player.txt'):
        pt = loadGame()
        return pt
    else:
        pt = newGame()
        return pt
    
    print(""""Welcome to Python RPG, fight monsters, level up and equip items.
    Type 'help' to bring up a list of commands""")
    
    main()
    
p1 = start()

#mainloop
def main():
    
    action = input()
    
    if action == 'battle':
        battleMain()
    elif action == 'character' or action == 'char':
        charMain()
    elif action == 'equipment' or action =='equip':
        equipMain()
    elif action == 'save':
        saveGame()
    elif action == 'help':
        helpMain()
    else:
        main()
    
    


#battle
def battle(p,en):
    #create temporary hp points
    pthp = p.hp
    ethp = en.hp
    global pthp
    global ethp
    
    print(pthp,ethp)
    def turn():
        #determine chance the player hits
        phitchance = p.hit / (en.lvl * 10)
        ehitchance = en.hit / (p.lvl * 10)
        
        #determine if hits
        pr = math.ceil((random.random() * 100))
        enr = math.ceil((random.random() * 100))
        
        #player action
        if pr <= phitchance: #hit
        
            if en.defe >= p.att: #0 damage
                ethp = ethp
            else: #does damage
                ethp = ethp - (p.att - en.defe)
                
        else: #doesn't hit
            ethp = ethp
            
        #enemy action
        if enr <= ehitchance: #hit
        
            if p.defe >= en.att: # 0 damage
                pthp = pthp
            else: #does damage
                pthp = pthp - (en.att - p.defe)
                
        else: #doesn't hit
            pthp = pthp
        
        return pthp, ethp
        
        
            
    #reiterate turns until player or enemy loses all hp
    while pthp > 0 and ethp > 0:
        turn()
battle(p1,en.mouse)       
def battleMain():
    action = input("")
    
    if action == 'battle':
        battleMain()
    elif action == 'character' or action == 'char':
        charMain()
    elif action == 'equipment' or action =='equip':
        equipMain()
    elif action == 'save':
        saveGame()
    elif action == 'help':
        helpMain()
    else:
        main()

#equipment
def equipMain():
    action = input()
    
    if action == 'battle':
        battleMain()
    elif action == 'character' or action == 'char':
        charMain()
    elif action == 'equipment' or action =='equip':
        equipMain()
    elif action == 'save':
        saveGame()
    elif action == 'help':
        helpMain()
    else:
        main()

#character
def charMain():
    action = input()
    
    if action == 'battle':
        battleMain()
    elif action == 'character' or action == 'char':
        charMain()
    elif action == 'equipment' or action =='equip':
        equipMain()
    elif action == 'save':
        saveGame()
    elif action == 'help':
        helpMain()
    else:
        main()
    
def helpMain():
    action = input("""
    Here is a list of commands:
    'help' for a list of commands
    'battle' to bring up the battle menu
    'equip' to bring up your equipment menu
    'char' to bring up character menu
    'save' to save your character at any time
    """)
    
    if action == 'battle':
        battleMain()
    elif action == 'character' or action == 'char':
        charMain()
    elif action == 'equipment' or action =='equip':
        equipMain()
    elif action == 'save':
        saveGame()
    elif action == 'help':
        helpMain()
    else:
        main()



    





        
