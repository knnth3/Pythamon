"""
Module for managing platforms.
"""
import pygame

from spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

grass            = (80, 16, 16, 16)
GRASS_RIGHT           = (80, 16, 16, 16)
GRASS_MIDDLE          = (80, 16, 16, 16)
STONE_PLATFORM_LEFT   = (80, 16, 16, 16)
STONE_PLATFORM_MIDDLE = (80, 16, 16, 16)
STONE_PLATFORM_RIGHT  = (80, 16, 16, 16)

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("images/Exterior_Tileset.png")
        # Grab the image for this platform
        self.sprite_image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        return self.sprite_image