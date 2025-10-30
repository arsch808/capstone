import pygame
import pygame_gui
import csv
import random

#initalize pygame
pygame.init()
pygame.display.set_caption('Its_Alive')
clock = pygame.time.Clock()
is_running = True

#set up the main window surface and gui manager
screen = pygame.display.set_mode((1920, 1090))
manager = pygame_gui.UIManager((1920, 1080))

#background
background = pygame.Surface((1920, 1080))
background.fill(pygame.Color('#000000'))


#title text
title_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((20,20), (1880, 130)),
    text="What does it take to be habitable in space?",
    manager=manager,
    object_id='title_label')


#input sliders
sizeslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((20, 200), (450, 30)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)
distslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((480, 200), (450, 30)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)
denslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((960, 200), (450, 30)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)
tempslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((1440, 200), (450, 30)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)

#parameter graphics

check = pygame.image.load('graphics/check.png').convert()
uncheck = pygame.image.load('graphics/uncheck.png').convert()

small_graphic = pygame.image.load('graphics/small.png').convert()
medium_graphic = pygame.image.load('graphics/medium.png').convert()
big_graphic = pygame.image.load('graphics/large.png').convert()
giant_graphic = pygame.image.load('graphics/giant.png').convert()

close_graphic = pygame.image.load('graphics/close.png').convert()
inner_graphic = pygame.image.load('graphics/inner.png').convert()
outer_graphic = pygame.image.load('graphics/outer.png').convert()
distant_graphic = pygame.image.load('graphics/distant.png').convert()

rocky_graphic = pygame.image.load('graphics/rocky.png').convert()
earthy_graphic = pygame.image.load('graphics/rocky.png').convert()
watery_graphic = pygame.image.load('graphics/watery.png').convert()
neptune_graphic = pygame.image.load('graphics/neptune.png').convert()

freeze_graphic = pygame.image.load('graphics/freeze.png').convert()
temperate_graphic = pygame.image.load('graphics/temp.png').convert()
hot_graphic = pygame.image.load('graphics/hot.png').convert()
wild_graphic = pygame.image.load('graphics/wild.png').convert()

#parameter icons

size_icon = pygame_gui.elements.ui_image.UIImage(
    relative_rect = pygame.rect.Rect((20, 100), (100, 100)),
    image_surface = small_graphic,
    manager = manager,
    visible = 1)

dist_icon = pygame_gui.elements.ui_image.UIImage(
    relative_rect = pygame.rect.Rect((480, 100), (100,100)),
    image_surface = close_graphic,
    manager = manager,
    visible = 1)

dens_icon = pygame_gui.elements.ui_image.UIImage(
    relative_rect = pygame.rect.Rect((960, 100), (100,100)),
    image_surface = rocky_graphic,
    manager = manager,
    visible = 1)

temp_icon = pygame_gui.elements.ui_image.UIImage(
    relative_rect = pygame.rect.Rect((1440, 100), (100,100)),
    image_surface = freeze_graphic,
    manager = manager,
    visible = 1)

#planet images

callisto_image = pygame.image.load('images/Callisto.jpg').convert()
ceres_image = pygame.image.load('images/Ceres.jpg').convert()
enceladus_image = pygame.image.load('images/Enceladus.png').convert()
europa_image = pygame.image.load('images/Europa.jpg').convert()
ganymede_image = pygame.image.load('images/Ganymede.jpg').convert()
io_image = pygame.image.load('images/Io.png').convert()
mars_image = pygame.image.load('images/Mars.png').convert()
mercury_image = pygame.image.load('images/Mercury.jpg').convert()
pluto_image = pygame.image.load('images/Pluto.jpg').convert()
titan_image = pygame.image.load('images/Titan.png').convert()
venus_image = pygame.image.load('images/Venus.jpg').convert()


planet_image_box = pygame_gui.elements.ui_image.UIImage(
    relative_rect = pygame.rect.Rect((120, 400), (600, 600)),
    image_surface = mars_image,
    manager = manager,
    visible = 1)
                                


#planet info UI boxes

planet_name_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text='planet name',
    relative_rect=pygame.Rect((960, 350), (940, 150)),
    manager=manager)

planet_fact_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text='planet text',
    relative_rect = pygame.Rect((960, 540), (940,360)),
    manager=manager)

planet_size_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text='planet size',
    relative_rect = pygame.Rect((200, 250), (240, 40)),
    manager = manager)

planet_dist_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text='planet dist',
    relative_rect = pygame.Rect((680, 250), (240, 40)),
    manager = manager)

planet_dens_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text='planet dens',
    relative_rect = pygame.Rect((1150, 250), (240, 40)),
    manager = manager)

planet_temp_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text = 'planet temp',
    relative_rect = pygame.Rect((1660, 250), (240, 40)),
    manager=manager)
    

    
    
#this is labeling text that doesnt change
Size_UILabel = pygame_gui.elements.ui_label.UILabel(
    relative_rect=pygame.rect.Rect((200, 100), (150, 50)),
    text="SIZE",
    manager=manager,
    object_id='main_label')

Distance_UILabel = pygame_gui.elements.ui_label.UILabel(
    relative_rect=pygame.rect.Rect((700, 100), (150, 50)),
    text="DISTANCE",
    manager=manager,
    object_id='main_label')

Density_UILabel = pygame_gui.elements.ui_label.UILabel(
    relative_rect=pygame.rect.Rect((1100, 100), (150, 50)),
    text="DENSITY",
    manager=manager,
    object_id='main_label')

Temp_UILabel = pygame_gui.elements.ui_label.UILabel(
    relative_rect=pygame.rect.Rect((1600, 100), (150, 50)),
    text="TEMPERATURE",
    manager=manager,
    object_id='main_label')

#these labels change based on what the user has chosen
size_label = pygame_gui.elements.ui_text_box.UITextBox(
    html_text = 'Size',
    relative_rect = pygame.rect.Rect((200, 150), (240, 40)),
    manager = manager,
    object_id='param_label')

dist_label = pygame_gui.elements.ui_text_box.UITextBox(
    html_text= 'Distance',
    relative_rect = pygame.rect.Rect((680, 150), (240, 40)),
    manager= manager,
    object_id='param_label')

dens_label = pygame_gui.elements.ui_text_box.UITextBox(
    html_text= 'Density',
    relative_rect = pygame.rect.Rect((1150, 150), (240, 40)),
    manager=manager,
    object_id='param_label')

temp_label = pygame_gui.elements.ui_text_box.UITextBox(
    html_text= 'Temp',
    relative_rect = pygame.rect.Rect((1660, 150), (240, 40)),
    manager=manager,
    object_id='param_label')

#search button
search_button = pygame_gui.elements.UIButton(
    relative_rect = pygame.Rect((960, 1000), (100,100)),
    text='SEARCH',
    manager=manager)

#comparison function that searches csv for a best match
def compare(filename, s, d, p, t):
    best_match_arrays = []
    max_matches = -1
    
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            current_matches = 0
            # Compare s, d, p, t to columns 2, 3, 4, 5 (indices 1, 2, 3, 4)
            target = [s, d, p, t]
            for i in range(4):  # Compare the first four columns
                if float(target[i]) == float(row[i + 1]):  # Adjust index for CSV
                    current_matches += 1

            if current_matches > max_matches:
                max_matches = current_matches
                best_match_arrays = [row]  # Reset list with new best match
            elif current_matches == max_matches:
                best_match_arrays.append(row)  # Add to list of equally good matches

        # Choose random match from best matches
        if best_match_arrays:
            best_match_array = random.choice(best_match_arrays)
            planet_name = best_match_array[0]
            planet_size = best_match_array[1]
            planet_distance = best_match_array[2]
            planet_density = best_match_array[3]
            planet_temperature = best_match_array[4]
            planet_text = best_match_array[5]

            
#main loop of game window
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        #SELECTION PHASE
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == sizeslide:
                size_slider_value = sizeslide.get_current_value()
                if size_slider_value == 0:
                    size_label.clear()
                    size_label.set_text('Small')
                    size_icon.set_image(small_graphic)
                elif size_slider_value == 1:
                    size_label.clear()
                    size_label.set_text('Medium')
                    size_icon.set_image(medium_graphic)
                elif size_slider_value == 2:
                    size_label.clear()
                    size_label.set_text('Big')
                    size_icon.set_image(big_graphic)
                elif size_slider_value == 3:
                    size_label.clear()
                    size_label.set_text('Giant')
                    size_icon.set_image(giant_graphic)
                    
            if event.ui_element == distslide:
                dist_slider_value = distslide.get_current_value()
                if dist_slider_value == 0:
                    dist_label.clear()
                    dist_label.set_text('Close')
                    dist_icon.set_image(close_graphic)
                elif dist_slider_value == 1:
                    dist_label.clear()
                    dist_label.set_text('Inner')
                    dist_icon.set_image(inner_graphic)
                elif dist_slider_value == 2:
                    dist_label.clear()
                    dist_label.set_text('Outer')
                    dist_icon.set_image(outer_graphic)
                elif dist_slider_value == 3:
                    dist_label.clear()
                    dist_label.set_text('Distant')
                    dist_icon.set_image(distant_graphic)

            if event.ui_element == denslide:
                dens_slider_value = denslide.get_current_value()
                if dens_slider_value == 0:
                    dens_label.clear()
                    dens_label.set_text('100% Rocky')
                    dens_icon.set_image(rocky_graphic)
                elif dens_slider_value == 1:
                    dens_label.clear()
                    dens_label.set_text('Rocky/Watery')
                    dens_icon.set_image(earthy_graphic)
                elif dens_slider_value == 2:
                    dens_label.clear()
                    dens_label.set_text('Water World')
                    dens_icon.set_image(watery_graphic)
                elif dens_slider_value == 3:
                    dens_label.clear()
                    dens_label.set_text('Mini-Neptune')
                    dens_icon.set_image(neptune_graphic)

            elif event.ui_element == tempslide:
                temp_slider_value = tempslide.get_current_value()
                if temp_slider_value == 0:
                    temp_label.clear()
                    temp_label.set_text('Freezing')
                    temp_icon.set_image(freeze_graphic)
                elif temp_slider_value == 1:
                    temp_label.clear()
                    temp_label.set_text('Temperate')
                    temp_icon.set_image(temperate_graphic)
                elif temp_slider_value == 2:
                    temp_label.clear()
                    temp_label.set_text('Scalding')
                    temp_icon.set_image(hot_graphic)
                elif temp_slider_value == 3:
                    temp_label.clear()
                    temp_label.set_text('Wildcard')
                    temp_icon.set_image(wild_graphic)

        
        #SEARCH PHASE
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == search_button:
                #csv is indexed from 0
                s = sizeslide.get_current_value()
                d = distslide.get_current_value()
                p = denslide.get_current_value()
                t = tempslide.get_current_value()
                compare('ss_test.csv', s,d,p,t)


                planet_name_box.clear()
                planet_name_box.set_text(planet_name)

                planet_text_box.clear()
                planet_text_box.set_text(planet_text)

            
            
        

        manager.process_events(event)

    manager.update(time_delta)

    #drawing onto the screen
    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    
    

#END: final display
    pygame.display.update()


pygame.quit()
