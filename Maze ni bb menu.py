import pygame, sys
import os
#from button import Button
#import cv2


pygame.init()

SCREEN = pygame.display.set_mode((950, 650))
pygame.display.set_caption("DATAMIN-C")

#BG_play = pygame.image.load("E:/all/pychram/PycharmProjects/cpen65/maze image/Background.png")
#BG_play = pygame.transform.scale(BG_play, (950, 650))
#DEFAULT_IMAGE_SIZE = (950,650)
#BG_play = pygame.transform.scale(BG_play, DEFAULT_IMAGE_SIZE)

#########################################

BG = pygame.image.load("E:/all/pychram/PycharmProjects/cpen65/maze image/stars5.png")
BG = pygame.transform.scale(BG, (950, 650))
width = 950



class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

#font
def get_font(size):
    return pygame.font.Font("E:/all/pychram/PycharmProjects/cpen65/maze image/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        #SCREEN.blit(BG_play,(0,0))

        PLAY_TEXT = get_font(45).render("Pogi ni Rhonan", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(477, 120))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(477, 600),
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")

        PLAY_EASY = Button(image=None, pos=(477, 250),
                            text_input="EASY", font=get_font(40), base_color="White", hovering_color="yellow")

        PLAY_MEDIUM = Button(image=None, pos=(477, 320),
                            text_input="MEDIUM", font=get_font(40), base_color="White", hovering_color="Green")

        PLAY_HARD = Button(image=None, pos=(477, 390),
                            text_input="HARD", font=get_font(40), base_color="White", hovering_color="Blue")

        PLAY_EASY.changeColor(PLAY_MOUSE_POS)
        PLAY_EASY.update(SCREEN)

        PLAY_MEDIUM.changeColor(PLAY_MOUSE_POS)
        PLAY_MEDIUM.update(SCREEN)

        PLAY_HARD.changeColor(PLAY_MOUSE_POS)
        PLAY_HARD.update(SCREEN)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        OPTIONS_TEXT = get_font(30).render("Ang Pogi talga niyaa <333", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(447, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(447, 600),
                              text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")

        OPTIONS_SOUND = Button(image=None, pos=(447, 300),
                              text_input="Sound", font=get_font(40), base_color="Orange", hovering_color="Red")

        OPTIONS_CREDITS = Button(image=None, pos=(447, 360),
                               text_input="Credits", font=get_font(40), base_color="Orange", hovering_color="Light Green")

        OPTIONS_CREDITS.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_CREDITS.update(SCREEN)

        OPTIONS_SOUND.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_SOUND.update(SCREEN)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    class Button():
        def __init__(self, image, pos, text_input, font, base_color, hovering_color):
            self.image = image
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.font = font
            self.base_color, self.hovering_color = base_color, hovering_color
            self.text_input = text_input
            self.text = self.font.render(self.text_input, True, self.base_color)
            if self.image is None:
                self.image = self.text
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        def update(self, screen):
            if self.image is not None:
                screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)

        def checkForInput(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom):
                return True
            return False

        def changeColor(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom):
                self.text = self.font.render(self.text_input, True, self.hovering_color)
            else:
                self.text = self.font.render(self.text_input, True, self.base_color)

    i = 0
    run = True
    while run:
        SCREEN.blit(BG, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Create looping background
        SCREEN.blit(BG, (i, 0))
        SCREEN.blit(BG, (width + i, 0))
        if i == -width:
            SCREEN.blit(BG, (width + i, 0))
            i = 0
        i -= 1

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(55).render("aMAZEing Escape", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(477, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("E:/all/pychram/PycharmProjects/cpen65/maze image/Play Rect2.png"), pos=(477, 279),
                             text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=pygame.image.load("E:/all/pychram/PycharmProjects/cpen65/maze image/Options Rect2.png"), pos=(477, 370),
                                text_input="OPTIONS", font=get_font(50), base_color="#d7fcd4", hovering_color="Light Green")
        QUIT_BUTTON = Button(image=pygame.image.load("E:/all/pychram/PycharmProjects/cpen65/maze image/Options Rect2.png"), pos=(477, 460),
                             text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="Light Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)


        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()