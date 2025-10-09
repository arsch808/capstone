import pygame
from pygame.locals import *

# pygame setup
pygame.init()
pygame.display.set_caption("World Explorer")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

cursor = pygame.image.load('PLACEHOLDER_cursor.bmp').convert_alpha() #placeholder mouse cursor
background = pygame.image.load('stars.bmp').convert() #placeholder background
mars = pygame.image.load('mars.bmp')

#header position
header = Rect((200, 50), (800, 100))

#define Rect object for the slider to use
sizebox = Rect((20, 600), (100, 10))
distbox = Rect((220, 600), (100, 10))
waterbox = Rect((420, 600), (100, 10))
atmosbox = Rect((620, 600), (100, 10))

#setting a clipping box to limit what draws on the screen
#screen.set_clip(0,0,640,300) #starting at x,y, following call will only draw w/i (640,300)
#draw_area()

color = [127,127,127]

#font = pygame.font.SysFont('Arial', 16)
#title = font.render("Welcome to the Worlds Explorer", True, (255, 255, 255), background=None)

while running:
#DEFINE EVENTS HERE
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user clicks x to close the window
            running = False   

    # wipe last frame
    screen.fill("black")

    screen.blit(background, (0,0))

    #drawing control placeholders onto the screen
    pygame.draw.rect(screen, (255,255,255), sizebox)
    pygame.draw.rect(screen, (255,255,255), distbox)
    pygame.draw.rect(screen, (255,255,255), waterbox)
    pygame.draw.rect(screen, (255,255,255), atmosbox)

    pygame.draw.rect(screen, (255, 255, 255), header)

    
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    x, y = pygame.mouse.get_pos()
    x -= cursor.get_width()/2
    y -= cursor.get_height()/2
    screen.blit(cursor, (x, y))



    
    
#END: this handles the final display

    pygame.display.update()

    clock.tick(60)  #FPS 60

pygame.quit()



