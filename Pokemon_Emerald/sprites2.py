import pygame, sys
from pygame.sprite import Sprite
from pygame.locals import *
from colors import *
import random
from files import *
pygame.mixer.init()

class Battle_music(pygame.sprite.Sprite):
    def __init__(self,sound1,sound2):
        self.mixer = pygame.mixer.Channel(4)
        self.loop = False
        self.sound1 = pygame.mixer.Sound(sound1)
        self.sound2 = pygame.mixer.Sound(sound2)
    def sound_check(self):
        if((self.mixer.get_busy() == False) and (self.loop == True)):
            self.mixer.play(self.sound2)
        elif((self.mixer.get_busy() == False) and (self.loop == False)):
            self.mixer.play(self.sound1)
            self.loop = True
        elif((self.mixer.get_busy() == True) and (self.loop == False)):
            return
        elif((self.mixer.get_busy() == True) and (self.loop == True)):
            return
    def stop_sound(self):
        self.loop = False
        self.mixer.fadeout(1000)
class Battle(pygame.sprite.Sprite):
    def __init__(self,screen):
        Battle.user_input = False
        Battle.trigger0 = True
        Battle.trigger1 = False
        Battle.trigger2 = False
        Battle.trigger3 = False
        Battle.trigger4 = False
        self.screen = screen
        self.pokemon = 0
        self.enemy_pokemon = 0
        self.player_pokemon = 0
        self.number = 0
        self.image_counter = 0
        self.frame = 250
        self.frame2 = 25
        self.x_axis = -75
        self.frame3 = 30
    def prepare_battle(self,pokemon,enemy,player):
        self.enemy_pokemon = enemy
        self.player_pokemon = player
        self.pokemon = pokemon
    def begining_counter(self):
        self.number += 1
        self.image_counter = (self.number/self.frame) % 2
        if self.number == 700:
            Battle.trigger0 = False
            Battle.trigger1 = True

    def intro(self):
        self.begining_counter()
        self.screen.blit(battle_scene,(0,0))
        self.screen.blit(enemy_statusbar,(13,16))
        self.screen.blit(statusbar,(126,74))
        self.screen.blit(self.enemy_pokemon,(20,20))
        self.screen.blit(self.player_pokemon,(145,77))
        self.screen.blit(self.pokemon[self.image_counter],(140,0))
    def bring_in_player(self):
        self.screen.blit(battle_scene,(0,0))
        self.screen.blit(self.pokemon[0],(140,0))
        self.screen.blit(enemy_statusbar,(13,16))
        self.screen.blit(statusbar,(126,74))
        self.screen.blit(self.enemy_pokemon,(20,20))
        self.screen.blit(self.player_pokemon,(145,77))
        for x in range (1,100):
            self.number += 1
            self.image_counter = ((self.number/self.frame2) % 100) + self.x_axis
            self.screen.blit(player_battle[0],(self.image_counter,58))
            if self.image_counter >15:
                self.number = 0
                self.image_counter = 0
                Battle.trigger1 = False
                Battle.trigger2 = True
    def send_out_pokemon_waiting(self):
        self.screen.blit(battle_scene,(0,0))
        self.screen.blit(self.pokemon[0],(140,0))
        self.screen.blit(enemy_statusbar,(13,16))
        self.screen.blit(statusbar,(126,74))
        self.screen.blit(self.enemy_pokemon,(20,20))
        self.screen.blit(self.player_pokemon,(145,77))
        self.screen.blit(player_battle[0],(16,58))
    def send_out_pokemon(self):
        self.screen.blit(battle_scene,(0,0))
        self.screen.blit(self.pokemon[0],(140,0))
        self.screen.blit(enemy_statusbar,(13,16))
        self.screen.blit(statusbar,(126,74))
        self.screen.blit(self.enemy_pokemon,(20,20))
        self.screen.blit(self.player_pokemon,(145,77))
        for x in range (1,100):
            self.number += 1
            self.image_counter = ((self.number/self.frame2) % 100) + self.x_axis
            self.screen.blit(player_battle[0],(self.image_counter,58))
            if self.image_counter >15:
                self.number = 0
                self.image_counter = 0
                Battle.trigger1 = False
                Battle.trigger2 = True
    def send_out_pokemon_2(self):
        self.screen.blit(battle_scene,(0,0))
        self.screen.blit(self.pokemon[0],(140,0))
        self.screen.blit(enemy_statusbar,(13,16))
        self.screen.blit(statusbar,(126,74))
        self.screen.blit(self.enemy_pokemon,(20,20))
        self.screen.blit(self.player_pokemon,(145,77))
        self.screen.blit(player_battle[0],(16,58))
class SpriteSheet(object):
    sprite_sheet = None
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
    def get_image(self,properties):
        image = pygame.Surface([properties[2], properties[3]]).convert()
        image.blit(self.sprite_sheet, (0, 0), (properties[0], properties[1], properties[2], properties[3]))
        image.set_colorkey(black)
        return image

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Player,self).__init__()
        self.frame = 0
        self.image = pygame.Surface((16,16),SRCALPHA).convert_alpha()
        self.image.fill(transparent_alpha)
        self.set_properties()
        self.walk = 16
        self.run = 32
        self.SPEED = self.walk
        self.level = None
        self.fps = 8
        self.rect.x = x
        self.rect.y = y
        self.hspeed = 0
        self.vspeed = 0
    def set_properties(self):
        self.rect = self.image.get_rect()
        self.rect.width = 16
        self.rect.height = 16
    def change_speed(self,hspeed,vspeed):
        self.hspeed = hspeed
        self.vspeed = vspeed
        self.rect.x += hspeed
        self.rect.y += vspeed
    def update(self,collidable,event = None):
        collision_list = pygame.sprite.spritecollide(self,collidable,False)
        for collision in collision_list:
            if (self.hspeed > 0):
                self.rect.right = collision.rect.left
            elif (self.hspeed< 0):
                self.rect.left = collision.rect.right
        collision_list = pygame.sprite.spritecollide(self,collidable,False)
        for collision in collision_list:
            if (self.vspeed > 0):
                self.rect.bottom = collision.rect.top
            elif (self.vspeed< 0):
                self.rect.top = collision.rect.bottom

class Player_mimic(pygame.sprite.Sprite):
    def __init__(self,character_walk,character_run,player):
        super(Player_mimic,self).__init__()
        self.mimic = player
        self.character_walk = character_walk
        self.character_run = character_run
        self.frame = 0
        self.image = (self.side("down")[self.frame])
        self.set_properties()
        self.hspeed = 0
        self.vspeed = 0
        self.image_counter = 0
        self.run = False
        self.SPEED = 16
        self.direction = 0
        self.level = None
        self.slow_fps = 8
        self.fast_fps = 4
        self.fps = self.slow_fps
    def set_properties(self):
        self.rect = self.image.get_rect()
    def change_speed(self,hspeed,vspeed):
        self.hspeed = hspeed
        self.vspeed = vspeed
    def set_position(self,x,y):
        self.rect.x = x
        self.rect.y = y
    def set_image(self,filename = None):
        if (filename!= None):
            self.image = pygame.image.load(filename)
            self.set_properties()
            player.set_image(os.path.join("images/playersplit","front0.png"))
    def counter(self,idle = False):
        if (idle == True):
            self.image_counter = 0
        else:
            self.frame += 1
            self.image_counter = (self.frame / self.fps) % 4
    def side(self,side = 0):
        self.direction = side
        if (self.direction == 0):
            return self.character_walk[4]
        if (self.direction == "left"):
            return self.character_walk[0]
        if (self.direction == "right"):
            return self.character_walk[1]
        if (self.direction == "up"):
            return self.character_walk[2]
        if (self.direction == "down"):
            return self.character_walk[3]
        if (self.direction == "left_run"):
            return self.character_run[0]
        if (self.direction == "right_run"):
            return self.character_run[0]
        if (self.direction == "up_run"):
            return self.character_run[2]
        if (self.direction == "down_run"):
            return self.character_run[3]
    def rest(self):
        if (self.direction == "left_run"):
            self.direction = "left"
        if (self.direction == "right_run"):
            self.direction = "right"
        if (self.direction == "up_run"):
            self.direction = "up"
        if (self.direction == "down_run"):
            self.direction = "down"
    def update(self):
        if ((self.hspeed == -self.SPEED) & (self.vspeed == 0) & (self.run == False)):
            self.image = (self.side("left")[self.image_counter])
            self.counter()
        if ((self.hspeed == self.SPEED) & (self.vspeed == 0) & (self.run == False)):
            self.image = (self.side("right")[self.image_counter])
            self.counter()
        if ((self.hspeed == 0) & (self.vspeed == -self.SPEED) & (self.run == False)):
            self.image = (self.side("up")[self.image_counter])
            self.counter()
        if ((self.hspeed == 0) & (self.vspeed == self.SPEED) & (self.run == False)):
            self.image = (self.side("down")[self.image_counter])
            self.counter()
        if ((self.hspeed == -self.SPEED) & (self.vspeed == 0) & (self.run == True)):
            self.image = (self.side("left_run")[self.image_counter])
            self.counter()
        if ((self.hspeed == self.SPEED) & (self.vspeed == 0) & (self.run == True)):
            self.image = (pygame.transform.flip((self.side("right_run")[self.image_counter]),True,False))
            self.counter()
        if ((self.hspeed == 0) & (self.vspeed == -self.SPEED) & (self.run == True)):
            self.image = (self.side("up_run")[self.image_counter])
            self.counter()
        if ((self.hspeed == 0) & (self.vspeed == self.SPEED) & (self.run == True)):
            self.image = (self.side("down_run")[self.image_counter])
            self.counter()
        if ((self.hspeed == 0) & (self.vspeed == 0)):
            self.rest()
            self.image = (self.side(self.direction)[self.image_counter])
            self.counter(True)

class No_entry_block(pygame.sprite.Sprite):
    def __init__(self,properties):
        super(No_entry_block,self).__init__()
        self.sprite_image = properties[2]
        self.override_image()
        self.rect = self.image.get_rect()
        self.set_position(properties[0],properties[1])
    def set_position(self,x,y):
        self.rect.x = x
        self.rect.y = y
    def override_image(self):
        self.sprite_image = (pygame.transform.scale((self.sprite_image),(16,16)))
        self.image = self.sprite_image

class Event_block(pygame.sprite.Sprite):
    def __init__(self,properties):
        super(Event_block,self).__init__()
        self.sprite_image = properties[4]
        self.override_image()
        self.rect = self.image.get_rect()
        self.entity = 0
        self.func = properties[1]
        self.move_char_x = 0
        self.move_char_y = 0
        self.running = True
        self.screen = properties[0]
        self.set_position(properties[2],properties[3])
        Event_block.switch_mode = False
        Event_block.pokemon = Charizard
        Event_block.pokemon_str = "Charizard"
    def set_position(self,x,y):
        self.rect.x = x
        self.rect.y = y
    def override_image(self):
        self.sprite_image = (pygame.transform.scale((self.sprite_image),(16,16)))
        self.image = self.sprite_image
    def entity_collision(self,entity,x = False,y = False):
        self.entity = entity
        if(pygame.sprite.collide_rect(self.entity,self)):
            if (self.func == "battle"):
                self.dice_roll()
            elif (self.func == "teleport"):
                self.teleport(self.move_char_x,self.move_char_y)

                self.teleport(self.move_char_x,self.move_char_y)
    def teleport(self,x,y):
        self.entity.rect.x = x
        self.entity.rect.y = y
    def dice_roll(self):
        chance = random.randint(0,18750)
        if (chance <= 125):
            pygame.image.save(self.screen, "images/screenshot.png")
            Event_block.switch_mode = True
            Event_block.pokemon = Groundon
            Event_block.pokemon_str = "Groundon"
        elif (chance <= 333):
            pygame.image.save(self.screen, "images/screenshot.png")
            Event_block.switch_mode = True
            Event_block.pokemon = Entei
            Event_block.pokemon_str = "Entei"
        elif (chance <= 675):
            pygame.image.save(self.screen, "images/screenshot.png")
            Event_block.switch_mode = True
            Event_block.pokemon = Pikachu
            Event_block.pokemon_str = "Pikachu"
        elif (chance <= 850):
            pygame.image.save(self.screen, "images/screenshot.png")
            Event_block.switch_mode = True
            Event_block.pokemon = Swampert
            Event_block.pokemon_str = "Swampert"
        elif (chance <= 1000):
            pygame.image.save(self.screen, "images/screenshot.png")
            Event_block.switch_mode = True
            Event_block.pokemon = Charizard
            Event_block.pokemon_str = "Charizard"

class Invisible_Queue(pygame.sprite.Sprite):
    def __init__(self,color,channel,(x,y,width,height)):
        super(Invisible_Queue,self).__init__()
        self.image = pygame.Surface((width,height),SRCALPHA).convert_alpha()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.sound1 = 0
        self.sound2 = 0
        self.mixer = 0
        self.entity = 0
        self.loop = False
        self.channel = channel
        self.width = width
        self.height = height
        self.rect.x = x
        self.rect.y = y
    def load_sound(self,filename = None,filename2 = None):
        if (filename!= None):
            self.sound1 = pygame.mixer.Sound(filename)
            self.sound2 = pygame.mixer.Sound(filename2)
            self.mixer = pygame.mixer.Channel(self.channel)
    def entity_collision(self,entity):
        self.entity = entity
        if(pygame.sprite.collide_rect(self.entity,self)):
            self.play_sound()
        else:
            self.stop_sound()


    def play_sound(self):
        if((self.mixer.get_busy() == False) and (self.loop == True)):
            self.mixer.play(self.sound2)
        elif((self.mixer.get_busy() == False) and (self.loop == False)):
            self.mixer.play(self.sound1,0,fade_ms=500)
            self.loop = True
        elif((self.mixer.get_busy() == True) and (self.loop == False)):
            return
        elif((self.mixer.get_busy() == True) and (self.loop == True)):
            return
    def stop_sound(self):
        self.loop = False
        self.mixer.fadeout(1000)


class Block( pygame.sprite.Sprite ):
    def __init__( self,properties):
        super( Block, self ).__init__()
        self.sprite_image = properties[2]
        self.override_image()
        self.rect = self.image.get_rect()
        self.set_position(properties[0],properties[1])

    def override_image(self):
        self.sprite_image = (pygame.transform.scale((self.sprite_image),(16,16)))
        self.image = self.sprite_image
    def set_position(self,x,y):
        self.rect.x = x
        self.rect.y = y

class Level( object ):

        def __init__( self, player_object ):

                self.collidable_list = pygame.sprite.Group()
                self.object_list = pygame.sprite.Group()
                self.queue_list = pygame.sprite.Group()
                self.location_list = pygame.sprite.Group()
                self.infront_list = pygame.sprite.Group()

                self.player_object = player_object
                self.change_x = 0
                self.change_y = 0
                self.left_camera = screen_width/2
                self.right_camera = screen_width/2
                self.up_camera = screen_height/2
                self.down_camera = screen_height/2

        def update( self ):
                self.collidable_list.update()
                self.object_list.update()
                self.queue_list.update()
                self.location_list.update()
                self.infront_list.update()

        def draw( self, window ):

                window.fill( black )

                self.collidable_list.draw( window )
                self.object_list.draw( window )
                self.queue_list.draw( window )
                self.location_list.draw( window )
        def camera_view(self,change_x,change_y):
            self.change_x += change_x
            self.change_y += change_y
            for each_object in self.object_list:
                each_object.rect.x +=change_x
                each_object.rect.y +=change_y
            for each_object in self.collidable_list:
                each_object.rect.x +=change_x
                each_object.rect.y +=change_y
            for each_object in self.queue_list:
                each_object.rect.x +=change_x
                each_object.rect.y +=change_y
            for each_object in self.location_list:
                each_object.rect.x +=change_x
                each_object.rect.y +=change_y
        def scroll(self):
            if (self.player_object.rect.x <= self.left_camera):
                view_difference = self.left_camera - self.player_object.rect.x
                self.player_object.rect.x = self.left_camera
                self.camera_view(view_difference,0)

            if (self.player_object.rect.x >= self.right_camera):
                view_difference = self.right_camera - self.player_object.rect.x
                self.player_object.rect.x = self.right_camera
                self.camera_view(view_difference,0)

            if (self.player_object.rect.y <= self.up_camera):
                view_difference = self.up_camera - self.player_object.rect.y
                self.player_object.rect.y = self.up_camera
                self.camera_view(0,view_difference)

            if (self.player_object.rect.y >= self.down_camera):
                view_difference = self.down_camera - self.player_object.rect.y
                self.player_object.rect.y = self.down_camera
                self.camera_view(0,view_difference)

class Level_01( Level ):
    def __init__( self, player_object ,screen):
        super( Level_01, self ).__init__( player_object )
        sprite_sheet = SpriteSheet('images/Exterior_Tileset.png')
        TILESIZE = 16
        ROWS = 65
        COLUMNS = 40
        MAPHEIGHT = ROWS
        MAPWIDTH = COLUMNS
        #No_Entry_Block(non_passable) = [x,y,image]
        #Block(passable) = [x,y,image]
        #Event_Block(grass) = [screen,type("battle" or "teleport"),x,y,image]
        ##Invisible_Queue is inserted in main game file because it is an indicator of a town and can be resised easily to fit an area.

        Tiles = {
          }
        for x in range(0, 6072):
          if x not in Tiles:
           Tiles[x] = [0,0,(sprite_sheet.get_image(s[x]))]

        Tiles[93] = [screen,"battle",0,0,(sprite_sheet.get_image(s[93]))]


        tile_map = [
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3520, 3168, 3169, 3170, 3522, 1, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 2118, 2118, 2118, 2118, 2118],
            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 3520, 3168, 3169, 3170, 3522, 1, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3520, 3168, 3169, 3170, 3522, 1, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 2118, 2118, 2118, 2118, 2118],
            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 3520, 3168, 3169, 3170, 3522, 1, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3520, 2466, 2466, 2466, 3522, 1, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 2118, 2118, 2118, 2118, 2118],
            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 3520, 3168, 3169, 3170, 3522, 1, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3520, 3168, 3169, 3170, 3522, 1, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 2118, 2118, 2118, 2118, 2118],
            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 3520, 3168, 3169, 3170, 3522, 1, 120, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3520, 3168, 3169, 3170, 3522, 1, 1, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 2118, 2118, 2118, 2118, 2118],
            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 3520, 3168, 3169, 3170, 3522, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 4, 1, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3520, 3168, 3169, 3170, 3522, 1, 4, 440, 441, 441, 443, 1, 1, 792, 793, 794, 795, 1, 4, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 2118, 2118, 2118, 2118, 2118],

            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 3520, 3168, 3169, 3170, 3522, 1, 1, 528, 529, 530, 531, 1, 1, 880, 881, 882, 883, 1, 1, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 181, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3520, 2904, 2905, 2906, 3522, 4, 1, 616, 617, 618, 619, 1, 4, 968, 969, 970, 971, 1, 1, 181, 181, 181, 181, 181, 181, 181, 181, 181, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 181, 181, 181, 181, 181, 181, 181, 181, 2118, 2118, 2118, 2118, 2118],
            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 3520, 2904, 2905, 2906, 3522, 4, 1, 1056, 705, 706, 707, 3609, 3609, 1056, 1057, 1058, 1059, 1, 1, 120, 120, 120, 120, 120, 120, 120, 120, 120, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 120, 120, 120, 120, 120, 120, 120, 120, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3520, 2904, 2905, 2906, 3522, 1, 3522, 2816, 2817, 2817, 2817, 2817, 2817, 2817, 2817, 2818, 3520, 1, 1, 1, 1, 1, 1, 1, 1, 94, 94, 94, 182, 182, 182, 182, 182, 182, 182, 182, 182, 182, 94, 94, 94, 94, 94, 94, 94, 94, 2118, 2118, 2118, 2118, 2118],
            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 3520, 2904, 2905, 2906, 3522, 1, 3522, 2904, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2906, 3520, 1, 1, 94, 94, 94, 94, 94, 94, 182, 182, 182, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 182, 182, 182, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3520, 2904, 2905, 2906, 3522, 1, 3522, 2904, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2906, 3520, 1, 1, 182, 182, 182, 2118, 2118, 182, 1, 93, 1, 93, 93, 93, 1, 93, 93, 1, 93, 1, 93, 93, 93, 1, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 3520, 2904, 2905, 2906, 3347, 3609, 3610, 2904, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2906, 3608, 3609, 3609, 3609, 3609, 3434, 182, 182, 93, 1, 93, 1, 93, 93, 93, 93, 1, 1, 93, 1, 1, 1, 93, 93, 93, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3520, 2904, 2905, 2905, 2817, 2817, 2817, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2906, 3522, 93, 93, 93, 1, 93, 93, 93, 1, 93, 1, 1, 93, 93, 93, 93, 93, 93, 1, 1, 182,  2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 3520, 2904, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2906, 1, 93, 93, 93, 93, 1, 1, 93, 1, 93, 93, 93, 1, 1, 1, 93, 93, 93, 93, 93, 93,  2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3520, 2992, 2993, 2993, 2993, 2993, 2993, 2993, 2993, 2993, 2993, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2906, 93, 1, 93, 93, 1, 93, 1, 93, 1, 93, 93, 93, 93, 93, 1, 93, 1, 93, 93, 93, 1, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 3608, 3609, 3609, 3609, 3609, 3609, 3609, 3609, 3609, 3609, 3434, 2904, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2906, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 1, 1, 93, 93, 93, 93, 93, 1, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3522, 2904, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2906, 1, 93, 93, 1, 1, 1, 1, 93, 93, 93, 1, 93, 93, 93, 93, 93, 93, 93, 93, 1, 93, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3522, 2904, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2906, 3434, 94, 94, 94, 94, 94, 93, 93, 93, 93, 93, 93, 93, 93, 93, 1, 1, 93, 93, 1, 1, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3522, 2904, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2906, 3522, 2118, 2118, 2118, 2118, 2118, 93, 93, 93, 93, 93, 93, 1, 1, 1, 93, 93, 93, 93, 93, 93, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 3522, 2904, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2906, 3522, 2118, 2118, 2118, 2118, 2118, 1, 93, 1, 93, 93, 93, 93, 93, 93, 93, 1, 93, 93, 93, 93, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3522, 2904, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2906, 3522, 2118, 2118, 2118, 2118, 2118, 94, 94, 94, 93, 1, 93, 93, 1, 93, 1, 93, 93, 1, 93, 93, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 5198, 5199, 3522, 2904, 2993, 2905, 2905, 2905, 2905, 2905, 2905, 2905, 2906, 3522, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 1, 93, 93, 93, 93, 1, 93, 93, 93, 93, 1, 93, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 5110, 5111, 3522, 3609, 3520, 2992, 2993, 2993, 2993, 2993, 2993, 2993, 2994, 3522, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 1, 93, 1, 93, 93, 1, 93, 93, 93, 1, 93, 93, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],

##bottom 11 lines (start of cave end of fence)
            [2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 2295, 1149, 1146, 3608, 3609, 3609, 3609, 3609, 1, 1, 1, 1, 3610, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 94, 94, 94, 94, 94, 93, 93, 93, 93, 93, 93, 93, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [2030, 2030, 2030, 2030, 2030, 2030, 2030, 2030, 2030, 2030, 2030, 2030, 2030, 2030, 1149, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 1234, 94, 94, 94, 94, 94, 1, 1, 1, 1, 94, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 94, 94, 1, 93, 1, 94, 94, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 1234, 2118, 2118, 2118, 2118, 2118, 1, 1, 1, 1, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 94, 94, 94, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 2383, 1236, 1324, 1324, 1324, 1324, 1679, 1324, 1324, 1325, 1234, 2118, 2118, 2118, 2118, 2118, 1, 1, 1, 1, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [1233, 1233, 1233, 1233, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 2383, 2559, 1236, 2471, 2471, 2471, 1767, 2471, 2471, 2471, 1322, 182, 182, 182, 182, 182, 1, 1, 1, 1, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [1233, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 2383, 2559, 4231, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [1233, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 2383, 2559, 4231, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 2383, 2383, 2383, 2295, 2295, 2295, 2295, 2295, 2295, 1149, 1146, 94, 94, 94, 94, 94, 94, 94, 94, 94, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 4231, 182, 182, 182, 182, 182, 182, 182, 182, 182, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 4231, 94, 94, 94, 94, 94, 94, 94, 94, 94, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],
            [2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2383, 2559, 4231, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118, 2118],

                      ]
        x=0
        y=0
        for constant in range(0,ROWS*COLUMNS):
            if (tile_map[x][y] == 1 ) \
            or (tile_map[x][y] == 4 ) \
            or (tile_map[x][y] == 3168 ) \
            or (tile_map[x][y] == 3169 ) \
            or (tile_map[x][y] == 3170 ) \
            or (tile_map[x][y] == 2816 ) \
            or (tile_map[x][y] == 2817 ) \
            or (tile_map[x][y] == 2818 ) \
            or (tile_map[x][y] == 2904 ) \
            or (tile_map[x][y] == 2905 ) \
            or (tile_map[x][y] == 2906 ) \
            or (tile_map[x][y] == 2992 ) \
            or (tile_map[x][y] == 2993 ) \
            or (tile_map[x][y] == 2994 ):
                tile = Block(Tiles[tile_map[x][y]])
                tile.set_position(y*TILESIZE,x*TILESIZE)
                self.object_list.add(tile)
            elif (tile_map[x][y] == 93):
                tile = Event_block(Tiles[tile_map[x][y]])
                tile.set_position(y*TILESIZE,x*TILESIZE)
                self.queue_list.add(tile)
            else:
                tile = No_entry_block(Tiles[tile_map[x][y]])
                tile.set_position(y*TILESIZE,x*TILESIZE)
                self.collidable_list.add(tile)
            y+=1
            if y == ROWS:
                x+=1
                if constant != ((ROWS*COLUMNS)-1):
                    y=0





    def add_sprites(self,group,array):
        if (group == "passable"):
            self.object_list.add( array )
        elif (group == "tangible"):
            self.collidable_list.add( array )
        elif (group == "location"):
            self.location_list.add( array )




