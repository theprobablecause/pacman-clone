import pygame as pg

class PGStopwatch:
    """A stopwatch that uses PyGame's timing functions."""
    def __init__(self):
        self.reset()

    def reset(self, restart=False):
        self._base = None
        self._pause_delta = None
        self.started = False
        self.paused = False

        if restart: self.start()
    
    def start(self):
        if self.started:
            self.resume()
        else:
            self._base = pg.time.get_ticks()
            self.started = True
    
    def pause(self):
        self._pause_delta = self.elapsed()
        self.paused = True
    
    def resume(self):
        if self.started and self.paused:
            self.paused = False
            self._base = pg.time.get_ticks() - self._pause_delta

    def elapsed(self):
        if not self.started: return -1
        if self.paused:
            return self._pause_delta
        else:
            return pg.time.get_ticks() - self._base

    

class PlayState:
    MODE_TIMER = {
        0: 420,
        1: 1200,
        2: 700
    }
    """Frames remaining until mode ends. Should tick down every frame (1/60 of a second).
    
    Mode keys:
    0: scatter
    1: chase
    2: frightened"""

    def __init__(self, play):
        self.sw = PGStopwatch()
        self.play = play

        # Tile coordinates for our portals
        self.portal_a = None
        self.portal_b = None

        self.level = 0
        """How many times the player has cleared the maze."""

        self.action_pause = False
        """Game will not be player-pausable; this is more for effect."""

        self.is_frightened = False
        """Whether we are in frightened mode or not."""

        self.frightened_timer = PlayState.MODE_TIMER[2]
        """Frames remaining in frightened mode. Starts at 600."""

        self.mode_ghosts = 0
        '''Mode the ghosts should preferably stay at.
        
        Possible values:
        0: Scatter
        1: Chase'''

        self.mode_countdown = PlayState.MODE_TIMER[self.mode_ghosts]
        """Frames remaining until mode ends. Should tick down every frame (1/60 of a second)."""

        self.reset_after_death()

    def power_pellet_eatened(self):
        self.is_frightened = True
        self.frightened_timer = PlayState.MODE_TIMER[2]

    def reset_after_death(self):
        self.portal_a = None
        self.portal_b = None
        self.mode_ghosts = 0
        self.mode_countdown = PlayState.MODE_TIMER[self.mode_ghosts]

    def update_ghost_mode(self):
        if self.is_frightened:
            self.frightened_timer -= 1
            if self.frightened_timer <= 0:
                self.frightened_timer = PlayState.MODE_TIMER[2]
                self.is_frightened = False
                self.play.set_ghosts_mode(self.mode_ghosts)
                self.play.sound.music_normal()
        else:
            self.mode_countdown -= 1
            if self.mode_countdown <= 0:
                self.mode_ghosts = (self.mode_ghosts + 1) % 2
                self.mode_countdown = PlayState.MODE_TIMER[self.mode_ghosts]
                self.play.set_ghosts_mode(self.mode_ghosts)


    def update(self):
        self.update_ghost_mode()