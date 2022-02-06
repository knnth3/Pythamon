#!/usr/bin/env python

import pygame
from pygame.locals import *
from core.colors import *
from core.sprites import *
from core.files import *
from core.effects.crossfade import *
from core.states.battlestate import BattleState
from core.states.mainstate import MainState
from core.states.statemachine import StateMachine

if ( __name__ == "__main__" ):
    pygame.init()
    pygame.mixer.init()

    window_size = (960,640)
    display = pygame.display.Info()
    pos_x = (display.current_w / 2) - (window_size[0] / 2)
    pos_y = (display.current_h / 2) - (window_size[1] / 2)
    print(pos_x, pos_y)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (pos_x, pos_y)
    screen_size = (screen_width,screen_height)
    screen = pygame.display.set_mode(screen_size, HWSURFACE|DOUBLEBUF|RESIZABLE)
    render_screen = screen.copy()
    screen = pygame.display.set_mode(window_size, HWSURFACE|DOUBLEBUF|RESIZABLE)

    pygame.display.set_caption("PyThamon")
    icon = icon.convert_alpha()
    pygame.display.set_icon(icon)
    
    running = True
    frames_per_second = 60
    # pygame.key.set_repeat(1, frames_per_second)
    clock = pygame.time.Clock()
    state_machine = StateMachine(MainState(render_screen))
    while (running):
        clock.tick(frames_per_second)
        game_events = pygame.event.get()
        for event in game_events:
            if event.type == pygame.QUIT:
                running = False
        
        state_machine.update(clock.get_time(), game_events)
        screen.blit(pygame.transform.scale(render_screen, screen.get_rect().size), (0, 0))
        pygame.display.flip()

    pygame.quit()
