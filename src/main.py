import pygame as pg
import game_events as ge

RESOLUTION = (1024, 768)

class Game:
    FRAMES_PER_SECOND = 60
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(size=RESOLUTION)
        self.frame_clock = pg.time.Clock()

    def play(self):
        while True:
            ge.process_events(self)
            self.frame_clock.tick(Game.FRAMES_PER_SECOND)
            
    

def main():
    g = Game()
    g.play()

if __name__ == "__main__":
    main()