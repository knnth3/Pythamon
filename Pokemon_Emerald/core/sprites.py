import pygame, random, os, math
from pygame.locals import *
from core.colors import *
from core.files import *
from core.sound import Sound, SoundGroup
from gamelayout.maps import *

class Battle(pygame.sprite.Sprite):
    def __init__(self,screen: pygame.Surface):
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
    def prepare_battle(self, pokemon, enemy, player):
        self.enemy_pokemon = enemy
        self.player_pokemon = player
        self.pokemon = pokemon

    def begining_counter(self):
        self.number += 1
        self.image_counter = math.floor((self.number/self.frame) % 2)
        if self.number == 300:
            Battle.trigger0 = False
            Battle.trigger1 = True

    def intro(self):
        self.begining_counter()
        self.screen.blit(battle_scene,(0,0))
        self.screen.blit(enemy_statusbar,(13,16))
        self.screen.blit(statusbar,(126,74))
        self.screen.blit(self.enemy_pokemon,(20,21))
        self.screen.blit(self.player_pokemon,(145,79))
        self.screen.blit(self.pokemon[self.image_counter],(140,0))

    def bring_in_player(self):
        self.screen.blit(battle_scene,(0,0))
        self.screen.blit(self.pokemon[0],(140,0))
        self.screen.blit(enemy_statusbar,(13,16))
        self.screen.blit(statusbar,(126,74))
        self.screen.blit(self.enemy_pokemon,(20,21))
        self.screen.blit(self.player_pokemon,(145,79))
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
        self.screen.blit(self.enemy_pokemon,(20,21))
        self.screen.blit(self.player_pokemon,(145,79))
        self.screen.blit(player_battle[0],(16,58))

    def send_out_pokemon(self):
        self.screen.blit(battle_scene,(0,0))
        self.screen.blit(self.pokemon[0],(140,0))
        self.screen.blit(enemy_statusbar,(13,16))
        self.screen.blit(statusbar,(126,74))
        self.screen.blit(self.enemy_pokemon,(20,21))
        self.screen.blit(self.player_pokemon,(145,79))
        
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
        self.direction = [0, 0]
    def set_properties(self):
        self.rect = self.image.get_rect()
        self.rect.width = 16
        self.rect.height = 16

    def change_speed(self, speed):
        self.speed = math.floor(speed)

    def get_direction_parsed(self):
        if (self.direction[0] == 0 and self.direction[1] == 0):
            return [0, 0]
        if (self.direction[0] == 0 and self.direction[1] == -1):
            return [0, -1]
        if (self.direction[0] == 0 and self.direction[1] == 1):
            return [0, 1]
        if (self.direction[0] == -1):
            return [-1, 0]
        if (self.direction[0] == 1):
            return [1, 0]

    def update(self, collidable, deltaTime):
        parsed = self.get_direction_parsed()
        new_x = (parsed[0] * self.speed)
        new_y = (parsed[1] * self.speed)
        self.rect.x += new_x
        self.rect.y += new_y
        collision_list = pygame.sprite.spritecollide(self,collidable,False)
        for collision in collision_list:
            if (self.direction[0] > 0):
                self.rect.right = collision.rect.left
            elif (self.direction[0] < 0):
                self.rect.left = collision.rect.right
        collision_list = pygame.sprite.spritecollide(self,collidable,False)
        for collision in collision_list:
            if (self.direction[1]  > 0):
                self.rect.bottom = collision.rect.top
            elif (self.direction[1]< 0):
                self.rect.top = collision.rect.bottom

class PlayerVisual(pygame.sprite.Sprite):
    def __init__(self, character_walk, character_run):
        super(PlayerVisual,self).__init__()
        self.character_walk = character_walk
        self.character_run = character_run
        self.frame = 0
        self.image = (self.get_movement_frames("down")[self.frame])
        self.set_properties()
        self.image_counter = 0
        self.run = False
        self.SPEED = 16
        self.direction = [0, 0]
        self.lastdirection = [0, 0]
        self.level = None
        self.slow_fps = 10
        self.fast_fps = 6
        self.fps = self.slow_fps
        self.update()

    def set_properties(self):
        self.rect = self.image.get_rect()

    def change_direction(self, x, y):
        self.direction = (x, y)
        if not(x == 0 and y == 0):
            self.lastdirection = (x, y)

    def set_position(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def set_running(self, value: bool = True):
        if value:
            self.fps = self.fast_fps
        else:
            self.fps = self.slow_fps

    def counter(self,idle = False):
        if (idle == True):
            self.image_counter = 0
        else:
            self.frame += 1
            self.image_counter = math.floor((self.frame / self.fps) % 4)

    def get_direction_text(self, direction):
        if (direction[0] == 0 and direction[1] == 0):
            if not(self.lastdirection[0] == 0 and self.lastdirection[1] == 0):
                return self.get_direction_text(self.lastdirection)
            return "none"
        if (direction[0] == 0 and direction[1] == -1):
            return "up"
        if (direction[0] == 0 and direction[1] == 1):
            return "down"
        if (direction[0] == -1):
            return "left"
        if (direction[0] == 1):
            return "right"

    def get_movement_frames(self, side = "none"):
        if (side == "none"):
            return self.character_walk[4]
        if (side == "left"):
            return self.character_walk[0]
        if (side == "right"):
            return self.character_walk[1]
        if (side == "up"):
            return self.character_walk[2]
        if (side == "down"):
            return self.character_walk[3]
        if (side == "left_run"):
            return self.character_run[0]
        if (side == "right_run"):
            return self.character_run[1]
        if (side == "up_run"):
            return self.character_run[2]
        if (side == "down_run"):
            return self.character_run[3]

    def update(self):
        direction_text = self.get_direction_text(self.direction);
        is_idle = (self.direction[0] == 0 and self.direction[1] == 0)
        if (not is_idle and self.run and direction_text != "none"):
            direction_text = direction_text + "_run"
        
        self.image = (self.get_movement_frames(direction_text)[self.image_counter])
        self.counter(is_idle)

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
            Event_block.switch_mode = True
            Event_block.pokemon = Groundon
            Event_block.pokemon_str = "Groundon"
        elif (chance <= 333):
            Event_block.switch_mode = True
            Event_block.pokemon = Entei
            Event_block.pokemon_str = "Entei"
        elif (chance <= 675):
            Event_block.switch_mode = True
            Event_block.pokemon = Pikachu
            Event_block.pokemon_str = "Pikachu"
        elif (chance <= 850):
            Event_block.switch_mode = True
            Event_block.pokemon = Swampert
            Event_block.pokemon_str = "Swampert"
        elif (chance <= 1000):
            Event_block.switch_mode = True
            Event_block.pokemon = Charizard
            Event_block.pokemon_str = "Charizard"

class LevelSubArea(pygame.sprite.Sprite):
    def __init__(self, name, color, music_channel, dimensions):
        super(LevelSubArea, self).__init__()
        (x,y,width,height) = dimensions
        self.name = name
        self.image = pygame.Surface((width,height),SRCALPHA).convert_alpha()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.music = None
        self.music_channel = music_channel
        self.width = width
        self.height = height
        self.rect.x = x
        self.rect.y = y
        self.sounds = SoundGroup(self.name)
        self.active = False

    def set_music(self, start_sound: str, loop_sound: str):
        self.sounds.add_sound(Sound(self.music_channel, start_sound))
        self.sounds.add_sound(Sound(self.music_channel, loop_sound, True))

    def entity_collision(self, entity):
        has_collision = pygame.sprite.collide_rect(entity, self)
        if (self.active != has_collision):
            self.active = has_collision
            if self.active:
                self.sounds.play()
            else:
                self.sounds.stop()

    def update(self):
        self.sounds.update()

    def disable(self):
        self.active = False
        self.sounds.stop()

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

Event_block.switch_mode = False
Event_block.pokemon = Charizard
Event_block.pokemon_str = "Charizard"