import pygame as pyg

class Entity:
    def __init__(self, name, texture, shadowTexture, posx=20, posy=20, time = 20):
        self.texture = texture
        self.name = name
        
        self.isDead = False
        self.VERT = ("UP", "DOWN")
        """0 = UP, 1 = DOWN"""
        self.HORIZ = ("LEFT", "RIGHT")
        """0 = LEFT, 1 = RIGHT"""

        self.wid = 50
        self.hei = 50

        self.x = posx
        self.y = posy
        self.r = 0

        self.time = time
        self.timeInc = 0
        self.timeSec = 0

        self.shadow = shadowTexture
        self.rect: pyg.Rect = None
        self.uTexture = pyg.image.load(self.texture)
        self.mTexture = None

        self.vert = self.VERT[1]
        self.horiz = self.HORIZ[1]

    def __del__(self):
        self.isDead = True
        print(f"Entity: {self.name} deleted")
        self.mTexture = None

    def kill(self):
        self.x = 10000
        self.y = 10000
        self.wid = 0
        self.hei = 0
        self.__del__()
    
    #Handles the player's drawing functionallities
    def drawPlayer(self, screen):
        shtx = pyg.image.load(self.shadow)
        sha = pyg.transform.scale(shtx, (self.wid, self.hei))
        shb = pyg.transform.rotate(sha, (self.r))
        shdw = shb
        screen.blit(shdw, (self.x + 10, self.y + 10))

        c = pyg.Rect(self.x, self.y, self.wid, self.hei)
        self.rect = c
        #pyg.draw.rect(screen, (100, 0, 0), c)
        
        a = pyg.transform.scale(self.uTexture, (self.wid, self.hei))
        b = pyg.transform.rotate(a, (self.r))
        self.mTexture = b
        screen.blit(self.mTexture, (self.x, self.y))

    #The timer that counts down till 0
    def entityTimer(self):
        self.timeInc += 1
        if self.timeInc >= 61:
            self.timeSec += 1
            self.time -= 1
            self.timeInc = 0

    # __________MAIN ENTITY UPDATE FUNCTION__________
    def update(self, screen):
        # Call logic functions based on logics
        if self.isDead == False:
            self.drawPlayer(screen)
        #self.death_timer(self,screen)
        
        #makes sure player size doesn't go negative so the game won't crash lol
        if self.wid <= 10 and self.wid != 0:
            self.wid = 10
        if self.hei <= 10 and self.hei != 0:
            self.hei = 10

        if self.time != 0:
            self.entityTimer()

        if self.wid > 800:
            self.wid = 800
        if self.hei > 800:
            self.hei = 800


    def getTime(self):
        return  self.time