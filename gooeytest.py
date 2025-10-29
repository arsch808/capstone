import pygame
import pygame_gui

#initialize and set up pygame
pygame.init()
pygame.display.set_caption('World Explorer')
clock = pygame.time.Clock()
is_running = True


#default window surface. everything should be attached to here unless otherwise stated
screen = pygame.display.set_mode((1920, 1080))
manager = pygame_gui.UIManager((1920, 1080))

#create a display background
background = pygame.image.load('stars.bmp').convert() #placeholder background, convert() makes the image easier to handle
cursor = pygame.image.load('PLACEHOLDER_cursor.bmp').convert_alpha()



#inputs
sizeslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((20, 200), (450, 30)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)
distslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((480, 200), (450, 30)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)
denslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((960, 200), (450, 30)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)
tempslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((1440, 200), (450, 30)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)

#display image
mars = pygame.image.load('mars.bmp').convert()

image = pygame_gui.elements.ui_image.UIImage(
    ((120, 400), (600, 600)), mars)


#text

title_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((20,20), (1880, 130)),
    text="Use the sliders to...",
    manager=manager,
    object_id='title_label')

planet_name = pygame_gui.elements.ui_text_box.UITextBox(
    html_text='planet name',
    relative_rect=pygame.Rect((960, 350), (940, 150)),
    manager=manager)

planet_text = pygame_gui.elements.ui_text_box.UITextBox(
    html_text='planet text',
    relative_rect=pygame.Rect((960, 540), (940,360)),
    manager=manager)

SIZE = pygame_gui.elements.ui_label.UILabel(
    relative_rect=pygame.rect.Rect((20, 240), (150, 50)),
    text="SIZE",
    manager=manager,
    object_id='main_label')

DIST = pygame_gui.elements.ui_label.UILabel(
    relative_rect=pygame.rect.Rect((720, 240), (150, 50)),
    text="DISTANCE",
    manager=manager,
    object_id='main_label')

DENS = pygame_gui.elements.ui_label.UILabel(
    relative_rect=pygame.rect.Rect((1200, 240), (150, 50)),
    text="DENSITY",
    manager=manager,
    object_id='main_label')

TEMP = pygame_gui.elements.ui_label.UILabel(
    relative_rect=pygame.rect.Rect((1650, 240), (150, 50)),
    text="TEMPERATURE",
    manager=manager,
    object_id='main_label')

size_label = pygame_gui.elements.ui_text_box.UITextBox(
    html_text = 'text',
    relative_rect = pygame.rect.Rect((200, 100), (240, 40)),
    manager = manager,
    object_id='param_label')

dist_label = pygame_gui.elements.ui_text_box.UITextBox(
    html_text= 'Distance',
    relative_rect = pygame.rect.Rect((680, 100), (240, 40)),
    manager= manager,
    object_id='param_label')

dens_label = pygame_gui.elements.ui_text_box.UITextBox(
    html_text= 'Density',
    relative_rect = pygame.rect.Rect((1150, 100), (240, 40)),
    manager=manager,
    object_id='param_label')

temp_label = pygame_gui.elements.ui_text_box.UITextBox(
    html_text= 'Temp',
    relative_rect = pygame.rect.Rect((1660, 100), (240, 40)),
    manager=manager,
    object_id='param_label')

planet_size = pygame_gui.elements.ui_text_box.UITextBox(
    html_text = 'text',
    relative_rect = pygame.rect.Rect((960, 270), (200, 50)),
    manager = manager,
    object_id='planet_label')


#icons

size_icon = pygame.rect.Rect((20,100),(100,100))

dist_icon = pygame.rect.Rect((480, 100), (100,100))

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

    pygame.draw.rect(screen, 'white', size_icon)
    pygame.draw.rect(screen, 'white', dist_icon)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    x, y = pygame.mouse.get_pos()
    x -= cursor.get_width()/2
    y -= cursor.get_height()/2
    screen.blit(cursor, (x, y))
    

#END: final display
    pygame.display.update()


pygame.quit()
