import pygame as pyg

class Item:
    def __init__(self, texture, posx=80, posy=120):
        self.texture = texture

        self.consumed: bool = False

        self.wid = 90
        self.hei = 90

        self.x = posx
        self.y = posy

        self.time = 100
        self.rect = pyg.Rect(self.x, self.y, self.wid, self.hei)
        self.uTexture = pyg.image.load(self.texture)
        self.mTexture = None #pyg.transform.scale(self.uTexture, (self.wid, self.hei))

        print(f"Item loaded")

    def __del__(self):
        print(f"Item deleted")
        self.mTexture = None
    
    #Is supposed to delete the item
    def kill(self):
        self.x = 10000
        self.y = 10000
        self.__del__()
    
    #Draws the item*
    def drawItem(self, screen):
        c = pyg.Rect(self.x, self.y, self.wid, self.hei)
        self.rect = c
        #pyg.draw.rect(screen, (0, 0, 100), c)
        
        a = pyg.transform.scale(self.uTexture, (self.wid, self.hei))
        self.mTexture = a
        screen.blit(self.mTexture, (self.x, self.y))

    # MAIN ENTITY UPDATE FUNCTION
    def update(self, screen):
        # Call logic functions based on logic

        self.drawItem(screen)
        #pyg.draw.rect(screen, (0,0,100),self.rect)
        #screen.blit(self.mTexture, (self.x, self.y))