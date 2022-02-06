import pygame
from core.sound import Sound, SoundGroup
from core.sprites import Event_block, Battle
from core.states.statemachine import GameState
from core.files import battle_music
from core.colors import black
from core.effects.crossfade import *


class BattleState(GameState):
    def __init__(self, screen: pygame.Surface):
        super(BattleState, self).__init__()
        self.font = pygame.font.SysFont("Lucida Console", 10)
        self.music_channel = pygame.mixer.Channel(4)
        self.music = SoundGroup("Battle")
        self.music.add_sound(Sound(self.music_channel, battle_music[0]))
        self.music.add_sound(Sound(self.music_channel, battle_music[1], True))
        self.player_pokemon = "No Pokemon"
        self.battle_sprite = Battle(screen)
        self.shadow = CrossFade(screen)
        self.fade = pygame.sprite.Group(self.shadow)
        self.screen = screen
        self.faded = False
        self.screenshot = pygame.image.load("images/screenshot.png")

    def onEnable(self):
        self.music.play()
        self.set_message("")
        self.shadow.fade_dir = -1
        self.shadow.trans_value = 0
        self.shadow.fade_speed = 6

    def onDisable(self):
        self.music.stop()

    def set_message(self, text):
        self.message = self.font.render(text, True, white, white)
        self.previous_message = self.message

    def onUpdate(self, deltaTime, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                Event_block.switch_mode = False
                self.battle_sprite.number = 0
                Battle.trigger0 = True
                Battle.trigger1 = False
                Battle.trigger2 = False
                self.deactivateSelf()
        
        self.music.update()
        enemy_pokemon = self.font.render(str(Event_block.pokemon_str),True,black)
        player_pokemon = self.font.render((self.player_pokemon),True,black)
        self.battle_sprite.prepare_battle(Event_block.pokemon,enemy_pokemon,player_pokemon)
        if Battle.trigger0 == True:
            self.battle_sprite.intro()
        elif Battle.trigger1 == True:
            self.battle_sprite.bring_in_player()
        elif Battle.trigger2 == True:
            self.battle_sprite.send_out_pokemon_waiting()
            inform = self.font.render('A wild ' + str(Event_block.pokemon_str) + ' has appeared, but',True,white)
            inform2 = self.font.render('you have no Pokemon! Press Enter',True,white)
            inform3 = self.font.render('to Flee..',True,white)
            self.screen.blit(inform,(15,120))
            self.screen.blit(inform2,(15,131))
            self.screen.blit(inform3,(15,142))

        if (self.shadow.trans_value != 255 and not self.faded):
            self.fade.clear(self.screen, self.screenshot)
        else:
            self.faded = True
            self.shadow.fade_dir = 1
            self.shadow.fade_speed = 3

        self.fade.update()
        self.fade.draw(self.screen);
