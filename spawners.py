import random as r
import pygame as pyg
import eatable as eat
import entity as en

def spawnCandies(candyList):
    maxX = 750
    maxY = 550
    minX = 0
    minY = 0
    i = 0
    while i < 24:
        c = r.choice(candyList)
        c.x = r.randrange(minX, maxX)
        c.y = r.randrange(minY, maxY)
        i += 1

def drawCandies(candyList, screen):
    for c in candyList:
        c.update(screen)

def spawnTrolls():
    pass