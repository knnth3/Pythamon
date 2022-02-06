import pygame

class Sound(object):
    def __init__(self, channel, soundUrl, loop: bool = False):
        self.channel = channel
        self.url = soundUrl
        self.playing = False
        self.enableLoop = loop
        self.instance = pygame.mixer.Sound(soundUrl)
    
    def loop(self):
        self.enableLoop = True
        return self

    def start_playing(self, force: bool = False):
        if force == True or self.channel.get_busy() == False:
            self.channel.play(self.instance)
            self.playing = True;
        
        return self.playing

    def stop_playing(self):
        self.playing = False
        self.channel.fadeout(1000)

    def is_playing(self):
        if not self.playing:
            return False

        return (self.channel.get_busy() is True)


class SoundGroup(object):
    def __init__(self, name: str):
        self.name = name
        self.soundlist: list[Sound] = [];
        self.playing_index = 0;
        self.playing = False;

    def add_sound(self, sound: Sound):
        print("Adding music to", self.name, ":", sound.url, ". Loop=", sound.enableLoop);
        self.soundlist.append(sound)
    
    def play(self):
        if self.playing or (len(self.soundlist) == 0):
            return
        
        self.playing_index = 0
        self.play_current()

    def play_current(self):
        if self.playing or (len(self.soundlist) == 0):
            return

        self.playing = True
        self.soundlist[self.playing_index].start_playing(True)

    def stop(self):
        if not self.playing:
            return

        self.playing = False
        self.soundlist[self.playing_index].stop_playing()
        self.playing_index = 0

    def update(self):
        if not self.playing:
            return
        
        self.playing = self.soundlist[self.playing_index].is_playing()
        if not self.playing:
            if not self.soundlist[self.playing_index].enableLoop:
                self.playing_index = (self.playing_index + 1) % len(self.soundlist)
            
            self.play_current()
    
