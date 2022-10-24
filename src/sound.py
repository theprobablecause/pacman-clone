import pygame as pg
import application as app
import time

import application as app

class Sound:
    def __init__(self):
        pg.mixer.init()

        soud_game_over = pg.mixer.Sound(f'{app.Application.PROJECT_DIR}/resources/sounds/pacman_death.wav')
        sound_chomp = pg.mixer.Sound(f'{app.Application.PROJECT_DIR}/resources/sounds/pacman_chomp.wav')
        sound_power_pellet = pg.mixer.Sound(f'{app.Application.PROJECT_DIR}/resources/sounds/pill_sound.wav')
        sound_eat_ghost = pg.mixer.Sound(f'{app.Application.PROJECT_DIR}/resources/sounds/pacman_eatghost.wav')
        self.sfx = {
            'game_over': soud_game_over,
            'chomp': sound_chomp,
            'power_pellet': sound_power_pellet,
            'eat_ghost': sound_eat_ghost
        }

        self.beginning_audio = f'{app.Application.PROJECT_DIR}/resources/sounds/pacman_beginning.wav'
        self.siren = [f'{app.Application.PROJECT_DIR}/resources/sounds/siren_{x}.wav' for x in range (1,6)]
        self.audio_power_pellet = f'{app.Application.PROJECT_DIR}/resources/sounds/pill_sound.wav'

        self.chomp_channel = pg.mixer.Channel(1)
        self.sfx_channel = pg.mixer.Channel(2)
    
        self.chomp_channel.set_volume(0.5)
        self.sfx_channel.set_volume(0.6)
        
        pg.mixer.music.set_volume(0.35)
        self.music_normal()

    def music_stop(self):
        pg.mixer.music.stop()

    def music_normal(self):
        self.music_stop()
        pg.mixer.music.load(self.siren[0])
        pg.mixer.music.play(-1, 0.0)

    def music_beginning(self):
        self.music_stop()
        pg.mixer.music.load(self.beginning_audio)
        pg.mixer.music.play(0, 0.0)

    def music_power_pellet(self):
        self.music_stop()
        pg.mixer.music.load(self.audio_power_pellet)
        pg.mixer.music.play(loops=-1)

    def start_chomping(self):
        if not self.chomp_channel.get_busy():
            self.chomp_channel.play(self.sfx['chomp'], loops=-1)
    
    def stop_chomping(self):
        self.chomp_channel.stop()

    def eat_ghost(self):
        self.sfx_channel.play(self.sfx['eat_ghost'])

    def game_over(self):
        self.music_stop()
        pg.mixer.Sound.play(self.sfx['game_over'])
        time.sleep(2.8)
    
    def update(self):
        pass
