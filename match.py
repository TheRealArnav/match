import pygame
from pygame.locals import*

pygame.init()


screen = pygame.display.set_mode((800,800))
screen.fill("white")

#images
subwaysurfers = pygame.image.load("C:/Pygame2/images/subwaysurfers.png")
templerun = pygame.image.load("C:/Pygame2/images/templerun.png")
candycrush = pygame.image.load("C:/Pygame2/images/candycrush.jpg")
ludo = pygame.image.load("C:/Pygame2/images/ludo.png")

#text
font = pygame.font.SysFont("Times New Roman",35)

subwaysurferstxt = font.render("Subway Surfers",True,"Black")

templeruntxt = font.render("Temple Run",True,"Black")

candycrushtxt = font.render("Candy Crush",True,"Black")

ludostxt = font.render("Ludo",True,"Black")

screen.blit(subwaysurfers,(50,50))
screen.blit(templerun,(50,225))
screen.blit(candycrush,(50,400))
screen.blit(ludo,(50,575))

screen.blit(ludostxt,(550,400))
screen.blit(templeruntxt,(550,575))
screen.blit(candycrushtxt,(550,225))
screen.blit(subwaysurferstxt,(550,50))


run = True
while run:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.circle(screen,"black",pygame.mouse.get_pos(),15,0)

    
    pygame.display.update()