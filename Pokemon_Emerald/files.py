import pygame
from sprites2 import *
pygame.mixer.init()
screen_width = 240
screen_height = 160
tile_size = 16
#################################################################################################################################
##SpriteSheet Data
x=0
y=0
s=[]
for variable in range (0, 6072):
    s.append([(x*16),(y*16),16,16])
    x+=1
    if x == 88:
        y+=1
        if variable != ((6072)-1):
                        x=0
######################Main Character#################
player_up_walk=[pygame.image.load('images/playersplit/back0.png'),pygame.image.load('images/playersplit/back1.png'),pygame.image.load('images/playersplit/back0.png'),pygame.image.load('images/playersplit/back2.png')]
player_down_walk=[pygame.image.load('images/playersplit/front0.png'),pygame.image.load('images/playersplit/front1.png'),pygame.image.load('images/playersplit/front0.png'),pygame.image.load('images/playersplit/front2.png')]
player_left_walk=[pygame.image.load('images/playersplit/side0.png'),pygame.image.load('images/playersplit/side1.png'),pygame.image.load('images/playersplit/side0.png'),pygame.image.load('images/playersplit/side2.png')]
player_right_walk=[pygame.transform.flip(pygame.image.load('images/playersplit/side0.png'),True,False),pygame.transform.flip(pygame.image.load('images/playersplit/side1.png'),True,False),pygame.transform.flip(pygame.image.load('images/playersplit/side0.png'),True,False),pygame.transform.flip(pygame.image.load('images/playersplit/side2.png'),True,False)]
player_still=[pygame.image.load('images/playersplit/front0.png'),pygame.image.load('images/playersplit/front0.png'),pygame.image.load('images/playersplit/front0.png'),pygame.image.load('images/playersplit/front0.png')]
player_up_run=[pygame.image.load('images/playersplit_run/back0.png'),pygame.image.load('images/playersplit_run/back1.png'),pygame.image.load('images/playersplit_run/back0.png'),pygame.image.load('images/playersplit_run/back2.png')]
player_down_run=[pygame.image.load('images/playersplit_run/front0.png'),pygame.image.load('images/playersplit_run/front1.png'),pygame.image.load('images/playersplit_run/front0.png'),pygame.image.load('images/playersplit_run/front2.png')]
player_left_run=[pygame.image.load('images/playersplit_run/side0.png'),pygame.image.load('images/playersplit_run/side1.png'),pygame.image.load('images/playersplit_run/side0.png'),pygame.image.load('images/playersplit_run/side2.png')]
player_right_run=[(pygame.transform.flip(pygame.image.load('images/playersplit_run/side0.png'),True,False)),(pygame.transform.flip(pygame.image.load('images/playersplit_run/side1.png'),True,False)),(pygame.transform.flip(pygame.image.load('images/playersplit_run/side0.png'),True,False)),(pygame.transform.flip(pygame.image.load('images/playersplit/side2.png'),True,False))]
player_walk = [player_left_walk,player_right_walk,player_up_walk,player_down_walk,player_still]
player_run = [player_left_run,player_right_run,player_up_run,player_down_run,player_still]
player_battle = [pygame.image.load('images/Trainer_battling_fight_0.png'),pygame.image.load('images/Trainer_battling_fight_1.png'),pygame.image.load('images/Trainer_battling_fight_2.png'),pygame.image.load('images/Trainer_battling_fight_3.png')]
######################Other Images#################
battle_scene = pygame.transform.scale((pygame.image.load('images/bg.png')),(screen_width,screen_height))
bg = pygame.transform.scale((pygame.image.load('images/Littleroot_town.png')),(screen_width,screen_height))
screenshot = pygame.image.load("images/screenshot.png")
ground_image = pygame.image.load('images/ground.png')
icon = pygame.image.load('images/rsz_icon.gif')
statusbar = pygame.image.load('images/health.png')
statusbar = pygame.transform.scale((statusbar),(100,29))
enemy_statusbar = pygame.image.load('images/enemyhealth.png')
enemy_statusbar = pygame.transform.scale((enemy_statusbar),(100,29))
Blastoise = [pygame.image.load('images/pokemon/Blastoise_0.png'),pygame.image.load('images/pokemon/Blastoise_1.png')]
Charizard = [pygame.image.load('images/pokemon/Charizard_0.png'),pygame.image.load('images/pokemon/Charizard_1.png')]
Groundon = [pygame.image.load('images/pokemon/Groundon_0.png'),pygame.image.load('images/pokemon/Groundon_1.png')]
Pikachu = [pygame.image.load('images/pokemon/Pikachu_0.png'),pygame.image.load('images/pokemon/Pikachu_1.png')]
Entei = [pygame.image.load('images/pokemon/Entei_0.png'),pygame.image.load('images/pokemon/Entei_1.png')]
Swampert = [pygame.image.load('images/pokemon/Swampert_0.png'),pygame.image.load('images/pokemon/Swampert_1.png')]





#################################################################################################################################
##Music
Litteroot_music = ("music/litteroot_intro.ogg","music/litteroot_loop.ogg")
Route101_music = ("music/Route_101_intro.ogg","music/Route_101_loop.ogg")
battle_music = ('music/battle_music_intro.ogg','music/battle_music_loop.ogg')








