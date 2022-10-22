import pygame as pg
import time


class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        pg.mixer.music.set_volume(0.7)

        # level_up_sound = pg.mixer.Sound('sounds/ .wav')
        ghost_run_sound = pg.mixer.Sound('sounds/ pacman_intermission.wav')
        game_over_sound = pg.mixer.Sound('sounds/death.wav')
        points_sound = pg.mixer.Sound('sounds/pacman_chomp.wav')
        power_pill_sound = pg.mixer.Sound('sounds/pill_sound.wav')
        pacman_eat_ghost = pg.mixer.Sound('sounds/pacman_eatghost.wav')
        self.sounds = {'level_up': level_up_sound, 'ghost_run': ghost_run_sound, 'game_over': game_over_sound,
                       'points': points_sound, 'power': power_pill_sound, 'eat_ghost': pacman_eat_ghost}

    def stop_bg(self):
        pg.mixer.music.stop()

    # def level_up(self): pg.mixer.Sound.play(self.sounds['level_up'])

    def play_bg(self):
        pg.mixer.music.play(-1, 0.0)

    def ghost_run(self):
        pg.mixer.Sound.play(self.sounds['ghost_run'])

    def points(self):
        pg.mixer.Sound.play(self.sounds['points'])

    def power_up(self):
        pg.mixer.Sound.play(self.sounds['power'])

    def eat_ghost(self):
        pg.mixer.Sound.play(self.sounds['eat_ghost'])

    def game_over(self):
        self.stop_bg()
        pg.mixer.music.load('sounds/death.wav')
        self.play_bg()
        time.sleep(2.8)
