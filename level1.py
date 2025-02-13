import pygame as pyg
import tkinter as tk
import time
from texload import *
from soundload import *
import entity as en
import eatable as eat
import spawners
import movement
import util

pyg.init()
pyg.mixer.init()
screen = pyg.display.set_mode((util.SCW, util.SCH))
pyg.display.set_caption("Glom")
icon = pyg.image.load(tglom)
pyg.display.set_icon(icon)
clock = pyg.time.Clock()
gameTimer = util.Timer()

tex_bg = pyg.image.load(tbg)

player = en.Entity(name="Player", texture=tglom, shadowTexture=tglom_shadow, time=10)
enemy = en.Entity(name="Troll", texture=ttroll, shadowTexture=ttroll_shadow, time=100, posx=500)

candyRed = eat.Item(texture=tcandy_red)
candyBlue = eat.Item(texture=tcandy_blue)
candyGreen = eat.Item(texture=tcandy_green)
candyYellow = eat.Item(texture=tcandy_yellow)
candyChoco = eat.Item(texture=tcandy_chocolate)
candyMint = eat.Item(texture=tcandy_peppermint)
candyChoco1 = eat.Item(texture=tcandy_chocolate)
candyMint1 = eat.Item(texture=tcandy_peppermint)
candyChoco2 = eat.Item(texture=tcandy_chocolate)
candyMint2 = eat.Item(texture=tcandy_peppermint)
candyChoco3 = eat.Item(texture=tcandy_chocolate)
candyMint3 = eat.Item(texture=tcandy_peppermint)
candyRed1 = eat.Item(texture=tcandy_red)
candyBlue1 = eat.Item(texture=tcandy_blue)
candyGreen1 = eat.Item(texture=tcandy_green)
candyYellow1 = eat.Item(texture=tcandy_yellow)
candyRed2 = eat.Item(texture=tcandy_red)
candyBlue2 = eat.Item(texture=tcandy_blue)
candyGreen2 = eat.Item(texture=tcandy_green)
candyYellow2 = eat.Item(texture=tcandy_yellow)
candyRed3 = eat.Item(texture=tcandy_red)
candyBlue3 = eat.Item(texture=tcandy_blue)
candyGreen3 = eat.Item(texture=tcandy_green)
candyYellow3 = eat.Item(texture=tcandy_yellow)

candyHolder = (
    candyRed,
    candyBlue,
    candyGreen,
    candyYellow,
    candyChoco,
    candyMint,
    candyChoco1,
    candyMint1,
    candyChoco2,
    candyMint2,
    candyChoco3,
    candyMint3,
    candyRed1,
    candyBlue1,
    candyGreen1,
    candyYellow1,
    candyRed2,
    candyBlue2,
    candyGreen2,
    candyYellow2,
    candyRed3,
    candyBlue3,
    candyGreen3,
    candyYellow3
)

# testTextFont = pyg.font.SysFont(util.fonts.terminal, 30)
# testText = testTextFont.render("Glom Is An Ugly Creature...", True, (255, 255, 15))

eat_sound = pyg.mixer.Sound(seat)
explode_sound = pyg.mixer.Sound(sexplode)

loopA: bool = True
loopB: bool = True

root = tk.Tk()
def timey():
    time.sleep(1)

# main Pygame loop
def main_loop():
    # Prepare the candies
    gameTimer.tick()
    spawners.spawnCandies(candyHolder)
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                return

        screen.fill(pyg.Color("blue"))
        screen.blit(tex_bg, (0, 0))
        # screen.blit(testText, (250, 300))

        # ____________UPDATES SECTION________________#
        # Spawn the candies lol
        global loopA
        global loopB
        spawners.drawCandies(candyHolder, screen)

        if player.isDead == False:
            player.update(screen)
            movement.playerMovement2(player, screen)

        if enemy.isDead == False:
            enemy.update(screen)
            movement.autoMovement(enemy, screen)

        # Candy eating handler
        for candy in candyHolder:
            # Player
            if candy.rect.colliderect(player):
                if candy == candyMint or candy == candyMint1 or candy == candyMint2 or candy == candyMint3:
                    player.wid += 5
                    player.hei += 5
                    player.time -= 25
                    candy.kill()
                    pyg.mixer.Sound.play(eat_sound)
                if candy == candyChoco or candy == candyChoco1 or candy == candyChoco2 or candy == candyChoco3:
                    player.wid -= 25
                    player.hei -= 25
                    player.time -= 10
                    candy.kill()
                    pyg.mixer.Sound.play(eat_sound)
                else:
                    player.wid += 10
                    player.hei += 10
                    player.time += 10
                    candy.kill()
                    pyg.mixer.Sound.play(eat_sound)
            # Enemy
            if candy.rect.colliderect(enemy):
                if candy == candyMint:
                    enemy.wid += 5
                    enemy.hei += 5
                    enemy.time -= 25
                    candy.kill()
                    pyg.mixer.Sound.play(eat_sound)
                if candy == candyChoco:
                    enemy.wid -= 25
                    enemy.hei -= 25
                    enemy.time -= 10
                    candy.kill()
                    pyg.mixer.Sound.play(eat_sound)
                else:
                    enemy.wid += 10
                    enemy.hei += 10
                    enemy.time += 10
                    candy.kill()
                    pyg.mixer.Sound.play(eat_sound)

            if enemy.rect.colliderect(player) and loopA:
                if enemy.wid > player.wid and enemy.hei > player.hei:
                    enemy.wid = enemy.wid + player.wid
                    enemy.hei = enemy.hei + player.hei
                    player.kill()
                    loopA = False
                    pyg.mixer.Sound.play(eat_sound)
                    util.dieFunction(player)
                if enemy.wid < player.wid and enemy.hei < player.hei:
                    player.wid = player.wid + enemy.wid
                    player.hei = player.hei + enemy.hei
                    enemy.kill()
                    loopA = False
                    pyg.mixer.Sound.play(eat_sound)
                    util.winFunction(player)
                util.tieFunction(player, enemy)

        # Explode timer
        countTextFont = pyg.font.SysFont(util.fonts.bell_mt, 50)
        countText = countTextFont.render(f"{player.getTime()}", True, (0, 255, 0))
        screen.blit(countText, (player.x + 20, player.y - 40))
        if player.getTime() <= 0:
            util.explode(player, screen)
            if loopB:
                pyg.mixer.Sound.play(explode_sound)
                player.isDead = True
                loopB = False

        # ___________________________________________#

        pyg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    print("Glom is an ugly creature...")
    main_loop()
