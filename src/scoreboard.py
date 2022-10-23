import pygame as pg

class Scoreboard():
    power_pallet_points = 100
    dot_food_points = 10
    ghost_points = 200

    def __init__(self, game): # game is an instance of application class/game
        # what is settings in this case if we compare with the space invaders ?
        self.score = 0
        self.level = 0
        self.high_score = 0
        self.game = game # using the entire application class by using its instance game ?
        self.screen = game.screen # accessing application screen variable ?
        self.screen_rect = self.screen.get_rect() 
        self.text_color = (255, 255, 255) # white color
        self.font = pg.font.SysFont(None, 48) # no font type assigned and size 48
        self.score_image = None 
        self.score_rect = None
        self.high_score_image = None
        self.high_score_rect = None
        self.prep_score_graphics()


    def save_high_score(self):
        print(f'Attempting to save our score ({self.score}/{self.high_score})')
        self.high_score = self.score if self.high_score < self.score else self.high_score
        with open('high_score.txt', 'w') as f:
            f.write(str(self.high_score))
        self.prep_score_graphics()


    def increment_points_power_pallet(self):
        self.score = self.score + Scoreboard.power_pallet_points
        self.prep_score_graphics()

    def increment_points_ghost(self):
        self.score = self.score + Scoreboard.ghost_points
        self.prep_score_graphics()

    def increment_points_dot(self):
        self.score = self.score + Scoreboard.dot_food_points
        self.prep_score_graphics()


    def prep_score_graphics(self):
        score_str = f'Score: {str(self.score)}'
        high_score_str = f'High Score: {str(self.high_score)}'
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

        # Display high score at top middle of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.center = self.screen_rect.center
        self.high_score_rect.top = 20


    def reset(self):
        self.save_high_score()
        self.score = 0
        self.update()


    def update(self):
        self.prep_score_graphics()
        self.draw()


    def draw(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)


        



        