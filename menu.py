import pygame as pg
import sys
from button import Button
import game as gm


class Menu():
    def __init__(self):
        pg.init()
        self.screen_height = 800
        self.screen_width = 1200
        size = self.screen_width, self.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
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

            self.hs_back = Button(image=None, pos=(100, 700), text_input="Menu", font=self.get_font(45), base_color="Blue", hovering_color="Red")
            self.hs_back.changeColor(self.score_mouse_pos)
            self.hs_back.update(self.screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.hs_back.checkForInput(self.score_mouse_pos):
                        self.frame = 0
                        self.set_mode(self.frame)
            pg.display.update()

    def play(self):
        while True:

            self.play_pos = pg.mouse.get_pos()
            self.screen.fill("black")
            self.menu_back = Button(image=None, pos=(100, 720), text_input="Menu", font=self.get_font(30), base_color="Blue", hovering_color="Red")
            self.menu_back.changeColor(self.play_pos)
            self.menu_back.update(self.screen)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.menu_back.checkForInput(self.play_pos):
                        self.frame = 0
                        self.set_mode(self.frame)
                        # self.set_mode(0)
            pg.display.update()

    def set_mode(self, mode):
        if mode == 0:
            self.main_menu()
        elif mode == 1:
            self.play()
        elif mode == 2:
            self.high_score_screen()
        elif mode == 3:
            pg.quit()
            sys.exit()

    def display_img(self):
        clock = pg.time.Clock()
        img = [pg.transform.rotozoom(pg.image.load(gm.Game.PROJECT_DIR + f'/pacman_img/tile{n}.png'), 0, 1.0) for n in range(85)]
        for i in range(len(img)):
            if i >= len(img):
                i = 0
            self.image = img[i]
            # i += 1
            self.img_rect = self.image.get_rect(center=(600, 400))
            self.screen.blit(self.image, self.img_rect)
            pg.display.update(self.img_rect)
            self.image.set_colorkey((0, 0, 0))
            i += 1
            clock.tick(60)
            
            # pg.display.update(self.img_rect)
        
            
        
        # for i in range(len(img)):
        #     if i >= len(img):
        #         i = 0
        #     image = img[i]
        #     self.img_rect = image.get_rect(center=(600, 400))
        #     self.screen.blit(image, self.img_rect)
        #     pg.display.update(self.img_rect)
        #     image.set_colorkey((0, 0, 0))
        #     i += 1
        # # pg.display.update(self.img_rect)
        # # pg.display.update()
        # clock.tick(30) 
              
        # pg.quit()
   

    # def starter_screen(self):
    #     clock2 = pg.time.Clock()
    #     while True:
    #         self.screen.fill('black')
    #         self.menu_mouse_pos = pg.mouse.get_pos()

    #         self.menu_button = Button(None, pos=(600, 400), text_input="MENU", font=self.get_font(40), base_color="Yellow", hovering_color="Blue")
    #         self.quit_button = Button(None, pos=(600, 600), text_input="QUIT", font=self.get_font(40), base_color="Yellow", hovering_color="Red")

    #         for button in [self.menu_button, self.quit_button]:
    #             button.changeColor(self.menu_mouse_pos)
    #             button.update(self.screen)
    #         clock2.tick(60)

    #         for event in pg.event.get():
    #             if event.type == pg.QUIT:
    #                 pg.quit()
    #                 sys.exit()

    #             if event.type == pg.MOUSEBUTTONDOWN:
    #                 if self.menu_button.checkForInput(self.menu_mouse_pos):
    #                     self.frame = 0
    #                     self.set_mode(self.frame)

    #                 if self.quit_button.checkForInput(self.menu_mouse_pos):
    #                     self.frame = 3
    #                     self.set_mode(self.frame)
    #         pg.display.update()

    def main_menu(self):
        clock = pg.time.Clock()

        while True:
            self.screen.fill((0, 0, 0))
            self.menu_mouse_pos = pg.mouse.get_pos()
            img_pacman = pg.image.load(gm.Game.PROJECT_DIR + "/pacman_img/pacman.png")
            image = pg.transform.scale(img_pacman, (200,200))
            self.img_rect = image.get_rect(center=(575, 110))
            self.screen.blit(image, self.img_rect)
            
            img_pacmanghost = pg.image.load(gm.Game.PROJECT_DIR + "/pacman_img/ghostintro.jpg")
            image2 = pg.transform.scale(img_pacmanghost, (260,160))
            self.img2_rect = image2.get_rect(center=(575, 560))
            self.screen.blit(image2, self.img2_rect)


            self.menu_text = self.get_font(140).render(" PA " + " MAN", True, "White")
            self.menu_rect = self.menu_text.get_rect(center=(570, 100))
            self.screen.blit(self.menu_text, self.menu_rect)

            self.play_button = Button(None, pos=(600, 680), text_input="PLAY", font=self.get_font(20), base_color="Yellow", hovering_color="Blue")
            self.high_score_button = Button(None, pos=(600, 715), text_input="HIGH SCORE", font=self.get_font(20), base_color="Yellow", hovering_color="Pink")
            self.quit_button = Button(None, pos=(600, 750), text_input="QUIT", font=self.get_font(20), base_color="Yellow", hovering_color="Red")

            # pacman_image = [pg.transform.rotozoom(pg.image.load(f'pacman_img/tile{n}.png'), 0, 0.7) for n in range(154)]
            
            for button in [self.play_button, self.high_score_button, self.quit_button]:
                button.changeColor(self.menu_mouse_pos)
                button.update(self.screen)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.play_button.checkForInput(self.menu_mouse_pos):
                        pg.display.set_caption("PACMAN GAME")
                        self.frame = 1
                        self.set_mode(self.frame)
                        # self.play()
                    if self.high_score_button.checkForInput(self.menu_mouse_pos):
                        pg.display.set_caption("PACMAN High Score")
                        self.frame = 2
                        self.set_mode(self.frame)
                        # self.high_score_screen()
                    if self.quit_button.checkForInput(self.menu_mouse_pos):
                        self.frame = 3
                        self.set_mode(self.frame)
                        
            pg.display.update()
            self.display_img()
            clock.tick(60)