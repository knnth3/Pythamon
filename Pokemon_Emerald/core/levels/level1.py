from core.levels.level_base import LevelBase
from core.sprites import Block, Event_block, No_entry_block, SpriteSheet
from gamelayout.maps import tile_map_level_one
from core.files import *

class Level1( LevelBase ):
    def __init__( self, player_object ,screen):
        super( Level1, self ).__init__( player_object )
        sprite_sheet = SpriteSheet('images/Exterior_Tileset.png')
        TILESIZE = 16
        ROWS = 65
        COLUMNS = 40
        MAPHEIGHT = ROWS
        MAPWIDTH = COLUMNS
        #No_Entry_Block(non_passable) = [x,y,image]
        #Block(passable) = [x,y,image]
        #Event_Block(grass) = [screen,type("battle" or "teleport"),x,y,image]
        #Invisible_Queue is inserted in main game file because it is an indicator of a town and can be resised easily to fit an area.

        Tiles = {
          }
        for x in range(0, 6072):
          if x not in Tiles:
           Tiles[x] = [0,0,(sprite_sheet.get_image(s[x]))]

        Tiles[93] = [screen,"battle",0,0,(sprite_sheet.get_image(s[93]))]


        tile_map = tile_map_level_one
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
