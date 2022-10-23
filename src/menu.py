import pygame as pg
import sys
from timer import Timer
from button import Button
from play import Play

class Menu():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.animation = Timer(
            frames=[pg.transform.rotozoom(pg.image.load(f'pacman_img/tile{n}.png'), 0, 0.7) for n in range(154)],
            wait=1000/60
        )
        pg.display.set_caption("PACMAN Menu")
    
    def get_font(self, size):
        return pg.font.Font("resources/fonts/Press Start 2P.ttf", size)

    def high_score_screen(self):
        while True:
            self.score_mouse_pos = pg.mouse.get_pos()
            self.screen.fill("black")

            # top
            self.hss_text = self.get_font(60).render("HIGH SCORE", True, "White")
            self.hss_rect = self.hss_text.get_rect(center=(600, 50))
            self.screen.blit(self.hss_text, self.hss_rect)

            #high score
            self.hsscore_text = self.get_font(50).render("high score displayed", True, "Yellow")
            self.hsscore_rect = self.hsscore_text.get_rect(center=(600, 370))
            self.screen.blit(self.hsscore_text, self.hsscore_rect)

            # self.hsscore_rect = self.hsscore_image.get_rect()
            # self.hsscore_rect.center = self.screen_rect.center
            # self.hsscore_rect.top = 20
            # self.screen.blit(self.hsscore_image, self.hsscore_rect)

            self.hs_back = Button(image=None, pos=(100, 700), text_input="Back", font=self.get_font(45), base_color="Blue", hovering_color="Red")
            self.hs_back.changeColor(self.score_mouse_pos)
            self.hs_back.update(self.screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.hs_back.checkForInput(self.score_mouse_pos):
                        self.main_menu()
                        
            self.game.wait_next_frame()

    def draw_anim_frame(self):
            image = self.animation.imagerect()
            self.img_rect = image.get_rect(center=(600, 400))
            self.screen.blit(image, self.img_rect)
        

    def main_menu(self):
        self.screen.fill((0, 0, 0))
        img_pacman = pg.image.load("pacman_img/pacman.png")
        image = pg.transform.scale(img_pacman, (200,200))
        self.img_rect = image.get_rect(center=(575, 110))
        self.screen.blit(image, self.img_rect)


        self.menu_text = self.get_font(140).render(" PA " + " MAN", True, "White")
        menu_rect = self.menu_text.get_rect(center=(570, 100))


        self.play_button = Button(None, pos=(600, 580), text_input="PLAY", font=self.get_font(30), base_color="Yellow", hovering_color="Blue")
        self.high_score_button = Button(None, pos=(600, 640), text_input="HIGH SCORE", font=self.get_font(30), base_color="Yellow", hovering_color="Pink")
        self.quit_button = Button(None, pos=(600, 700), text_input="QUIT", font=self.get_font(30), base_color="Yellow", hovering_color="Red")

        while True:
            self.menu_mouse_pos = pg.mouse.get_pos()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.play_button.checkForInput(self.menu_mouse_pos):
                        pg.display.set_caption("PAC MAN")
                        p = Play(app=self.game)
                        p.run()
                    if self.high_score_button.checkForInput(self.menu_mouse_pos):
                        pg.display.set_caption("PACMAN High Score")
                        self.high_score_screen()
                    if self.quit_button.checkForInput(self.menu_mouse_pos):
                        pg.quit()
                        sys.exit()
            
            for button in [self.play_button, self.high_score_button, self.quit_button]:
                button.changeColor(self.menu_mouse_pos)
                button.update(self.screen)

            self.screen.blit(self.menu_text, menu_rect)
            self.draw_anim_frame()
            self.game.wait_next_frame()

