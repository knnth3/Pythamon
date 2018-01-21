#!/usr/bin/env python

import pygame, sys
from pygame.sprite import Sprite
from pygame.locals import *
from colors import *
from sprites2 import *
from files import *
import os
import random
from Cross_Fade import *

def set_message( text ):

	global message, previous_message

	message = font.render( text, True, black, white )
	previous_message = message

if ( __name__ == "__main__" ):
    pygame.init()

    screen_size = (screen_width,screen_height)
    screen = pygame.display.set_mode( screen_size, 0)

    pygame.display.set_caption( "PyThamon" )
    icon = icon.convert_alpha()
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()
    frames_per_second = 60
    tile_player_wants_to_be_on_x = 17
    tile_player_wants_to_be_on_y = 6
    active_object_list = pygame.sprite.Group()
    player = Player((tile_size*(tile_player_wants_to_be_on_x -1)),(tile_size*(tile_player_wants_to_be_on_y -1)))
    player_mimic = Player_mimic(player_walk,player_run,player)
    player_mimic.set_position( screen_width/2, (screen_height/2)-6)
    active_object_list.add( player, player_mimic )
    shadow = CrossFade(screen)
    fade = pygame.sprite.Group(shadow)
    current_level = Level_01(player,screen)
    Litteroot_Town = Invisible_Queue(transparent_alpha,1,(tile_size*0,tile_size*12,tile_size*60,tile_size*40))
    Route_101 = Invisible_Queue(transparent_alpha,2,(0,0,tile_size*60,tile_size*12))
    Litteroot_Town.load_sound("music/litteroot_intro.ogg","music/litteroot_loop.ogg")
    Route_101.load_sound("music/Route_101_intro.ogg","music/Route_101_loop.ogg")
    town_list = [Litteroot_Town,Route_101]
    current_level.add_sprites("location",town_list)
    player.level = current_level
    Battle_sprite = Battle(screen)
    Battle_music_sprite = Battle_music(battle_music[0],battle_music[1])

    font = pygame.font.SysFont( "Times New Roman", 12 )
    message = previous_message = None
    set_message( "" )

    running = True
    entered = False
    manual_switch = True
    running = True
    update = False
    number = 0
    selected = 0
    slow = 60
    fast = 30
    speed = slow
    health = 0
    enemy_health = 0
    player_pokemon_str = "No Pokemon"
    x = 0

    i = 0
    pygame.key.set_repeat(1, speed)

    def check_queues():
        switch = 0
        if (len(current_level.queue_list.sprites()) == None):
            switch = None
        else:
            switch = Event_block.switch_mode
        return switch


    while ( running ):
        if (check_queues() == True):
            if (entered == False):
                pygame.mixer.stop()
                Battle_music_sprite.sound_check()
                entered = True
            if (number <= 75):
                for event in pygame.event.get():
                    if (event.type==pygame.QUIT):
                        running = False
                if shadow.fade_dir == 1:
                    shadow.fade_dir *= -1
                    number +=1
                elif shadow.fade_dir == -1:
                    shadow.fade_dir *= -1
                    number+=1
                fade.clear(screen, screenshot)
                clock.tick( 30 )
                fade.update()

                fade.draw(screen)
            else:
                for event in pygame.event.get():
                    if (event.type==pygame.QUIT):
                        running = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        Event_block.switch_mode = False
                        number = 0
                        entered = False
                        Battle_sprite.number = 0
                        Battle.trigger0 = True
                        Battle.trigger1 = False
                        Battle.trigger2 = False
                        Battle_music_sprite.stop_sound()
                Battle_music_sprite.sound_check()
                enemy_pokemon = font.render(str(Event_block.pokemon_str),True,black)
                player_pokemon = font.render((player_pokemon_str),True,black)
                Battle_sprite.prepare_battle(Event_block.pokemon,enemy_pokemon,player_pokemon)
                if Battle.trigger0 == True:
                    Battle_sprite.intro()
                elif Battle.trigger1 == True:
                    Battle_sprite.bring_in_player()
                elif Battle.trigger2 == True:
                    Battle_sprite.send_out_pokemon_waiting()
                    inform = font.render('A wild ' + str(Event_block.pokemon_str) + ' has appeared but you',True,white)
                    inform2 = font.render('have no Pokemon! Press Enter to Flee',True,white)
                    screen.blit(inform,(15,120))
                    screen.blit(inform2,(15,133))
        else:
            for event in pygame.event.get():
                if (event.type==pygame.QUIT):
                    running = False
                if (event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_q):
                        player_mimic.run = True
                        player_mimic.fps = player_mimic.fast_fps
                        speed = fast
                        update = True
                    if(event.key == pygame.K_w):
                        player_mimic.run = False
                        player_mimic.fps = player_mimic.slow_fps
                        speed = slow
                        update = True
                if (event.type == pygame.KEYDOWN):
                    k = event.key
                    if(k == pygame.K_LEFT):
                        for x in range(0,(len(current_level.queue_list.sprites()))):
                            (current_level.queue_list.sprites())[x].entity_collision(player)
                        player.change_speed(-player.SPEED,0)
                        player_mimic.change_speed(-player.SPEED,0)
                    elif(k == pygame.K_RIGHT):
                        for x in range(0,(len(current_level.queue_list.sprites()))):
                            (current_level.queue_list.sprites())[x].entity_collision(player)
                        player.change_speed(player.SPEED,0)
                        player_mimic.change_speed(player.SPEED,0)
                    elif(k == pygame.K_UP):
                        for x in range(0,(len(current_level.queue_list.sprites()))):
                            (current_level.queue_list.sprites())[x].entity_collision(player)
                        player.change_speed(0,-player.SPEED)
                        player_mimic.change_speed(0,-player.SPEED)
                    elif(k == pygame.K_DOWN):
                        for x in range(0,(len(current_level.queue_list.sprites()))):
                            (current_level.queue_list.sprites())[x].entity_collision(player)
                        player.change_speed(0,player.SPEED)
                        player_mimic.change_speed(0,player.SPEED)
                    else:
                        player.change_speed(0,0)
                        player_mimic.change_speed(0,0)
                elif (event.type == pygame.KEYUP):
                    player.change_speed(0,0)
                    player_mimic.change_speed(0,0)
    
            Litteroot_Town.entity_collision(player)
            Route_101.entity_collision(player)
    	    player.update( current_level.collidable_list, event )
            player_mimic.update()
            if update == True:
                pygame.key.set_repeat(1, speed)
                update = False
    	    event = None

    	    current_level.update()

            current_level.scroll()


    	    current_level.draw( screen )
    	    active_object_list.draw( screen )


    	    clock.tick( frames_per_second )
            i += 1   
            pygame.display.update()

    pygame.quit()
