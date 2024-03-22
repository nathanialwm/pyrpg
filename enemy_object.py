
class Enemy:
    def __init__(self, name = '', lvl = 1, exp = 1, dropC = 1, dropR = 1, hp = 1, att = 1, defe = 1, hit = 1):
        self.name = name
        self.lvl = lvl
        self.exp = exp #exp given when defeated
        self.dropC = dropC #drop chance
        self.dropR = dropR #drop rarity
        self.hp = hp
        self.att = att
        self.defe = defe
        self.hit = hit

    #create getters and setters  
    #get full enemy data to append to a dictionary           
        def getEnemy(self):
            return self.name
            return self.lvl
            return self.exp
            return self.dropC
            return self.dropR
            return self.hp
            return self.att
            return self.defe
            return self.hit
        
        #get individual enemy stats
        def getEName(self):
            return self.name
        
        def getELvl(self):
            return self.lvl
        
        def getEExp(self):
            return self.exp
        
        def getEDropC(self):
            return self.dropC
        
        def getEDropR(self):
            return self.dropR
        
        def getEHP(self):
            return self.hp
        
        def getEAtt(self):
            return self.att
        
        def getEDef(self):
            return self.defe
        
        def getEHit(self):
            return self.hit
        
        #set all stats
        def setEnemy(self, name, lvl, exp, dropC, dropR, hp, att, defe, hit):
            self.name = name
            self.lvl = lvl
            self.exp = exp
            self.dropC = dropC
            self.dropR = dropR
            self.hp = hp
            self.att = att
            self.defe = defe
            self.hit = hit
        
        #set individual player stats
        def setEName(self,x):
             self.name = x
        
        def setELvl(self,x):
             self.lvl = x
        
        def setEExp(self,x):
            self.exp = x
            
        def setEDropC(self,x):
            self.dropC = x
            
        def setDropR(self,x):
            self.dropR = x
        
        def setEHP(self,x):
             self.hp = x
        
        def setEAtt(self,x):
             self.att = x
        
        def setEDef(self,x):
             self.defe = x
        
        def setEHit(self,x):
             self.hit = x

#create a child class for a boss enemy that has an extra stat
class Boss(Enemy):
    def __init__(self, name = '', lvl = 1, exp = 1, dropC = 1, dropR = 1, hp = 1, att = 1, defe = 1, hit = 1, regen = 1):
        Enemy.__init__(self, name = '', lvl = 1, exp = 1, dropC = 1, dropR = 1, hp = 1, att = 1, defe = 1, hit = 1)
        #regen is health restored every other turn
        self.regen = regen
        
        def getERegen(self):
            return self.regen
        
        def setERegen(self,x):
            self.regen = x
        
#create list of enemies
mouse = Enemy('Mouse',1,5,1,1,10,2,0,2)
largeRat = Enemy('Large Rat',5,8,1,1.5,30,4,4,10)       
goblin = Enemy('Goblin',12,19,1.25,2.5,85,12,8,30)
ogre = Enemy('Ogre',25,42,1.33,4.5,220,30,20,65)    
giant = Enemy('Frost Giant', 50, 99, 1.5, 8, 550, 55, 50, 120)        

#create boss enemy
dragon = Boss('Dragon',100, 1000, 2.25, 19.25, 2350, 140, 105, 350, 100)
        
        
        