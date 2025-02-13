#import raylibpy as rl
import pygame as pyg
import entity as en
import util
import soundload as sl

pyg.mixer.init()
bounce_sound = pyg.mixer.Sound(sl.sbounce)

speed = 3

#Movement for the player. Controled by user.
def playerMovement2(player: en.Entity, screen = None):
    """Movement for the player. Controled by user."""
    keys = pyg.key.get_pressed()
    if keys[pyg.K_a]:
        player.x -= speed
        player.r = 90
    if keys[pyg.K_d]:
        player.x += speed
        player.r = -90
    if keys[pyg.K_w]:
        player.y -= speed
        player.r = 0
    if keys[pyg.K_s]:
        player.y += speed
        player.r = 180

    # Collision with the edges
    if player.x > util.SCW - player.wid and player.x != 10000:
        player.x = util.SCW - player.wid
    if player.x < 0:
        player.x = 0
    if player.y > util.SCH - player.hei and player.y != 10000:
        player.y = util.SCH - player.hei
    if player.y < 0:
        player.y = 0
    #DEBUG: size controls
    # if keys[pyg.K_SPACE]:
    #     player.wid += 10
    #     player.hei += 10
    # if keys[pyg.K_LSHIFT]:
    #     player.wid -= 10
    #     player.hei -= 10

    #DEBUG: explode controls
    # if keys[pyg.K_e]:
    #     u.explode(player, screen)

    #DEBUG: kill controls
    # if keys[pyg.K_k]:
    #     player.kill()

def autoMovement(entity: en.Entity, sceen = None):

    if entity.vert == entity.VERT[0]:
        entity.y -= 2
    if entity.vert == entity.VERT[1]:
        entity.y += 2

    if entity.y > util.SCH - entity.hei and entity.y != 10000:
        entity.y = util.SCH - entity.hei
        entity.vert = entity.VERT[0]
        pyg.mixer.Sound.play(bounce_sound)
    if entity.y < 0:
        entity.y = 0
        entity.vert = entity.VERT[1]
        pyg.mixer.Sound.play(bounce_sound)


    if entity.horiz == entity.HORIZ[0]:
        entity.x -= 2
    if entity.horiz == entity.HORIZ[1]:
        entity.x += 2

    if entity.x > util.SCW - entity.wid and entity.x != 10000:
        entity.x = util.SCW - entity.wid
        entity.horiz = entity.HORIZ[0]
        pyg.mixer.Sound.play(bounce_sound)
    if entity.x < 0:
        entity.x = 0
        entity.horiz = entity.HORIZ[1]
        pyg.mixer.Sound.play(bounce_sound)