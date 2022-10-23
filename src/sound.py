import pygame as pg
import time

import application as app

class Sound:
    def __init__(self):
        pg.mixer.init()

        self.chomp_channel = pg.mixer.find_channel()

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

        self.siren = [f'{app.Application.PROJECT_DIR}/resources/sounds/siren_{x}.wav' for x in range (1,6)]
        self.power_pellet = f'{app.Application.PROJECT_DIR}/resources/sounds/pill_sound.wav'

        pg.mixer.music.load(self.siren[0])
        pg.mixer.music.set_volume(0.35)
        self.chomp_channel.set_volume(0.5)

    def stop_bg(self):
        pg.mixer.music.stop()

    def play_bg(self):
        pg.mixer.music.play(-1, 0.0)

    def ghost_run(self):
        pg.mixer.Sound.play(self.sfx['ghost_run'])

    def chomp(self):
        if not self.chomp_channel.get_busy():
            self.chomp_channel.play(self.sfx['chomp'])

    def power_up(self):
        pg.mixer.Sound.play(self.sfx['power'])

    def eat_ghost(self):
        pg.mixer.Sound.play(self.sfx['eat_ghost'])

    def game_over(self):
        self.stop_bg()
        pg.mixer.Sound.play(self.sfx['game_over'])
        time.sleep(2.8)
    
    def update(self):
        pass
