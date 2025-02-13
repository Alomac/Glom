import pygame as pyg
from tkinter import messagebox
import tkinter as tk

import entity as en
from texload import texplode

# Screen Width
SCW = 800
# Screen Height
SCH = 600

#Fonts
class fonts:
    arial = "Arial Rounded MT Bold"
    bell_mt = "Bell MT"
    system_bold = "System Bold"
    terminal = "Terminal"

#Functions for when the player dies
def explode(player: en.Entity, screen):
    tx = pyg.image.load(texplode)
    screen.blit(tx, (player.x - 200, player.y - 200))
    if player.isDead:
        udied = tk.messagebox.showerror(title="  ERROR!!  ", message="       YOU DIED FROM EXPLODE  ")
        udied()
def dieFunction(player: en.Entity):
    if player.isDead:
        udied = tk.messagebox.showerror(title="  ERROR!!  ", message="           YOU DIED FROM TROLL      ")
        udied()
def winFunction(player: en.Entity):
    uwin = tk.messagebox.showinfo(title="  LOL  ", message="         YOU WINNED   ")
    uwin()
def tieFunction(player: en.Entity, monster: en.Entity):
    if player.wid == monster.wid and player.hei == monster.hei:
        utie = tk.messagebox.showinfo(title="  Cat  ", message="         TIE        ")
        utie()

#Timer
class Timer:
    def __init__(self):
        self.inc = 0
        self.second = 0
        self.signal = False
    
    def tick(self, amount=1):
        self.inc += amount
        if self.inc >= 61:  # So that the count actually reaches 60
            self.second += 1
            self.inc = 0

    def tick_reverse(self, amount=1):
        self.inc -= amount
        if self.inc <= -61:
            self.second -= 1
            self.inc = 0

    def getSecond(self):
        return self.second
    def getInc(self):
        return self.inc
    def getSignal(self):
        return self.signal