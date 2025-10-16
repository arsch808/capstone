import pygame
import pygame_gui

#initialize and set up pygame
pygame.init()
pygame.display.set_caption('World Explorer')
clock = pygame.time.Clock()
is_running = True


#default window surface. everything should be attached to here unless otherwise stated
screen = pygame.display.set_mode((1280, 720))
manager = pygame_gui.UIManager((1280, 720))

#create a display background
background = pygame.image.load('stars.bmp').convert() #placeholder background, convert() makes the image easier to handle
cursor = pygame.image.load('PLACEHOLDER_cursor.bmp').convert_alpha()


#inputs
sizeslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((20, 650), (200, 25)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)
distslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((330, 650), (200, 25)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)
denslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((690, 650), (200, 25)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)
tempslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((1010 , 650), (200, 25)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)

#display image
mars = pygame.image.load('mars.bmp').convert()

image = pygame_gui.elements.ui_image.UIImage(
    ((25, 100), (500, 500)), mars)

#"checkbox" for if a parameter matches
dist_checkbox = pygame.Rect((640, 120), (150, 100))
size_checkbox = pygame.Rect((790, 120), (150, 100))
dens_checkbox = pygame.Rect((940, 120), (150, 100))
temp_checkbox = pygame.Rect((1090, 120), (150, 100))


#text 
title_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((330,20), (600, 100)),
    text="Worlds Explorer",
    manager=manager,
    object_id='title_label')

textRect = pygame.Rect((640, 240), (620,200))

#set_image(new_image: ~pygame.surface.Surface) allows image to change during runtime (screensaver)


while is_running:

    #DEFINE EVENTS HERE
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False


        manager.process_events(event)

    manager.update(time_delta)

    #drawing onto the screen
    screen.blit(background, (0, 0))
    manager.draw_ui(screen)
    
    pygame.draw.rect(screen, 'white', dist_checkbox)
    pygame.draw.rect(screen, 'black' , size_checkbox)
    pygame.draw.rect(screen, 'white', dens_checkbox)
    pygame.draw.rect(screen, 'black', temp_checkbox)

    pygame.draw.rect(screen, 'white', textRect)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    x, y = pygame.mouse.get_pos()
    x -= cursor.get_width()/2
    y -= cursor.get_height()/2
    screen.blit(cursor, (x, y))
    

#END: final display
    pygame.display.update()


pygame.quit()
