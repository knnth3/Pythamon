import pygame
from core.levels.level1 import Level1
from core.sprites import Event_block, LevelSubArea, Player, PlayerVisual
from core.states.battlestate import BattleState
from core.states.statemachine import GameState
from core.colors import *
from core.files import *

class Controls(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        
    def gety(self):
        if self.up and self.down:
            return 0

        if self.up:
            return -1

        if self.down:
            return 1
        
        return 0

    def getx(self):
        if self.left and self.right:
            return 0

        if self.left:
            return -1

        if self.right:
            return 1
        
        return 0

class MainState(GameState):
    def __init__(self, screen):
        super(MainState, self).__init__()
        start_location = (17, 6)
        self.player = Player((tile_size*(start_location[0] - 1)),(tile_size*(start_location[1] - 1)))
        self.player_visual = PlayerVisual(player_walk, player_run)
        self.player_visual.set_position( screen_width/2, (screen_height/2)-6)
        self.subareas: list[LevelSubArea] = []
        self.current_level = Level1(self.player, screen)

        litteroot_town = LevelSubArea("Litteroot Town", transparent_alpha, pygame.mixer.Channel(1), (tile_size*0,tile_size*12,tile_size*60,tile_size*40))
        litteroot_town.set_music("music/litteroot_intro.ogg","music/litteroot_loop.ogg")
        self.current_level.add_sprites("location", [litteroot_town])
        self.subareas.append(litteroot_town)

        route_101 = LevelSubArea("Route 101", transparent_alpha, pygame.mixer.Channel(2), (0,0,tile_size*60,tile_size*12))
        route_101.set_music("music/Route_101_intro.ogg","music/Route_101_loop.ogg")
        self.current_level.add_sprites("location", [route_101])
        self.subareas.append(route_101)
        
        self.player.level = self.current_level
        self.screen = screen
        self.slow = 1
        self.fast = 3
        self.active_object_list = pygame.sprite.Group()
        self.active_object_list.add(self.player, self.player_visual)
        self.controls = Controls()

    def onEnable(self):
        print("Main State was enabled!")
        self.make_player_walk()
        self.controls.reset()
        self.player_visual.change_direction(0, 0)

    def onDisable(self):
        print("Main State was disabled!")

    def make_player_run(self):
        self.player_visual.run = True
        self.player_visual.fps = self.player_visual.fast_fps
        self.player.change_speed(self.fast)

    def make_player_walk(self):
        self.player_visual.run = False
        self.player_visual.fps = self.player_visual.slow_fps
        self.player.change_speed(self.slow)

    def switch_to_battle(self):
        Event_block.switch_mode = False
        self.controls.reset()
        pygame.image.save(self.screen, "images/screenshot.png")
        self.activateNewState(BattleState(self.screen))

        for subarea in self.subareas:
            subarea.disable()

        print("disabled")

    def onUpdate(self, deltaTime, events):
        if Event_block.switch_mode:
            self.switch_to_battle()
            return

        for event in events:
            if (event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_q):
                    self.make_player_run()
                if(event.key == pygame.K_w):
                    self.make_player_walk()
            if (event.type == pygame.KEYDOWN):
                k = event.key
                if(k == pygame.K_LEFT):
                    for x in range(0,(len(self.current_level.queue_list.sprites()))):
                        (self.current_level.queue_list.sprites())[x].entity_collision(self.player)
                    self.controls.left = True
                elif(k == pygame.K_RIGHT):
                    for x in range(0,(len(self.current_level.queue_list.sprites()))):
                        (self.current_level.queue_list.sprites())[x].entity_collision(self.player)
                    self.controls.right = True
                elif(k == pygame.K_UP):
                    for x in range(0,(len(self.current_level.queue_list.sprites()))):
                        (self.current_level.queue_list.sprites())[x].entity_collision(self.player)
                    self.controls.up = True
                elif(k == pygame.K_DOWN):
                    for x in range(0,(len(self.current_level.queue_list.sprites()))):
                        (self.current_level.queue_list.sprites())[x].entity_collision(self.player)
                    self.controls.down = True
            elif (event.type == pygame.KEYUP):
                k = event.key
                if(k == pygame.K_LEFT):
                    self.controls.left = False
                elif(k == pygame.K_RIGHT):
                    self.controls.right = False
                elif(k == pygame.K_UP):
                    self.controls.up = False
                elif(k == pygame.K_DOWN):
                    self.controls.down = False

        for subarea in self.subareas:
            subarea.entity_collision(self.player)

        self.player.direction[0] = self.controls.getx();
        self.player.direction[1] = self.controls.gety();
        self.player.update(self.current_level.collidable_list, deltaTime)
        self.player_visual.change_direction(self.player.direction[0], self.player.direction[1])
        self.player_visual.update()

        self.current_level.update()
        self.current_level.scroll()
        self.current_level.draw(self.screen)
        self.active_object_list.draw(self.screen)

