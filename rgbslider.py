import pygame
from pygame.locals import *

# pygame setup
pygame.init()
pygame.display.set_caption("World Explorer")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

cursor = pygame.image.load('PLACEHOLDER_cursor.bmp') #placeholder mouse cursor
background = pygame.image.load('stars.bmp') #placeholder background
mars = pygame.image.load('mars.bmp') 

#example rgb sliders from "Beginning Game Development with Python and Pygame"
def create_scales(height):
    red_scale_surface = pygame.surface.Surface((640, height))
    green_scale_surface = pygame.surface.Surface((640, height))
    blue_scale_surface = pygame.surface.Surface((640, height))
    for x in range(640):
        c = int((x/639.)*255.)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        line_rect = Rect(x, 0, 1, height)
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)
    return red_scale_surface, green_scale_surface, blue_scale_surface
red_scale, green_scale, blue_scale = create_scales(80)

color = [127,127,127]

while running:
#DEFINE EVENTS HERE
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user clicks x to close the window
            running = False   

    # wipe last frame
    screen.fill("black")
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    screen.blit(background, (0,0))

    
    
#event for the rbg slider example     
    # Draw the scales to the screen
    screen.blit(red_scale, (10, 10))
    screen.blit(green_scale, (20, 10))
    screen.blit(blue_scale, (30, 10))
    x, y = pygame.mouse.get_pos()
    # If the mouse was pressed on one of the sliders, adjust the color component
    if pygame.mouse.get_pressed()[0]:
        for component in range(3):
            if y > component*80 and y < (component+1)*80:
                color[component] = int((x/639.)*255.)
        pygame.display.set_caption("PyGame Color Test - "+str(tuple(color)))
 #Draw a circle for each slider to represent the current setting
    for component in range(3):
        pos = ( int((color[component]/255.)*639), component*80+40 )
        pygame.draw.circle(screen, (255, 255, 255), pos, 20)
    pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))


    
#END: this handles the final display

    pygame.display.flip()

    clock.tick(60)  #FPS 60

pygame.quit()



