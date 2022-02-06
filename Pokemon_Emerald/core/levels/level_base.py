import pygame
from core.colors import black
from core.files import screen_width, screen_height

class LevelBase( object ):

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