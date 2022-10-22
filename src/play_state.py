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
    def __init__(self):
        self.sw = PGStopwatch()
        self.level = 0
        """How many times the player has cleared the maze."""

        self.paused = False
        """Game will not be player-pausable; this is more for effect."""

        self.reset()

    def reset_after_death(self):

        self.mode_ghosts = 0
        '''Mode the ghosts should preferably stay at.
        
        Possible values:
        0: Scatter
        1: Chase
        2: Frightened'''

        self.mode_countdown = 420
        """Frames remaining until mode ends.
        
        scatter: 420
        chase: 1200"""

        # Tile coordinates for our portals
        self.portal_a = None
        self.portal_b = None

    def update():
        pass