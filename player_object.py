
#player object
#8 values
class Player:
    def __init__(self, name = '', lvl = 0, exp = 0 , hp = 0, att = 0, defe = 0, hit = 0, luck = 0):
        self.name = name
        self.lvl = lvl
        self.exp = exp
        self.hp = hp
        self.att = att
        self.defe = defe
        self.hit = hit
        self.luck = luck
 
#create getters and setters  
#get full player data to append to a dictionary           
    def getPlayer(self):
        return self.name
        return self.lvl
        return self.exp
        return self.hp
        return self.att
        return self.defe
        return self.hit
        return self.luck
    
    #get individual player stats
    def getPName(self):
        return self.name
    
    def getPLvl(self):
        return self.lvl
    
    def getPExp(self):
        return self.exp
    
    def getPHP(self):
        return self.hp
    
    def getPAtt(self):
        return self.att
    
    def getPDef(self):
        return self.defe
    
    def getPHit(self):
        return self.hit
    
    def getPLuck(self):
        return self.luck
    
    #set all stats
    def setPlayer(self, name, lvl, exp, hp, att, defe, hit, luck):
        self.name = name
        self.lvl = lvl
        self.exp = exp
        self.hp = hp
        self.att = att
        self.defe = defe
        self.hit = hit
        self.luck = luck
    
    #set individual player stats
    def setPName(self,x):
         self.name = x
    
    def setPLvl(self,x):
         self.lvl = x
    
    def setPExp(self,x):
         self.exp = x
    
    def setPHP(self,x):
         self.hp = x
    
    def setPAtt(self,x):
         self.att = x
    
    def setPDef(self,x):
         self.defe = x
    
    def setPHit(self,x):
         self.hit = x
    
    def setPLuck(self,x):
         self.luck = x